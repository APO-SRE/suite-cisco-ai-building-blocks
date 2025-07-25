#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/llm/dynamic.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
 
"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""

"""
Dynamic helper that chooses the correct vector-search retriever and
builds the diet-function list the LLM receives.

* Never raises AttributeError if a given retriever class name is missing.
* Supports Chroma, Azure Cognitive Search and Elastic back-ends out-of-the-box.
* Falls back to the first "SomethingRetriever" class it can find, so adding new
  back-ends later is zero-touch.
* Implements intelligent function prioritization for all Cisco platforms.

ENV VARS
--------
FASTAPI_VECTOR_BACKEND              chroma | azure | elastic   (default: chroma)
FASTAPI_CHROMA_COLLECTION_PLATFORM  override Chroma collection name
FASTAPI_FUNCTION_TOKEN_BUDGET       max tokens for function payload (default: 16384)
FASTAPI_FUNCTION_TOP_K              number of functions to retrieve (default: 50)
"""
import importlib
import inspect
import json
import os
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional, Set
from collections import defaultdict

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# SEMANTIC MAPPINGS FOR INTELLIGENT SCORING
# ─────────────────────────────────────────────────────────────────────────────
SEMANTIC_MAPPINGS = {
    # What the user asks for -> what functions should match
    "servers": {
        "boost_terms": ["server", "compute", "physical", "rack", "blade", "node", "machine", "host"],
        "avoid_terms": ["profile", "policy", "setting", "disruption", "template"],
        "primary_functions": ["GetComputePhysicalSummaryList", "GetComputeRackUnitList", "GetComputeBladeList"]
    },
    "devices": {
        "boost_terms": ["device", "equipment", "hardware", "network", "controller", "router", "switch", "vedge", "cedge"],
        "avoid_terms": ["template", "policy", "config", "setting"],
        "primary_functions": ["getDeviceList", "getAllDeviceStatus", "getOrganizationDevices", "getNetworkDeviceList", "listAllDevices"]
    },
    "interfaces": {
        "boost_terms": ["interface", "port", "ethernet", "adapter", "nic", "network"],
        "avoid_terms": ["policy", "template", "profile"],
        "primary_functions": ["getAllInterfaces", "getInterfaces", "GetVnicEthIfList"]
    },
    "users": {
        "boost_terms": ["user", "account", "identity", "person", "people", "admin", "operator"],
        "avoid_terms": ["policy", "setting", "template"],
        "primary_functions": ["getUsers", "getUserList", "GetIamUserList", "findUsers_1"]
    },
    "alerts": {
        "boost_terms": ["alert", "alarm", "notification", "event", "warning", "issue", "problem"],
        "avoid_terms": ["policy", "template", "setting"],
        "primary_functions": ["GetCondAlarmList", "getSecurityAlerts", "getAlarmsCount", "getRawAlarmData", "getActiveAlarms"]
    },
    "networks": {
        "boost_terms": ["network", "vlan", "subnet", "fabric", "vpc", "segment"],
        "avoid_terms": ["policy", "template"],
        "primary_functions": ["getNetworks", "getNetworkList", "getOrganizationNetworks"]
    },
    "health": {
        "boost_terms": ["health", "status", "state", "condition", "monitoring"],
        "avoid_terms": ["policy", "template"],
        "primary_functions": ["getOverallNetworkHealth", "getSiteHealth", "getDeviceHealthStats", "getFabricHealth"]
    },
    "inventory": {
        "boost_terms": ["inventory", "assets", "equipment", "hardware"],
        "avoid_terms": ["policy", "template"],
        "primary_functions": ["getOrganizationInventoryDevices", "GetComputePhysicalSummaryList", "listAllDevices"]
    },
    "templates": {
        "boost_terms": ["template", "configuration", "blueprint", "model"],
        "avoid_terms": ["policy", "rule"],
        "primary_functions": ["getAllDeviceTemplates", "getFeatureTemplateList", "getTemplatePolicy"]
    },
    "sites": {
        "boost_terms": ["site", "location", "branch", "office", "campus"],
        "avoid_terms": ["policy", "template"],
        "primary_functions": ["getAllSites", "getSiteHealth", "getSites"]
    },
    "policies": {
        "boost_terms": ["policy", "rule", "configuration", "setting"],
        "avoid_terms": ["template", "device"],
        "primary_functions": ["getAllVedgePolicies", "getPolicyList", "getApplicationAwareRoutingPolicyList"]
    },
    "sdwan": {
        "boost_terms": ["sdwan", "sd-wan", "vmanage", "vedge", "cedge", "viptela"],
        "avoid_terms": ["meraki", "catalyst"],
        "primary_functions": ["listAllDevices", "getAllDeviceStatus", "getRawAlarmData"]
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# PLATFORM-SPECIFIC FUNCTION PRIORITIES
# ─────────────────────────────────────────────────────────────────────────────
FUNCTION_PRIORITIES = {
    "meraki": {
        # Organization and network management (most common)
        "getOrganizations": 95,
        "getOrganization": 90,
        "getNetworks": 90,
        "getNetwork": 85,
        "getOrganizationDevices": 85,
        "getDevices": 85,
        "getDevice": 80,
        
        # Configuration and monitoring
        "getNetworkClients": 75,
        "getOrganizationNetworks": 75,
        "getNetworkDevices": 70,
        "getDeviceClients": 70,
        
        # Specialized operations
        "getNetworkTraffic": 50,
        "getOrganizationInventoryDevices": 50,
        "updateDevice": 40,
        "createNetwork": 40,
        
        # Low priority - rarely needed directly
        "getNetworkSmDevices": 20,
        "getNetworkPiiRequests": 15,
        "getNetworkMqttBrokers": 10,
    },
    
    "catalyst": {
        # Device and interface management (most common)
        "getDeviceList": 95,
        "getAllInterfaces": 90,
        "getDeviceCount": 85,
        "getNetworkDeviceList": 85,
        "getInterfaces": 80,
        "getDeviceDetail": 80,
        
        # Network health and monitoring
        "getOverallNetworkHealth": 75,
        "getDeviceHealthStats": 70,
        "getSiteHealth": 70,
        
        # Configuration and discovery
        "getDiscoveryById": 50,
        "getGlobalPool": 50,
        "getSites": 50,
        
        # Specialized/administrative
        "getExecutionByExecutionId": 20,
        "getTaskById": 20,
        "getEventSubscriptions": 15,
    },
    
    "intersight": {
        # Server inventory (MOST common)
        "GetComputePhysicalSummaryList": 100,  # PRIMARY server list function
        "GetComputeRackUnitList": 75,
        "GetComputeBladeList": 75,
        "GetEquipmentChassisIdByMoid": 70,
        
        # Server management
        "GetServerProfileList": 40,  # Profiles, not actual servers
        "GetComputeServerSettingList": 35,
        "GetBootPrecisionPolicyList": 30,
        
        # Alerts and monitoring
        "GetCondAlarmList": 60,
        "GetCondHclStatusList": 55,
        
        # Storage and network
        "GetStoragePhysicalDiskList": 50,
        "GetNetworkElementList": 50,
        
        # Specialized - rarely what users want
        "GetServerDisruptionList": 10,  # NOT for general server listing
        "GetThermalPolicyList": 15,
        "GetVnicEthQosPolicyList": 15,
        
        # View endpoints - typically lower priority
        "GetViewComputePhysicalSummaryList": 25,
        "GetViewServerList": 25,
    },
    
    "nexus_dashboard": {
        # Fabric and site management
        "getFabrics": 90,
        "getSites": 85,
        "getFabricHealth": 80,
        "getNodes": 75,
        
        # Policy and configuration
        "getPolicies": 60,
        "getTemplates": 55,
        
        # Analytics and insights
        "getAnalytics": 50,
        "getInsights": 50,
    },
    
    "nexus_hyperfabric": {
        # Fabric operations
        "fabricsGetAllFabrics": 95,
        "fabricsGetFabric": 90,
        "nodesGetAllNodes": 85,
        "fabricsGetFabricHealth": 80,
        
        # Configuration
        "policiesGetPolicies": 60,
        "templatesGetTemplates": 55,
    },
    
    "sdwan_mngr": {
        # Device management (most common)
        "listAllDevices": 95,  # Primary device inventory function
        "getAllDeviceStatus": 90,  # Device operational status
        "getDevicesDetails": 85,  # Detailed device information
        "getDevicesHealth": 85,  # Device health metrics
        "getDevicesHealthOverview": 80,  # Health overview
        "getDeviceCounters": 75,
        "getDeviceModels": 70,
        "getControlStatus": 70,
        
        # Alarms and monitoring
        "getRawAlarmData": 85,  # Primary alarm data function
        "getActiveAlarms": 85,  # Active alarms only
        "getNonViewedAlarms": 80,  # Unviewed alarms
        "getAlarmsCount": 70,  # Just counts
        "getRunningAlarmCount": 65,
        
        # Users and AAA
        "findUsers_1": 85,  # Primary user list function
        "getUserRole": 75,
        "getUserGroups": 75,
        "getAaaConfig": 70,
        
        # Templates and configuration
        "getAllDeviceTemplates": 80,  # Device templates
        "getFeatureTemplateList": 75,
        "getTemplatePolicy": 70,
        "getDeviceTemplateList": 70,
        
        # Sites and topology
        "getAllSites": 85,  # Site list
        "getSiteHealth": 80,
        "getTopology": 75,
        "getControlConnections": 70,
        
        # Policies
        "getAllVedgePolicies": 75,  # vEdge policies
        "getPolicyList": 70,
        "getApplicationAwareRoutingPolicyList": 65,
        "getControlPolicyList": 65,
        
        # Lower priority - specialized operations
        "getDeviceRebootHistory": 30,
        "getDeviceRunningConfig": 40,
        "getStatisticsRawData": 35,
        
        # Deprecated or less useful
        "getDevicesList": 20,  # Use listAllDevices instead
    },
    
    "secure_access": {
        # User and authentication
        "getUsers": 90,
        "getGroups": 85,
        "getAuthentications": 80,
        
        # Policy and admin
        "getPolicies": 60,
        "getAdmins": 55,
    },
    
    "umbrella": {
        # Organization and identity
        "getOrganizations": 90,
        "getNetworks": 85,
        "getIdentities": 80,
        
        # Security and reporting
        "getSecurityActivity": 70,
        "getDestinationLists": 65,
        "getReports": 60,
    },
    
    "cloudlock": {
        # Incidents and policies
        "getIncidents": 85,
        "getPolicies": 80,
        "getUsers": 75,
        
        # Data and compliance
        "getDataPatterns": 60,
        "getComplianceScans": 55,
    },
    
    "ai_defense": {
        # Threat detection
        "getThreatDetections": 90,
        "getSecurityAlerts": 85,
        "getIncidentList": 80,
        
        # Analysis and response
        "getAnalysisResults": 70,
        "getResponseActions": 65,
    },
    
    "sdwan_mngr": {
        # Device management (MOST common)
        "listAllDevices": 100,  # PRIMARY device list function
        "getAllDeviceStatus": 95,  # PRIMARY device status
        "getDeviceDetails": 85,
        "getSystemDeviceList": 80,
        
        # Alarms and monitoring
        "getRawAlarmData": 90,
        "getActiveAlarms": 85,
        "getAlarmsCount": 80,
        "getCriticalAlarmsCount": 75,
        
        # Policy management (HIGH priority)
        "getAllVedgePolicies": 90,
        "getSecurityPolicyDeviceList": 85,
        "getApplicationAwareRoutingPolicyList": 80,
        "getControlPolicyList": 80,
        "getDataPolicyList": 80,
        "getTrafficPolicyList": 75,
        
        # Templates
        "getAllDeviceTemplates": 75,
        "getFeatureTemplateList": 70,
        "getTemplatePolicy": 65,
        
        # Sites and topology
        "getAllSites": 70,
        "getTopology": 65,
        
        # Specialized operations (lower priority)
        "getCloudxDeviceList": 30,
        "getMasterOrchestrators": 25,
        "getCloudConnections": 20,
    }
}

# Query pattern to function boost mapping
QUERY_PATTERN_BOOSTS = {
    "list servers": {
        "intersight": {
            "GetComputePhysicalSummaryList": 50,
            "GetComputeRackUnitList": 20,
            "GetComputeBladeList": 20,
            "GetServerDisruptionList": -40,  # Negative boost
            "GetServerProfileList": -20,
        }
    },
    "server inventory": {
        "intersight": {
            "GetComputePhysicalSummaryList": 40,
            "GetComputeRackUnitList": 15,
            "GetComputeBladeList": 15,
        }
    },
    "all devices": {
        "meraki": {
            "getOrganizationDevices": 30,
            "getDevices": 25,
        },
        "catalyst": {
            "getDeviceList": 30,
            "getNetworkDeviceList": 20,
        },
        "sdwan_mngr": {
            "listAllDevices": 40,  # Primary device list
            "getAllDeviceStatus": 30,
            "getDevicesDetails": 25,
            "getDevicesList": -30,  # Discourage less useful variant
        }
    },
    "network health": {
        "catalyst": {
            "getOverallNetworkHealth": 40,
            "getSiteHealth": 20,
            "getDeviceHealthStats": 20,
        },
        "nexus_dashboard": {
            "getFabricHealth": 30,
        }
    },
    "interfaces": {
        "catalyst": {
            "getAllInterfaces": 50,
            "getInterfaces": 30,
        }
    },
    "alerts": {
        "intersight": {
            "GetCondAlarmList": 40,
        },
        "ai_defense": {
            "getSecurityAlerts": 40,
        }
    },
    "alarms": {
        "sdwan_mngr": {
            "getRawAlarmData": 50,  # Primary alarm function
            "getActiveAlarms": 40,
            "getNonViewedAlarms": 30,
            "getAlarmsCount": 20,  # Just count
        }
    },
    "sd-wan devices": {
        "sdwan_mngr": {
            "listAllDevices": 50,
            "getAllDeviceStatus": 40,
            "getDevicesDetails": 35,
            "getDevicesHealth": 30,
        }
    },
    "vmanage devices": {
        "sdwan_mngr": {
            "listAllDevices": 50,
            "getAllDeviceStatus": 40,
            "getDevicesDetails": 35,
        }
    },
    "users": {
        "sdwan_mngr": {
            "findUsers_1": 50,
            "getUserRole": 30,
            "getUserGroups": 30,
        }
    },
    "templates": {
        "sdwan_mngr": {
            "getAllDeviceTemplates": 50,
            "getFeatureTemplateList": 40,
            "getTemplatePolicy": 30,
        }
    },
    "sites": {
        "sdwan_mngr": {
            "getAllSites": 50,
            "getSiteHealth": 40,
        }
    },
    "policies": {
        "sdwan_mngr": {
            "getAllVedgePolicies": 40,
            "getPolicyList": 35,
            "getApplicationAwareRoutingPolicyList": 30,
            "getControlPolicyList": 30,
        }
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# 1.  Pick retriever backend
# ─────────────────────────────────────────────────────────────────────────────
BACKEND = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()

RETRIEVER_MODULES: dict[str, str] = {
    "chroma":  "app.retrievers.chroma_retriever",
    "azure":   "app.retrievers.ai_search_retriever",
    "elastic": "app.retrievers.elastic_retriever",
}
if BACKEND not in RETRIEVER_MODULES:
    raise ValueError(
        f"Unsupported FASTAPI_VECTOR_BACKEND={BACKEND!r}. "
        f"Expected one of: {', '.join(RETRIEVER_MODULES)}"
    )

mod = importlib.import_module(RETRIEVER_MODULES[BACKEND])

# Try the common names first, then fall back to "any *Retriever class"
Retriever = (
    getattr(mod, "FunctionRetriever", None)
    or getattr(mod, "ChromaRetriever", None)
    or getattr(mod, "AzureSearchRetriever", None)
    or getattr(mod, "ElasticRetriever", None)
)

if Retriever is None:
    for attr in dir(mod):
        obj = getattr(mod, attr)
        if inspect.isclass(obj) and attr.endswith("Retriever"):
            Retriever = obj
            break

if Retriever is None:  # still nothing?  bail out clearly.
    raise ImportError(
        f"No retriever class found in module {RETRIEVER_MODULES[BACKEND]}"
    )

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Instantiate a singleton
# ─────────────────────────────────────────────────────────────────────────────
if BACKEND == "chroma":
    retriever = Retriever(
        collection_name=os.getenv(
            "FASTAPI_CHROMA_COLLECTION_PLATFORM",
            "platform-summaries-index",
        )
    )
    # honour dynamic override if the Chroma client exposes helpers
    custom_col = os.getenv(
        "FASTAPI_CHROMA_COLLECTION_PLATFORM",
        "platform-summaries-index",
    )
    if hasattr(retriever, "set_collection"):
        retriever.set_collection(custom_col)
    elif hasattr(retriever, "collection_name"):
        setattr(retriever, "collection_name", custom_col)
else:  # Azure / Elastic (both accept layer kwarg)
    retriever = Retriever(layer="FASTAPI")

# ─────────────────────────────────────────────────────────────────────────────
# 3.  Full-schema KV (lazy build + cache)
# ─────────────────────────────────────────────────────────────────────────────

DYNAMIC_CACHE_ROOT = Path(
    os.getenv(
        "PLATFORM_DYNAMIC_CACHE_PATH",
        # Default: <repo-root>/src/app/llm/platform_dynamic_cache
        (Path(__file__).resolve().parent / "platform_dynamic_cache").as_posix(),
    )
).resolve()
DYNAMIC_CACHE_ROOT.mkdir(parents=True, exist_ok=True)

CACHE_FILE = DYNAMIC_CACHE_ROOT / "full_schemas.json"
SPEC_DIR   = Path(__file__).resolve().parent / "openapi_specs"


def _build_full_kv() -> Dict[str, Any]:
    """Load `openapi_specs/full_*.json` files into a single lookup table."""
    kv: dict[str, Any] = {}
    for fp in SPEC_DIR.glob("full_*.json"):
        platform = fp.stem.replace("full_", "")
        spec     = json.loads(fp.read_text(encoding="utf-8"))
        for path_item in spec.get("paths", {}).values():
            for op in path_item.values():
                op_id = op.get("operationId")
                if op_id:
                    kv[f"{platform}:{op_id}"] = op
    CACHE_FILE.write_text(json.dumps(kv), encoding="utf-8")
    return kv


FULL_KV: Dict[str, Any] = (
    json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    if CACHE_FILE.exists()
    else _build_full_kv()
)

# ─────────────────────────────────────────────────────────────────────────────
# 4.  Priority calculation helpers
# ─────────────────────────────────────────────────────────────────────────────

def extract_query_intent(query: str) -> Tuple[str, Set[str]]:
    """
    Extract the primary intent and relevant terms from a query.
    Returns: (primary_target, query_words_set)
    """
    query_lower = query.lower()
    words = set(query_lower.split())
    
    # Find the primary target (what the user wants)
    primary_target = None
    for target, config in SEMANTIC_MAPPINGS.items():
        if target in query_lower:
            primary_target = target
            break
        # Check if any boost terms are in the query
        for term in config["boost_terms"]:
            if term in query_lower:
                primary_target = target
                break
        if primary_target:
            break
    
    return primary_target, words


def calculate_function_score(
    func_name: str,
    platform: str,
    query: str,
    is_lexical_match: bool = False
) -> float:
    """
    Enhanced semantic scoring that considers the meaning and intent of the query.
    
    Args:
        func_name: Name of the function
        platform: Platform name (e.g., 'intersight', 'meraki')
        query: User's query string
        is_lexical_match: Whether this was a lexical token match
        
    Returns:
        Priority score (higher = more relevant)
    """
    # Base priority from platform configuration
    platform_priorities = FUNCTION_PRIORITIES.get(platform, {})
    base_score = platform_priorities.get(func_name, 50)  # Default priority is 50
    score = base_score
    
    func_name_lower = func_name.lower()
    query_lower = query.lower()
    
    # Extract query intent
    primary_target, query_words = extract_query_intent(query)
    
    # Apply semantic scoring if we identified a target
    if primary_target and primary_target in SEMANTIC_MAPPINGS:
        config = SEMANTIC_MAPPINGS[primary_target]
        
        # Huge boost for primary functions
        if func_name in config["primary_functions"]:
            score += 200
            log.debug(f"Primary function boost for {func_name}: +200")
        
        # Boost for matching semantic terms
        for boost_term in config["boost_terms"]:
            if boost_term in func_name_lower:
                score += 50
                log.debug(f"Semantic term '{boost_term}' found in {func_name}: +50")
        
        # Penalty for avoid terms (unless explicitly requested)
        for avoid_term in config["avoid_terms"]:
            if avoid_term in func_name_lower and avoid_term not in query_lower:
                score -= 30
                log.debug(f"Avoid term '{avoid_term}' found in {func_name}: -30")
    
    # Multi-word matching bonus
    # Count how many query words appear in the function name
    func_words = set(re.findall(r'[a-z]+', func_name_lower))
    common_words = query_words & func_words
    
    # Filter out common words that don't add meaning
    meaningful_words = common_words - {'get', 'list', 'show', 'all', 'the', 'a', 'an', 'of', 'for'}
    if len(meaningful_words) >= 2:
        boost = len(meaningful_words) * 30
        score += boost
        log.debug(f"Multi-word match for {func_name}: +{boost} ({meaningful_words})")
    
    # Lexical match gets moderate boost (reduced from 25)
    if is_lexical_match:
        score += 15
    
    # Apply query pattern boosts (legacy support)
    for pattern, platform_boosts in QUERY_PATTERN_BOOSTS.items():
        if pattern in query_lower and platform in platform_boosts:
            boost = platform_boosts[platform].get(func_name, 0)
            if boost != 0:
                score += boost
                log.debug(f"Query pattern '{pattern}' boost for {func_name}: {boost:+d}")
    
    # Common action words get a small boost
    if any(action in func_name_lower for action in ['get', 'list', 'show']):
        score += 5
    
    # Penalty for specialized/administrative functions
    if any(term in func_name_lower for term in ['debug', 'diagnostic', 'internal', 'test']):
        score -= 20
    
    # Platform-specific semantic adjustments
    if platform == "intersight":
        if primary_target == "servers":
            if "physical" in func_name_lower and "summary" in func_name_lower:
                score += 100  # Extra boost for the primary server function
                log.debug(f"Intersight primary server function boost: +100")
            elif "profile" in func_name_lower and "server" not in query_lower:
                score -= 50  # Penalty for profile functions unless requested
                log.debug(f"Intersight profile penalty: -50")
    
    elif platform == "catalyst":
        if primary_target == "interfaces":
            if func_name == "getAllInterfaces":
                score += 100
                log.debug(f"Catalyst primary interface function boost: +100")
            elif func_name == "getInterfaces":
                score += 50
    
    elif platform == "sdwan_mngr":
        if primary_target == "devices":
            if func_name == "getAllDeviceStatus":
                score += 100
                log.debug(f"SD-WAN primary device function boost: +100")
            elif func_name in ["listAllDevices", "getDevicesList"]:
                score -= 50  # Deprecated/confusing functions
                log.debug(f"SD-WAN deprecated function penalty: -50")
    
    return max(0, score)  # Ensure non-negative score

# ─────────────────────────────────────────────────────────────────────────────
# 5.  Public helpers
# ─────────────────────────────────────────────────────────────────────────────
def build_functions_for_llm(
    query: str,
    enabled: list[str],
    *,
    token_budget: int = int(os.getenv("FASTAPI_FUNCTION_TOKEN_BUDGET", 16_384)),
    k: int = int(os.getenv("FASTAPI_FUNCTION_TOP_K", 50)),
) -> Tuple[List[dict], Dict[str, str]]: # <-- Return a tuple
    """
    Return a list of diet-function JSON objects that the LLM will receive.

    1. Enhanced natural language preprocessing for better semantic matching
    2. Top-k vector search over enabled platforms with multiple query variants
    3. Lexical fallback: include any function whose *name* contains a user token
       (case-insensitive, plural⇢singular).
    4. Priority-based reranking for optimal function selection.
    5. Trim JSON payload to fit within *token_budget*.
    """
    query_lower = query.lower()
    primary_target, query_words = extract_query_intent(query)
    
    # ── 1. Enhanced query preprocessing ────────────────────────────────────
    # Generate multiple search queries based on the natural language input
    enhanced_queries = [query]  # Always include the original
    
    # Check for common natural language patterns
    nl_patterns = {
        "list servers": ["GetComputePhysicalSummaryList", "server inventory", "compute servers"],
        "show servers": ["GetComputePhysicalSummaryList", "server inventory"],
        "get servers": ["GetComputePhysicalSummaryList", "server inventory"],
        "all servers": ["GetComputePhysicalSummaryList", "server inventory"],
        "list devices": ["getDeviceList", "getAllDeviceStatus", "device inventory", "listAllDevices"],
        "show devices": ["getDeviceList", "getAllDeviceStatus", "listAllDevices"],
        "all devices": ["getAllDeviceStatus", "device inventory", "listAllDevices"],
        "sd-wan devices": ["listAllDevices", "getAllDeviceStatus", "getDevicesDetails"],
        "sdwan devices": ["listAllDevices", "getAllDeviceStatus", "getDevicesDetails"],
        "vmanage devices": ["listAllDevices", "getAllDeviceStatus", "getDevicesDetails"],
        "list sd-wan": ["listAllDevices", "getAllDeviceStatus", "getDevicesDetails"],
        "list sdwan": ["listAllDevices", "getAllDeviceStatus", "getDevicesDetails"],
        "list alarms": ["getRawAlarmData", "getActiveAlarms", "getNonViewedAlarms"],
        "show alarms": ["getRawAlarmData", "getActiveAlarms"],
        "sd-wan alarms": ["getRawAlarmData", "getActiveAlarms", "getNonViewedAlarms"],
        "list interfaces": ["getAllInterfaces", "getInterfaces", "interface inventory"],
        "show interfaces": ["getAllInterfaces", "interface inventory"],
        "list users": ["getUsers", "getUserList", "user inventory", "findUsers_1"],
        "sd-wan users": ["findUsers_1", "getUserRole", "getUserGroups"],
        "list alerts": ["GetCondAlarmList", "getSecurityAlerts", "alarm list"],
        "list networks": ["getNetworks", "getNetworkList", "network inventory"],
        "network health": ["getOverallNetworkHealth", "getSiteHealth", "health status"],
        "device health": ["getDeviceHealthStats", "device health status", "getDevicesHealth"],
        "sd-wan templates": ["getAllDeviceTemplates", "getFeatureTemplateList"],
        "list templates": ["getAllDeviceTemplates", "getFeatureTemplateList"],
        "sd-wan sites": ["getAllSites", "getSiteHealth"],
        "list sites": ["getAllSites", "getSiteHealth"],
        "sd-wan policies": ["getAllVedgePolicies", "getPolicyList"],
        "list policies": ["getAllVedgePolicies", "getPolicyList"],
    }
    
    # Find matching patterns and add their expansions
    for pattern, expansions in nl_patterns.items():
        if pattern in query_lower:
            enhanced_queries.extend(expansions)
            log.debug(f"Matched pattern '{pattern}' - adding {len(expansions)} enhanced queries")
    
    # Add semantic target-based queries
    if primary_target and primary_target in SEMANTIC_MAPPINGS:
        mapping = SEMANTIC_MAPPINGS[primary_target]
        # Add primary function names as search terms
        enhanced_queries.extend(mapping["primary_functions"][:3])
        # Add semantic keywords
        enhanced_queries.extend(mapping["boost_terms"][:2])
    
    # Deduplicate while preserving order
    seen = set()
    unique_queries = []
    for q in enhanced_queries:
        if q not in seen:
            seen.add(q)
            unique_queries.append(q)
    enhanced_queries = unique_queries[:10]  # Limit to avoid too many searches
    
    # ── 2. Multi-query vector search ────────────────────────────────────────
    # Aggregate results from all enhanced queries
    all_vec_hits = {}
    hit_scores = {}  # Track best score for each function
    
    for i, search_query in enumerate(enhanced_queries):
        hits = retriever.query(
            search_query,
            k=min(k, 50),  # Limit per query
            filter={"platform": {"$in": enabled}},
        )
        
        for hit in hits:
            # Extract function name from content JSON
            try:
                content = json.loads(hit.get("content", "{}"))
                func_name = content.get("name", "")
            except (json.JSONDecodeError, AttributeError):
                func_name = ""
            
            if not func_name:
                # Fallback to direct name field if available
                func_name = hit.get("name", "")
            
            if func_name:
                # Store the function name in the hit for easier access later
                hit["name"] = func_name
                # Keep the hit with the best (lowest) distance
                current_distance = hit.get("distance", float('inf'))
                if func_name not in all_vec_hits or current_distance < hit_scores.get(func_name, float('inf')):
                    all_vec_hits[func_name] = hit
                    hit_scores[func_name] = current_distance
                    # Boost score if from early enhanced query
                    if i < 3:  # First 3 queries are most relevant
                        hit_scores[func_name] *= 0.8
    
    # Convert back to list
    vec_hits = list(all_vec_hits.values())
    
    # ── 2b. Ensure primary functions are included ─────────────────────────
    # If we detected a semantic target, explicitly search for its primary functions
    if primary_target and primary_target in SEMANTIC_MAPPINGS:
        primary_funcs = SEMANTIC_MAPPINGS[primary_target]["primary_functions"]
        for func_name in primary_funcs:
            # Check if this function is already in our results
            if func_name not in all_vec_hits:
                # Try to find it
                for platform in enabled:
                    extra_hits = retriever.query(
                        func_name,  # Search by exact name
                        k=1,
                        filter={"platform": {"$in": [platform]}},
                    )
                    if extra_hits:
                        # Extract function name from content to verify match
                        try:
                            content = json.loads(extra_hits[0].get("content", "{}"))
                            hit_func_name = content.get("name", "")
                        except (json.JSONDecodeError, AttributeError):
                            hit_func_name = extra_hits[0].get("name", "")
                        
                        if hit_func_name == func_name:
                            # Store the function name in the hit
                            extra_hits[0]["name"] = func_name
                            vec_hits.extend(extra_hits)
                            all_vec_hits[func_name] = extra_hits[0]
                            log.info(f"Added primary function {func_name} for {primary_target} query")
    
    # No forced functions to handle anymore
    
    have: set[str] = {d["name"] for d in vec_hits}

    # ── 2. lexical fallback  ────────────────────────────────────────────
    raw_tokens = [t.lower().strip(".,!?") for t in query.split()]
    tokens: set[str] = set()
    for tok in raw_tokens:
        tokens.add(tok)
        if tok.endswith("s") and len(tok) > 3:
            tokens.add(tok[:-1])  # Singular form

    lex_hits: list[dict] = []
    for platform in enabled:
        every = retriever.query(
            "",                  # empty query returns everything
            k=500,               # Increased to handle large platforms like intersight
            filter={"platform": {"$in": [platform]}},
        )
        for d in every:
            if d["name"] in have:
                continue
            if any(tok in d["name"].lower() for tok in tokens):
                lex_hits.append(d)
                have.add(d["name"])

    # ── 3. Priority-based reranking ─────────────────────────────────────
    all_hits = lex_hits + vec_hits
    
    # Score and sort all candidates
    scored_hits: List[Tuple[float, dict]] = []
    for hit in all_hits:
        platform = hit.get("metadata", {}).get("platform", "")
        func_name = hit["name"]
        is_lexical = hit in lex_hits
        
        score = calculate_function_score(func_name, platform, query, is_lexical)
        scored_hits.append((score, hit))
    
    # Sort by score (highest first)
    scored_hits.sort(key=lambda x: x[0], reverse=True)
    
    if ("server" in query.lower() and "intersight" in enabled) or ("device" in query.lower() and "sdwan_mngr" in enabled):
        print(f"\n=== DEBUG: Query '{query}' ===")
        primary_target, _ = extract_query_intent(query)
        print(f"Detected semantic target: '{primary_target}'")
        print(f"Enabled platforms: {enabled}")
        print("Top 10 functions after scoring:")
        for i, (score, hit) in enumerate(scored_hits[:10]):
            platform = hit.get("metadata", {}).get("platform", hit.get("platform", ""))
            print(f"{i+1}. {hit['name']} ({platform}) (score: {score})")
    # Take top k after scoring
    docs = [hit for score, hit in scored_hits[:k]]

    # ── 4. unwrap + schema enhancement + trimming ─────────────────────────
    size = 0
    out: list[dict] = []
    platform_map: Dict[str, str] = {} 
    for d in docs:
        try:
            # The 'content' field is a JSON string of the core function definition
            fn_schema = json.loads(d["content"])
        except (KeyError, json.JSONDecodeError):
            continue

        # --- CHANGE #3: This logic now correctly populates the platform map ---
        # Get the platform from the top-level dictionary `d` from the retriever
        platform = d.get("platform")
        func_name = fn_schema.get("name")

        # Populate the platform map if we have the necessary info
        if func_name and platform:
            platform_map[func_name] = platform
        # --- END of platform map logic ---

        # Enhance description based on priority (this existing logic is good)
        platform_priorities = FUNCTION_PRIORITIES.get(platform, {})
        priority = platform_priorities.get(func_name, 50)
        
        original_desc = fn_schema.get("description", "")
        if priority >= 90:
            fn_schema["description"] = f"⭐ [PRIMARY] {original_desc}"
        elif priority >= 70:
            fn_schema["description"] = f"[RECOMMENDED] {original_desc}"
        elif priority <= 20:
            fn_schema["description"] = f"[SPECIALIZED] {original_desc}"
        
        # Platform-specific description enhancements
        if platform == "intersight" and func_name == "GetComputePhysicalSummaryList":
            fn_schema["description"] = "⭐ [PRIMARY] Main function to list all servers. Use this for: list servers, show servers, get servers, server inventory."
        elif platform == "catalyst" and func_name == "getAllInterfaces":
            fn_schema["description"] = "⭐ [PRIMARY] Get all network interfaces from all devices. Use this for interface inventory."
        elif platform == "sdwan_mngr" and func_name == "getAllDeviceStatus":
            fn_schema["description"] = "⭐ [PRIMARY] Get complete list and status of all SD-WAN devices."

        # Fix OpenAI array-schema quirk (missing "items")
        for pschema in fn_schema.get("parameters", {}).get("properties", {}).values():
            if pschema.get("type") == "array" and "items" not in pschema:
                pschema["items"] = {"type": "string"}

 

        payload = json.dumps(fn_schema, separators=(",", ":"))
        if size + len(payload) > token_budget:
            break

        size += len(payload)
        out.append(fn_schema)

    # Log function selection for debugging
    if log.isEnabledFor(logging.DEBUG):
        selected_names = [fn["name"] for fn in out[:10]]  # First 10
        log.debug(f"Query: '{query}' -> Selected functions: {selected_names}")

    if "server" in query.lower() and "intersight" in enabled:
        print("\nFunctions being sent to LLM:")
        for i, fn in enumerate(out[:10]):
            print(f"{i+1}. {fn['name']}: {fn.get('description', '')[:80]}...")
        print(f"Total functions sent: {len(out)}\n")

    return out, platform_map

def full_schema_lookup(platform: str, name: str) -> dict | None:
    """Return the full OpenAPI operation object (or `None` if not found)."""
    return FULL_KV.get(f"{platform}:{name}")


# ─────────────────────────────────────────────────────────────────────────────
# 6. Configuration management
# ─────────────────────────────────────────────────────────────────────────────

def load_custom_priorities() -> None:
    """Load custom function priorities from external JSON file if available."""
    priority_file = DYNAMIC_CACHE_ROOT / "function_priorities.json"
    if priority_file.exists():
        try:
            with open(priority_file, 'r') as f:
                custom_priorities = json.load(f)
                # Merge with default priorities (custom takes precedence)
                for platform, priorities in custom_priorities.items():
                    if platform in FUNCTION_PRIORITIES:
                        FUNCTION_PRIORITIES[platform].update(priorities)
                    else:
                        FUNCTION_PRIORITIES[platform] = priorities
                log.info(f"Loaded custom function priorities from {priority_file}")
        except Exception as e:
            log.warning(f"Failed to load custom priorities: {e}")


def export_current_priorities() -> None:
    """Export current function priorities for review/editing."""
    export_file = DYNAMIC_CACHE_ROOT / "function_priorities_export.json"
    with open(export_file, 'w') as f:
        json.dump(FUNCTION_PRIORITIES, f, indent=2, sort_keys=True)
    log.info(f"Exported function priorities to {export_file}")


# Load custom priorities on module import
load_custom_priorities()

# ─────────────────────────────────────────────────────────────────────────────
# 7. Testing and debugging helpers
# ─────────────────────────────────────────────────────────────────────────────

def test_function_selection(query: str, platform: str) -> None:
    """Test function selection for a given query and platform."""
    print(f"\nTesting query: '{query}' for platform: {platform}")
    print("-" * 60)
    
    functions = build_functions_for_llm(query, [platform], k=10)
    
    for i, func in enumerate(functions, 1):
        name = func.get("name", "Unknown")
        desc = func.get("description", "No description")[:100]
        print(f"{i:2d}. {name}")
        print(f"    {desc}...")
    print()


if __name__ == "__main__":
    # Test the function selection
    test_queries = [
        ("list servers", "intersight"),
        ("get all devices", "meraki"),
        ("show interfaces", "catalyst"),
        ("network health", "catalyst"),
        ("get fabrics", "nexus_dashboard"),
    ]
    
    for query, platform in test_queries:
        test_function_selection(query, platform)