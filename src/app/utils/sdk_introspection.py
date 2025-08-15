#!/usr/bin/env python3
"""
suite-cisco-ai-building-blocks/src/app/utils/sdk_introspection.py
SDK Introspection Module for Multiple Cisco SDKs
Discovers available methods in SDK modules and provides validation
"""
import inspect
import importlib
import os
from typing import Dict, Any, Callable, Optional, Set, List, Tuple
from pathlib import Path
import logging
import re
from dataclasses import dataclass
from enum import Enum

log = logging.getLogger(__name__)


class SDKPattern(Enum):
    """Known SDK patterns for Cisco products"""
    MERAKI = "meraki"  # DashboardAPI with sub-clients
    CATALYST = "catalyst"  # DNACenterAPI or similar
    WEBEX = "webex"  # WebexTeamsAPI pattern
    INTERSIGHT = "intersight"  # Module-based API structure
    NEXUS_DASHBOARD = "nexus_dashboard"  # Nexus Dashboard API
    NEXUS_HYPERFABRIC = "nexus_hyperfabric"  # Nexus HyperFabric API
    SDWAN = "sdwan"  # SD-WAN Manager (vManage) API
    AI_DEFENSE = "ai_defense"  # Cisco AI Defense API
    CLOUDLOCK = "cloudlock"  # Cisco Cloudlock API
    SECURE_ACCESS = "secure_access"  # Cisco Secure Access (formerly Duo)
    UMBRELLA = "umbrella"  # Cisco Umbrella API
    GENERIC = "generic"  # Unknown pattern


@dataclass
class SDKMethod:
    """Represents an SDK method with metadata"""
    name: str
    signature: Optional[inspect.Signature]
    parent_class: str
    sub_client: Optional[str] = None
    operation_id_variants: List[str] = None
    
    def __post_init__(self):
        if self.operation_id_variants is None:
            self.operation_id_variants = self._generate_variants()
    
    def _generate_variants(self) -> List[str]:
        """Generate possible operationId variants for this method"""
        variants = [self.name]
        
        # camelCase to snake_case
        snake = re.sub(r'(?<!^)(?=[A-Z])', '_', self.name).lower()
        if snake != self.name:
            variants.append(snake)
        
        # snake_case to camelCase
        if '_' in self.name:
            camel = ''.join(word.capitalize() if i > 0 else word 
                          for i, word in enumerate(self.name.split('_')))
            variants.append(camel)
        
        # With and without underscores
        no_underscore = self.name.replace('_', '')
        if no_underscore != self.name:
            variants.append(no_underscore)
        
        # All lowercase
        variants.append(self.name.lower())
        
        # If there's a sub_client, add prefixed variants
        if self.sub_client:
            for variant in variants[:]:
                variants.append(f"{self.sub_client}_{variant}")
                variants.append(f"{self.sub_client}{variant.capitalize()}")
        
        return list(set(variants))


class SDKIntrospector:
    """Main introspection class that handles multiple SDK patterns"""
    
    def __init__(self, platform: str, sdk_module_name: str):
        self.platform = platform
        self.sdk_module_name = sdk_module_name
        self.sdk_pattern = self._detect_sdk_pattern()
        self.methods: Dict[str, SDKMethod] = {}
        
    def _detect_sdk_pattern(self) -> SDKPattern:
        """Detect which SDK pattern this module follows"""
        pattern_mapping = {
            'meraki': SDKPattern.MERAKI,
            'dnacentersdk': SDKPattern.CATALYST,
            'catalystwan': SDKPattern.SDWAN,  # Check this before 'catalyst'
            'catalyst': SDKPattern.CATALYST,
            'webexteamssdk': SDKPattern.WEBEX,
            'webex': SDKPattern.WEBEX,
            'intersight': SDKPattern.INTERSIGHT,
            'nexus_dashboard': SDKPattern.NEXUS_DASHBOARD,
            'nexusdashboard': SDKPattern.NEXUS_DASHBOARD,
            'nd_sdk': SDKPattern.NEXUS_DASHBOARD,
            'hyperfabric': SDKPattern.NEXUS_HYPERFABRIC,
            'nexushyperfabric': SDKPattern.NEXUS_HYPERFABRIC,
            'sdwan': SDKPattern.SDWAN,
            'vmanage': SDKPattern.SDWAN,
            'viptela': SDKPattern.SDWAN,
            'ai_defense': SDKPattern.AI_DEFENSE,
            'aidefense': SDKPattern.AI_DEFENSE,
            'cloudlock': SDKPattern.CLOUDLOCK,
            'secure_access': SDKPattern.SECURE_ACCESS,
            'duo': SDKPattern.SECURE_ACCESS,
            'umbrella': SDKPattern.UMBRELLA,
            'opendns': SDKPattern.UMBRELLA,
        }
        
        module_lower = self.sdk_module_name.lower()
        for key, pattern in pattern_mapping.items():
            if key in module_lower:
                return pattern
        
        return SDKPattern.GENERIC
    
    def discover_methods(self) -> Dict[str, SDKMethod]:
        """Main method to discover all SDK methods"""
        try:
            sdk_module = importlib.import_module(self.sdk_module_name)
            
            if self.sdk_pattern == SDKPattern.MERAKI:
                self._discover_meraki_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.CATALYST:
                self._discover_catalyst_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.WEBEX:
                self._discover_webex_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.INTERSIGHT:
                self._discover_intersight_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.NEXUS_DASHBOARD:
                self._discover_nexus_dashboard_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.NEXUS_HYPERFABRIC:
                self._discover_nexus_hyperfabric_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.SDWAN:
                self._discover_sdwan_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.AI_DEFENSE:
                self._discover_ai_defense_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.CLOUDLOCK:
                self._discover_cloudlock_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.SECURE_ACCESS:
                self._discover_secure_access_methods(sdk_module)
            elif self.sdk_pattern == SDKPattern.UMBRELLA:
                self._discover_umbrella_methods(sdk_module)
            else:
                self._discover_generic_methods(sdk_module)
            
            log.info(f"Discovered {len(self.methods)} methods for {self.platform}")
            return self.methods
            
        except ImportError as e:
            log.error(f"Failed to import SDK module {self.sdk_module_name}: {e}")
            return {}
    
    def _discover_meraki_methods(self, sdk_module):
        """Discover methods for Meraki SDK pattern (DashboardAPI with sub-clients)"""
        # Find the main API class (usually DashboardAPI)
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if 'API' in name and not name.startswith('_'):
                log.info(f"Found Meraki API class: {name}")
                
                # Try to instantiate with dummy key to discover structure
                try:
                    # Meraki SDK typically needs an API key
                    dummy_instance = obj('dummy_key')
                    
                    # Iterate through attributes that are sub-clients
                    for attr_name in dir(dummy_instance):
                        if not attr_name.startswith('_'):
                            attr = getattr(dummy_instance, attr_name)
                            
                            # Check if this is a sub-client
                            if hasattr(attr, '__class__') and not callable(attr):
                                sub_client_name = attr_name
                                
                                # Get methods from sub-client
                                for method_name in dir(attr):
                                    if not method_name.startswith('_'):
                                        method = getattr(attr, method_name)
                                        if callable(method):
                                            try:
                                                sig = inspect.signature(method)
                                                sdk_method = SDKMethod(
                                                    name=method_name,
                                                    signature=sig,
                                                    parent_class=name,
                                                    sub_client=sub_client_name
                                                )
                                                self.methods[method_name] = sdk_method
                                            except (ValueError, TypeError):
                                                continue
                except Exception as e:
                    log.warning(f"Could not instantiate {name} for deeper inspection: {e}")
                    # Fall back to static inspection
                    self._static_inspection(obj, name)
    
    def _discover_catalyst_methods(self, sdk_module):
        """Discover methods for Catalyst Center SDK pattern"""
        # Similar to Meraki but might have different instantiation
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if 'API' in name and not name.startswith('_'):
                log.info(f"Found Catalyst API class: {name}")
                
                try:
                    # Catalyst might need different params
                    dummy_instance = obj(base_url='https://dummy', username='dummy', password='dummy')
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    # Try alternative instantiation
                    try:
                        dummy_instance = obj()
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _discover_webex_methods(self, sdk_module):
        """Discover methods for Webex SDK pattern"""
        # Webex typically uses WebexTeamsAPI or similar
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if 'API' in name and not name.startswith('_'):
                log.info(f"Found Webex API class: {name}")
                
                try:
                    # Webex needs access token
                    dummy_instance = obj(access_token='dummy_token')
                    self._introspect_instance(dummy_instance, name)
                except Exception as e:
                    log.warning(f"Could not instantiate {name}: {e}")
                    self._static_inspection(obj, name)
    
    def _discover_intersight_methods(self, sdk_module):
        """Discover methods for Intersight SDK pattern (module-based)"""
        # Intersight uses apis module (with 's') that imports all API classes
        apis_found = False
        
        # First try the apis module (recommended approach)
        try:
            from intersight import apis
            apis_found = True
            log.info("Using intersight.apis module for introspection")
            
            # Get all API classes from the apis module
            for api_class_name in dir(apis):
                if api_class_name.endswith('Api') and not api_class_name.startswith('_'):
                    try:
                        api_class = getattr(apis, api_class_name)
                        if inspect.isclass(api_class):
                            log.info(f"Found Intersight API class: {api_class_name}")
                            
                            # Extract the API category from class name (e.g., ComputeApi -> compute)
                            api_category = api_class_name[:-3].lower()  # Remove 'Api' suffix
                            
                            # Get methods from the API class
                            for method_name, method in inspect.getmembers(api_class):
                                if callable(method) and not method_name.startswith('_'):
                                    try:
                                        sig = inspect.signature(method)
                                        sdk_method = SDKMethod(
                                            name=method_name,
                                            signature=sig,
                                            parent_class=api_class_name,
                                            sub_client=api_category
                                        )
                                        self.methods[method_name] = sdk_method
                                    except (ValueError, TypeError):
                                        continue
                    except Exception as e:
                        log.debug(f"Error introspecting {api_class_name}: {e}")
        except ImportError:
            log.warning("Could not import intersight.apis module")
        
        # If apis module not found, try the api module approach
        if not apis_found and hasattr(sdk_module, 'api'):
            log.info("Falling back to intersight.api module for introspection")
            api_module = getattr(sdk_module, 'api')
            
            # This would require loading individual API files
            api_path = os.path.dirname(api_module.__file__)
            for filename in os.listdir(api_path):
                if filename.endswith('_api.py') and not filename.startswith('_'):
                    module_name = filename[:-3]  # Remove .py
                    try:
                        # Dynamically import the API module
                        api_submodule = importlib.import_module(f'intersight.api.{module_name}')
                        
                        # Find API classes in the submodule
                        for class_name, class_obj in inspect.getmembers(api_submodule, inspect.isclass):
                            if class_name.endswith('Api'):
                                log.info(f"Found Intersight API class: {class_name}")
                                
                                # Get methods from the API class
                                for method_name, method in inspect.getmembers(class_obj):
                                    if callable(method) and not method_name.startswith('_'):
                                        try:
                                            sig = inspect.signature(method)
                                            sdk_method = SDKMethod(
                                                name=method_name,
                                                signature=sig,
                                                parent_class=class_name,
                                                sub_client=module_name.replace('_api', '')
                                            )
                                            self.methods[method_name] = sdk_method
                                        except (ValueError, TypeError):
                                            continue
                    except Exception as e:
                        log.debug(f"Error introspecting {module_name}: {e}")
    
    def _discover_generic_methods(self, sdk_module):
        """Generic discovery for unknown SDK patterns"""
        for name, obj in inspect.getmembers(sdk_module):
            if inspect.isclass(obj) and not name.startswith('_'):
                log.info(f"Found class: {name}")
                self._static_inspection(obj, name)
    
    def _discover_nexus_dashboard_methods(self, sdk_module):
        """Discover methods for Nexus Dashboard SDK"""
        # Nexus Dashboard typically uses session-based authentication
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if any(keyword in name.lower() for keyword in ['client', 'api', 'session', 'nexus']):
                log.info(f"Found Nexus Dashboard API class: {name}")
                
                try:
                    # Try common instantiation patterns
                    dummy_instance = obj(host='dummy.com', username='admin', password='pass')
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    try:
                        dummy_instance = obj(base_url='https://dummy.com', api_key='dummy')
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _discover_nexus_hyperfabric_methods(self, sdk_module):
        """Discover methods for Nexus HyperFabric SDK"""
        # Similar to Nexus Dashboard but might have fabric-specific patterns
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if any(keyword in name.lower() for keyword in ['fabric', 'hyperfabric', 'api', 'client']):
                log.info(f"Found Nexus HyperFabric API class: {name}")
                
                try:
                    # HyperFabric might need fabric credentials
                    dummy_instance = obj(fabric_url='https://dummy.com', api_token='dummy')
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    try:
                        dummy_instance = obj()
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _discover_sdwan_methods(self, sdk_module):
        """Discover methods for SD-WAN Manager (vManage) SDK using catalystwan"""
        try:
            import catalystwan.api as api_module
            import pkgutil
            import importlib
            
            log.info("Using catalystwan SDK pattern for SD-WAN discovery")
            
            # Iterate through all API submodules
            for importer, modname, ispkg in pkgutil.iter_modules(api_module.__path__):
                if modname in ['api_container', 'versions_utils']:  # Skip non-API modules
                    continue
                    
                try:
                    # Import the API module
                    full_module_name = f'catalystwan.api.{modname}'
                    api_submodule = importlib.import_module(full_module_name)
                    
                    # Find API classes in the module
                    for class_name, class_obj in inspect.getmembers(api_submodule, inspect.isclass):
                        # Skip imported classes and base classes
                        if (class_obj.__module__ != full_module_name or 
                            class_name.startswith('_') or
                            class_name in ['ABC', 'BaseModel']):
                            continue
                            
                        log.info(f"Found SD-WAN API class: {class_name} in {modname}")
                        
                        # Introspect methods from the API class
                        for method_name, method in inspect.getmembers(class_obj):
                            if (method_name.startswith('_') or 
                                not callable(method) or 
                                isinstance(method, type)):
                                continue
                                
                            try:
                                sig = inspect.signature(method)
                                # Skip if it's a property or classmethod
                                if any(param.name == 'cls' for param in sig.parameters.values()):
                                    continue
                                    
                                sdk_method = SDKMethod(
                                    name=method_name,
                                    signature=sig,
                                    parent_class=class_name,
                                    sub_client=modname.replace('_api', '')
                                )
                                self.methods[method_name] = sdk_method
                                
                                # Also add camelCase variant for better matching
                                camel_case_name = self._to_camel_case(method_name)
                                if camel_case_name != method_name:
                                    self.methods[camel_case_name] = sdk_method
                                    
                                # For SD-WAN, also try to match OpenAPI operation IDs
                                # which often have patterns like getAllDeviceStatus
                                if method_name.startswith('get_'):
                                    # get_all_device_status -> getAllDeviceStatus
                                    parts = method_name.split('_')
                                    if len(parts) > 1:
                                        open_api_style = parts[0] + ''.join(p.title() for p in parts[1:])
                                        self.methods[open_api_style] = sdk_method
                                        
                            except (ValueError, TypeError) as e:
                                log.debug(f"Could not get signature for {class_name}.{method_name}: {e}")
                                
                except Exception as e:
                    log.debug(f"Error importing/introspecting {modname}: {e}")
                    
        except ImportError as e:
            log.warning(f"Could not import catalystwan.api: {e}")
            # Fall back to generic discovery
            self._discover_generic_methods(sdk_module)
    
    def _discover_ai_defense_methods(self, sdk_module):
        """Discover methods for Cisco AI Defense SDK"""
        # AI Defense might use API key or OAuth patterns
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if any(keyword in name.lower() for keyword in ['aidefense', 'defense', 'api', 'client']):
                log.info(f"Found AI Defense API class: {name}")
                
                try:
                    # Try API key pattern
                    dummy_instance = obj(api_key='dummy_key', region='us')
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    try:
                        # Try OAuth pattern
                        dummy_instance = obj(client_id='dummy', client_secret='dummy')
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _discover_cloudlock_methods(self, sdk_module):
        """Discover methods for Cisco Cloudlock SDK"""
        # Cloudlock uses REST API with token authentication
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if any(keyword in name.lower() for keyword in ['cloudlock', 'api', 'client']):
                log.info(f"Found Cloudlock API class: {name}")
                
                try:
                    # Cloudlock typically uses API tokens
                    dummy_instance = obj(api_token='dummy_token', base_url='https://api.cloudlock.com')
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    try:
                        dummy_instance = obj(token='dummy_token')
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _discover_secure_access_methods(self, sdk_module):
        """Discover methods for Cisco Secure Access (Duo) SDK"""
        # Secure Access/Duo uses API with integration key and secret
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if any(keyword in name.lower() for keyword in ['duo', 'secure', 'access', 'api', 'client']):
                log.info(f"Found Secure Access API class: {name}")
                
                try:
                    # Duo pattern
                    dummy_instance = obj(
                        ikey='dummy_integration_key',
                        skey='dummy_secret_key',
                        host='api-dummy.duosecurity.com'
                    )
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    try:
                        # Alternative pattern
                        dummy_instance = obj(api_host='dummy.com', api_key='dummy')
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _discover_umbrella_methods(self, sdk_module):
        """Discover methods for Cisco Umbrella SDK"""
        # Umbrella uses different APIs (Reporting, Management, etc.)
        for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
            if any(keyword in name.lower() for keyword in ['umbrella', 'opendns', 'api', 'client']):
                log.info(f"Found Umbrella API class: {name}")
                
                try:
                    # Umbrella typically uses API key and secret
                    dummy_instance = obj(
                        key='dummy_key',
                        secret='dummy_secret',
                        base_url='https://api.umbrella.com'
                    )
                    self._introspect_instance(dummy_instance, name)
                except Exception:
                    try:
                        # Management API pattern
                        dummy_instance = obj(api_key='dummy_key', org_id='dummy_org')
                        self._introspect_instance(dummy_instance, name)
                    except Exception as e:
                        log.warning(f"Could not instantiate {name}: {e}")
                        self._static_inspection(obj, name)
    
    def _introspect_instance(self, instance, parent_class: str):
        """Introspect an instantiated SDK client"""
        # Direct methods
        for name in dir(instance):
            if not name.startswith('_'):
                attr = getattr(instance, name)
                if callable(attr):
                    try:
                        sig = inspect.signature(attr)
                        sdk_method = SDKMethod(
                            name=name,
                            signature=sig,
                            parent_class=parent_class
                        )
                        self.methods[name] = sdk_method
                    except (ValueError, TypeError):
                        continue
                elif hasattr(attr, '__class__'):
                    # Potential sub-client
                    sub_client_name = name
                    for sub_name in dir(attr):
                        if not sub_name.startswith('_'):
                            sub_attr = getattr(attr, sub_name)
                            if callable(sub_attr):
                                try:
                                    sig = inspect.signature(sub_attr)
                                    sdk_method = SDKMethod(
                                        name=sub_name,
                                        signature=sig,
                                        parent_class=parent_class,
                                        sub_client=sub_client_name
                                    )
                                    self.methods[sub_name] = sdk_method
                                except (ValueError, TypeError):
                                    continue
    
    def _static_inspection(self, class_obj, class_name: str):
        """Static inspection when instantiation fails"""
        for method_name, method in inspect.getmembers(class_obj):
            if callable(method) and not method_name.startswith('_'):
                try:
                    sig = inspect.signature(method)
                    sdk_method = SDKMethod(
                        name=method_name,
                        signature=sig,
                        parent_class=class_name
                    )
                    self.methods[method_name] = sdk_method
                except (ValueError, TypeError):
                    continue
    
    def _to_camel_case(self, snake_str: str) -> str:
        """Convert snake_case to camelCase"""
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])


class SDKOpenAPIFilter:
    """Filters OpenAPI specs based on SDK availability"""
    
    def __init__(self, introspector: SDKIntrospector):
        self.introspector = introspector
        self.methods = introspector.discover_methods()
        self._build_operation_id_map()
    
    def _build_operation_id_map(self):
        """Build a map of all possible operationId variants to SDK methods"""
        self.operation_id_map = {}
        
        for method_name, sdk_method in self.methods.items():
            for variant in sdk_method.operation_id_variants:
                self.operation_id_map[variant] = sdk_method
    
    def filter_openapi_spec(self, openapi_spec: dict) -> Tuple[dict, Dict[str, str]]:
        """
        Filter OpenAPI spec to only include operations available in SDK.
        
        Returns:
            Tuple of (filtered_spec, operation_id_to_sdk_method_map)
        """
        import copy
        
        filtered_spec = copy.deepcopy(openapi_spec)
        operation_mapping = {}
        paths_to_remove = []
        
        for path, path_item in filtered_spec.get('paths', {}).items():
            methods_to_remove = []
            
            for method, operation in path_item.items():
                if method in ['parameters', 'servers', 'summary', 'description']:
                    continue
                
                operation_id = operation.get('operationId')
                if not operation_id:
                    continue
                
                # Check if operation is available
                sdk_method = self.operation_id_map.get(operation_id)
                if not sdk_method:
                    # Try lowercase
                    sdk_method = self.operation_id_map.get(operation_id.lower())
                
                if sdk_method:
                    operation_mapping[operation_id] = sdk_method.name
                    log.debug(f"Mapped {operation_id} -> {sdk_method.name}")
                else:
                    methods_to_remove.append(method)
                    log.info(f"Removing operation not in SDK: {operation_id}")
            
            # Remove methods not available in SDK
            for method in methods_to_remove:
                del path_item[method]
            
            # If no methods left for this path, mark for removal
            if not any(m in path_item for m in ['get', 'post', 'put', 'patch', 'delete']):
                paths_to_remove.append(path)
        
        # Remove empty paths
        for path in paths_to_remove:
            del filtered_spec['paths'][path]
        
        return filtered_spec, operation_mapping
    
    def generate_coverage_report(self, openapi_spec: dict) -> dict:
        """Generate a coverage report comparing OpenAPI spec to SDK"""
        total_operations = 0
        covered_operations = 0
        missing_operations = []
        http_method_breakdown = {}
        
        for path, path_item in openapi_spec.get('paths', {}).items():
            for method, operation in path_item.items():
                if method in ['parameters', 'servers', 'summary', 'description']:
                    continue
                
                operation_id = operation.get('operationId')
                if not operation_id:
                    continue
                
                total_operations += 1
                
                # Count HTTP methods
                method_upper = method.upper()
                if method_upper in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
                    http_method_breakdown[method_upper] = http_method_breakdown.get(method_upper, 0) + 1
                
                if (operation_id in self.operation_id_map or 
                    operation_id.lower() in self.operation_id_map):
                    covered_operations += 1
                else:
                    missing_operations.append({
                        'operationId': operation_id,
                        'path': path,
                        'method': method,
                        'summary': operation.get('summary', '')
                    })
        
        coverage_percentage = (covered_operations / total_operations * 100) if total_operations > 0 else 0
        
        return {
            'platform': self.introspector.platform,
            'sdk_module': self.introspector.sdk_module_name,
            'total_operations': total_operations,
            'covered_operations': covered_operations,
            'coverage_percentage': coverage_percentage,
            'missing_operations': missing_operations,
            'sdk_methods_count': len(self.methods),
            'http_method_breakdown': http_method_breakdown
        }


# Convenience functions for backwards compatibility
def discover_sdk_methods(sdk_module) -> Dict[str, inspect.Signature]:
    """Legacy function for compatibility"""
    introspector = SDKIntrospector('generic', sdk_module.__name__)
    methods = introspector.discover_methods()
    return {name: method.signature for name, method in methods.items() if method.signature}


def filter_openapi_by_sdk(openapi_spec: dict, sdk_methods: Set[str]) -> dict:
    """Legacy function for compatibility"""
    # Convert set to proper introspector format
    class MockIntrospector:
        def __init__(self, methods):
            self.methods = {name: SDKMethod(name, None, 'Unknown') for name in methods}
        
        def discover_methods(self):
            return self.methods
    
    mock = MockIntrospector(sdk_methods)
    filter_obj = SDKOpenAPIFilter(mock)
    filtered_spec, _ = filter_obj.filter_openapi_spec(openapi_spec)
    return filtered_spec


# Example usage
if __name__ == "__main__":
    # Example for Meraki
    introspector = SDKIntrospector('meraki', 'meraki')
    meraki_methods = introspector.discover_methods()
    
    # Load OpenAPI spec
    # with open('meraki_openapi.json', 'r') as f:
    #     openapi_spec = json.load(f)
    
    # filter_obj = SDKOpenAPIFilter(introspector)
    # filtered_spec, mapping = filter_obj.filter_openapi_spec(openapi_spec)
    # coverage = filter_obj.generate_coverage_report(openapi_spec)
    
    # print(f"Coverage: {coverage['coverage_percentage']:.2f}%")
    # print(f"Missing operations: {len(coverage['missing_operations'])}")