#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/routers/chat_routes.py
## Unified – with full Structured-Logging + OpenTelemetry tracing
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
import json
import inspect 
import logging
import os
import re
import requests
import time
from contextlib import contextmanager
from typing import Any, Dict, List, Sequence

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, Response
from opentelemetry import trace
from opentelemetry.trace import Tracer
import structlog
from pydantic import BaseModel
from app.utils.paths import REPO_ROOT
from datetime import datetime, date, time
from enum import Enum
from decimal import Decimal

from app.config import cfg
from app.llm.llm_factory import get_llm, LLMClientBase
from app.llm.utils import enabled_platforms
from app.llm.dynamic import build_functions_for_llm
from app.llm.function_dispatcher import dispatch_function_call
from app.llm.prompt_templates import (
    BASE_SYSTEM_PROMPT_DOCS_ONLY,
    BASE_SYSTEM_PROMPT_EVENT,
    BASE_SYSTEM_PROMPT_LOB as BASE_SYSTEM_PROMPT_DOMAIN,
    USER_PROMPT_TEMPLATE,
    FUNCTIONS_LLM_PROMPT,
    GENERIC_RESPONSE_PROMPT,
    HTML_SDWAN_DEVICE_STATUS_PROMPT
)
from app.retrievers.chroma_retriever import FunctionRetriever
from app.routers._domain_keywords import DOMAIN_KEYWORDS_MAP
from app.main import request_latency  # prometheus histogram
from app.user_commands.update_platform_registry import load_registry
LLM_DIR = REPO_ROOT / "src" / "app" / "llm"
# ──────────────────────────────── env / logging / tracing
load_dotenv()
registry = load_registry()



structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
)
log = structlog.get_logger("chat_routes")
tracer: Tracer = trace.get_tracer("chat_routes")

TIMING = os.getenv("DEBUG_TIMING", "false").lower() == "true"
VECTOR_BACKEND = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()
try:
    with open(LLM_DIR / "platform_hints.json", 'r') as f:
        platform_hints = json.load(f)
    log.info("✅ Loaded platform hints.")
except (FileNotFoundError, json.JSONDecodeError) as e:
    log.warning(f"⚠️ Platform hints file not found or invalid, hint filter will be disabled: {e}")
    platform_hints = {} #

    
# ──────────────────────────────── helper timer ctx mgr
@contextmanager
def timer(label: str):
    t0 = time.perf_counter()
    yield
    if TIMING:
        log.debug("timing", phase=label, sec=round(time.perf_counter() - t0, 3))

# ──────────────────────────────── message-assembly helpers

def _assemble_docs_messages(user_input: str, docs: Sequence[Dict[str, Any]], *, general: bool) -> List[Dict[str, str]]:
    if docs and not general:
        docs_str = "\n\n".join(d.get("content", "") for d in docs)
        sys_prompt = f"{BASE_SYSTEM_PROMPT_DOCS_ONLY}\n\nDocuments:\n{docs_str}"
    else:
        sys_prompt = BASE_SYSTEM_PROMPT_DOCS_ONLY
    user_prompt = USER_PROMPT_TEMPLATE.format(user_query=user_input)
    return [
        {"role": "system", "content": sys_prompt},
        {"role": "user",   "content": user_prompt},
    ]

# Turn this off to disable keyword-based platform narrowing
PLATFORM_HINT_FILTER = os.getenv("ENABLE_PLATFORM_HINT_FILTER", "true").lower() == "true"




def _assemble_event_messages(user_input: str, docs: Sequence[Dict[str, Any]]) -> List[Dict[str, str]]:
    chunks: list[str] = []
    for d in docs:
        txt = d.get("content", "")
        if add := d.get("additional_info"):
            txt += "\n\nAdditional Info:\n" + json.dumps(add, indent=2)
        chunks.append(txt)
    sys_prompt = f"{BASE_SYSTEM_PROMPT_EVENT}\n\nEvent Docs:\n" + "\n\n".join(chunks)
    user_prompt = USER_PROMPT_TEMPLATE.format(user_query=user_input)
    return [
        {"role": "system", "content": sys_prompt},
        {"role": "user",   "content": user_prompt},
    ]

def _assemble_domain_messages(user_input: str, docs: Sequence[Dict[str, Any]]) -> List[Dict[str, str]]:
    chunks: list[str] = []
    for d in docs:
        txt = d.get("content", "")
        if meta := d.get("metadata"):
            txt += "\n\nMetadata:\n" + json.dumps(meta)
        chunks.append(txt)
    sys_prompt = f"{BASE_SYSTEM_PROMPT_DOMAIN}\n\nDomain Docs:\n" + "\n\n".join(chunks)
    user_prompt = USER_PROMPT_TEMPLATE.format(user_query=user_input)
    return [
        {"role": "system", "content": sys_prompt},
        {"role": "user",   "content": user_prompt},
    ]

# ──────────────────────────────── Pydantic models
class ChatRequest(BaseModel):
    message: str
    domain_index: str | None = None

# ──────────────────────────────── globals
func_retriever = FunctionRetriever(collection_name="function-definitions-index")
# disabled so can do platform filtering in the retriever
#platforms = enabled_platforms() 
router = APIRouter(tags=["chat"])

# ──────────────────────────────── Webex webhook endpoint
@router.post("/webex/webhook")
async def webex_webhook(req: Request):
    """
    1) Extract message ID and room ID
    2) Fetch full message text
    3) Ignore messages sent by this bot (loop-prevention)
    4) Delegate into `handle_chat` for retrieval + function dispatch
    5) Post the result back to Webex
    """
    payload = await req.json()
    log.info("[WEBEX] Received payload", payload=payload)

    #1️⃣ Extract IDs
    try:
        message_id = payload["data"]["id"]
        room_id    = payload["data"]["roomId"]
    except KeyError:
        raise HTTPException(400, "Invalid Webex payload")

    # 2️⃣ Fetch message text
    webex_token = os.getenv("WEBEX_BOT_TOKEN")
    if not webex_token:
        raise HTTPException(500, "Missing WEBEX_BOT_TOKEN")

    msg_resp = requests.get(
        f"https://webexapis.com/v1/messages/{message_id}",
        headers={"Authorization": f"Bearer {webex_token}"}
    )
    if msg_resp.status_code != 200:
        raise HTTPException(400, f"Failed to fetch message: {msg_resp.status_code}")

    msg_json     = msg_resp.json()
    user_query   = msg_json.get("text", "").strip()
    sender_email = msg_json.get("personEmail", "").lower()

    # 3️⃣ Loop-prevention: fetch actual bot email
    me_resp = requests.get(
        "https://webexapis.com/v1/people/me",
        headers={"Authorization": f"Bearer {webex_token}"}
    )
    if me_resp.status_code == 200:
        bot_email = me_resp.json().get("emails", [""])[0].lower()
    else:
        bot_email = os.getenv("WEBEX_BOT_EMAIL", "").lower()

    if sender_email == bot_email:
        log.info("Ignored self-triggered message from bot")
        return JSONResponse({"status": "ignored"})

    # 4️⃣ Delegate under a single span
    chat_req = ChatRequest(message=user_query)
    with tracer.start_as_current_span("chat-workflow"):
        result = await handle_chat(chat_req, req)

    answer = result.get("response", "")

    # 5️⃣ Post reply to Webex
    post_resp = requests.post(
        "https://webexapis.com/v1/messages",
        headers={
            "Authorization": f"Bearer {webex_token}",
            "Content-Type":  "application/json"
        },
        json={"roomId": room_id, "markdown": answer}
    )
    try:
        post_resp.raise_for_status()
    except Exception:
        log.error("Webex API error", status=post_resp.status_code, text=post_resp.text)
        raise HTTPException(502, "Failed to deliver message to Webex")

    return JSONResponse({"status": "sent"})

def summarize_api_data(data: Any, max_items: int = 50, platform: str = None, function_name: str = None) -> str:
    """
    Intelligently summarizes raw API data to create a concise payload for the LLM,
    preventing performance bottlenecks with large responses.
    
    Platform-aware summarization:
    - SD-WAN: Preserves more detail for device/alarm operations
    - Other platforms: Standard summarization
    
    Controlled by LLM2_SUMMARIZER environment variable:
    - "false" or "0": Disable summarization, return full data
    - numeric value (e.g., "50"): Use as max_items
    - "true" or unset: Use default max_items with platform-aware logic
    """
    # Check LLM2_SUMMARIZER environment variable
    summarizer_config = os.getenv("LLM2_SUMMARIZER", "true").lower()
    
    # Disable summarization if set to false or 0
    if summarizer_config in ["false", "0", "no", "disable", "disabled"]:
        if data is None:
            return "The API call returned no data (None)."
        serialised_data = to_serialisable(data)
        return json.dumps(serialised_data, indent=2)
    
    # Check if it's a numeric value to use as max_items override
    if summarizer_config.isdigit():
        max_items = int(summarizer_config)
    
    if data is None:
        return "The API call returned no data (None)."

    # Platform-specific handling for SD-WAN
    if platform == "sdwan_mngr":
        # Critical operations that need full data
        if function_name in ["getRawAlarmData", "getActiveAlarms", "getNonViewedAlarms", 
                             "listAllDevices", "getAllDeviceStatus", "getDevicesDetails",
                             "getDevices", "getDeviceListAsKeyValue"]:
            max_items = 100  # Show more items for these critical operations
        # For alarm operations specifically, try to show all alarms
        elif "alarm" in function_name.lower():
            max_items = 200
        # For user/admin operations, show reasonable amount
        elif function_name in ["findUsers_1", "getAAAUsers", "getUserGroups"]:
            max_items = 50
        
    # Use the existing to_serialisable function to handle complex objects
    serialised_data = to_serialisable(data)

    if not isinstance(serialised_data, list):
        # If it's not a list (e.g., a single dictionary), convert to string
        return json.dumps(serialised_data, indent=2)

    total_items = len(serialised_data)
    if total_items == 0:
        return "The API call returned an empty list."
    
    # For SD-WAN operations, provide smart summaries
    if platform == "sdwan_mngr" and total_items > max_items:
        # Device-specific summary
        if "device" in function_name.lower() or function_name in ["listAllDevices", "getAllDeviceStatus"]:
            device_summary = []
            for device in serialised_data[:max_items]:
                if isinstance(device, dict):
                    # Extract key fields that vary based on the operation
                    summary_item = {}
                    # Common device identifiers
                    for field in ["host-name", "hostname", "deviceId", "uuid", "system-ip", "systemIP"]:
                        if field in device:
                            summary_item[field] = device[field]
                    # Status fields
                    for field in ["reachability", "status", "state", "device-state"]:
                        if field in device:
                            summary_item[field] = device[field]
                    # Additional useful fields
                    for field in ["device-model", "deviceModel", "version", "site-id"]:
                        if field in device:
                            summary_item[field] = device[field]
                    
                    if summary_item:  # Only add if we extracted some data
                        device_summary.append(summary_item)
                    else:  # Fallback to full device data if no known fields
                        device_summary.append(device)
            
            return (
                f"The API call returned {total_items} devices. "
                f"Showing details for the first {len(device_summary)}:\n\n"
                f"{json.dumps(device_summary, indent=2)}"
            )
        
        # Alarm-specific summary
        elif "alarm" in function_name.lower():
            alarm_summary = []
            for alarm in serialised_data[:max_items]:
                if isinstance(alarm, dict):
                    # Include all alarm data as it's critical
                    alarm_summary.append(alarm)
            
            return (
                f"The API call returned {total_items} alarms. "
                f"Showing all details for the first {len(alarm_summary)}:\n\n"
                f"{json.dumps(alarm_summary, indent=2)}"
            )
    
    if total_items <= max_items:
        # If the list is small enough, return it as is
        return json.dumps(serialised_data, indent=2)

    # Default truncation for other cases
    summary_message = (
        f"The API call returned {total_items} items. "
        f"Showing the first {max_items} for detailed analysis."
    )
    truncated_data = serialised_data[:max_items]
    
    return f"{summary_message}\n\n{json.dumps(truncated_data, indent=2)}"

# ---------------------------------------------------------------------------
# Utility – convert SDK objects (attrs classes) into plain JSON‑serialisable
# structures before we pass them to json.dumps().
# ---------------------------------------------------------------------------
def to_serialisable(obj):
    # ➡ 1) short-circuit None → JSON null
    if obj is None:
        return None
    
    # ➡ 2) primitives that JSON can’t handle natively
    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, Decimal):
        return float(obj)

    # ➡ 3) Handle catalystwan SDK objects and other custom classes
    # The catalystwan objects often have a .data attribute or can be cast to a dict.
    # We also keep the original .to_dict() for other SDKs.
    if hasattr(obj, 'data') and isinstance(obj.data, dict):
        # This handles many catalystwan objects which store their payload in a .data dict
        return to_serialisable(obj.data)
    
    to_dict = getattr(obj, "to_dict", None)
    if callable(to_dict):
        try:
            return to_serialisable(to_dict())
        except Exception:
            pass # Fall through if .to_dict() fails

    # This is a robust way to handle Pydantic models (v1 and v2)
    model_dump = getattr(obj, "model_dump", None)
    if callable(model_dump):
        try:
            return model_dump() # model_dump already returns a serializable dict
        except Exception:
            pass # Fall through
            
    # As a last resort for custom objects, try converting its __dict__
    if hasattr(obj, '__dict__'):
        # This will convert an arbitrary class instance to a dict,
        # excluding private/magic methods.
        return {
            k: to_serialisable(v)
            for k, v in obj.__dict__.items()
            if not k.startswith('_')
        }

    # ➡ 4) containers
    if isinstance(obj, (list, tuple, set)):
        return [to_serialisable(x) for x in obj]
    if isinstance(obj, dict):
        return {k: to_serialisable(v) for k, v in obj.items()}

    # ➡ 5) anything else (str, int, bool, etc.) is JSON-ready
    return obj
 

# ──────────────────────────────── Shared business logic
async def handle_chat(req: ChatRequest, request: Request) -> Dict[str, Any]:
    prompt = req.message
    messages: list[dict] = []
    llm: LLMClientBase = get_llm()

    # 1️⃣ Retrieve docs or domain/event data
    with tracer.start_as_current_span("retriever") as rspan:
        if hasattr(request.app.state, "retriever"):
            retriever = request.app.state.retriever
        else:
            from app.retrievers.null_retriever import NullRetriever
            retriever = NullRetriever()

        lower      = prompt.lower()
        # ── DETECT EXPLICIT PLATFORM NAME IN PROMPT ────────────────────────────────────
        if PLATFORM_HINT_FILTER:
            hinted = []
            # Iterate through the hints loaded from platform_hints.json
            for platform_key, aliases in platform_hints.items():
                # Check if this platform is actually installed and enabled
                if not registry.get(platform_key, {}).get("installed", False):
                    continue
                
                # Check if any of the platform's aliases are in the user's query
                if any(alias in lower for alias in aliases):
                    hinted.append(platform_key)
            if hinted:
                # narrow to only the platforms explicitly named
                platforms = hinted
            else:
                # fall back to whatever’s enabled in .env
                platforms = enabled_platforms()
        else:
            platforms = enabled_platforms()
        is_event   = "event" in lower
        domain_idx = (req.domain_index or getattr(retriever, "domain_index", "")).lower()
        is_domain  = domain_idx in DOMAIN_KEYWORDS_MAP and any(
            kw in lower for kw in DOMAIN_KEYWORDS_MAP[domain_idx]
        )

        if is_event and hasattr(retriever, "retrieve_event_info"):
            docs     = retriever.retrieve_event_info(prompt)
            messages = _assemble_event_messages(prompt, docs)
            rspan.set_attribute("type", "event")

        elif is_domain and hasattr(retriever, "retrieve_domain_info"):
            docs     = retriever.retrieve_domain_info(prompt)
            messages = _assemble_domain_messages(prompt, docs)
            rspan.set_attribute("type", "domain")

        else:
            docs = retriever.retrieve_domain_info(prompt)
            messages = [
                {"role": "system", "content": BASE_SYSTEM_PROMPT_DOCS_ONLY},
                {"role": "user",   "content": USER_PROMPT_TEMPLATE.format(user_query=prompt)},
            ]
            rspan.set_attribute("type", "general")

        rspan.set_attribute("docs", len(docs))

    # 2️⃣ Build candidate functions
    with tracer.start_as_current_span("build.functions") as bfspan:
        # This line should unpack the tuple
        functions, platform_map = build_functions_for_llm(prompt, platforms)
         
        
        # Set span attributes for observability
        bfspan.set_attribute("functions.count", len(functions))
        bfspan.set_attribute("platforms", platforms)
        
        # DEBUG: Log which functions were selected for the LLM
        print(f"\n📋 FUNCTIONS PRESENTED TO LLM (top 10):")
        for i, func in enumerate(functions[:10]):
            func_name = func.get("name", "unknown")
            func_platform = func.get("metadata", {}).get("platform", "unknown")
            func_desc = func.get("description", "")[:50] + "..." if len(func.get("description", "")) > 50 else func.get("description", "")
            print(f"   {i+1}. {func_name} ({func_platform}) - {func_desc}")
        if len(functions) > 10:
            print(f"   ... and {len(functions) - 10} more functions")
        print()
  
      

    # 3️⃣ First LLM call
    with tracer.start_as_current_span("llm#1") as l1span:
        try:
            if functions:
                messages[0]["content"] = FUNCTIONS_LLM_PROMPT
                llm_resp = await llm.chat(
                    messages, functions=functions, function_call="auto"
                )
            else:
                llm_resp = await llm.chat(messages)

            if isinstance(llm_resp, str):
                llm_resp = {"content": llm_resp}

        except Exception as exc:
            log.exception("llm_error", exc=str(exc))
            raise HTTPException(status_code=500, detail=f"LLM backend failure: {exc}")

        fc = llm_resp.get("function_call") or {}
        if not fc and isinstance(llm_resp.get("content"), str):
            try:
                candidate = json.loads(llm_resp["content"])
                if "name" in candidate and "arguments" in candidate:
                    fc = candidate
                    log.debug("☞ recovered function_call from content", name=fc["name"])
            except Exception:
                pass

        l1span.set_attribute("llm.choices", len(llm_resp.get("choices", [])))

    # 4️⃣ If no function_call → return text
    if not fc:
        return {"role": "assistant", "label": "Cisco AI", "response": llm_resp.get("content", "I don't know.")}

    # normalize function name + args
    fname = fc["name"].removeprefix("functions.")
    fargs = fc.get("arguments", {})
    if isinstance(fargs, str):
        fargs = json.loads(fargs)
    
    # DEBUG: Log which function the LLM selected
    log.info(f"🎯 LLM selected function: {fname}")
    log.info(f"   Arguments: {json.dumps(fargs, indent=2)}")
    
    # Also print to console for visibility
    print(f"\n🎯 LLM FUNCTION SELECTION:")
    print(f"   Function: {fname}")
    print(f"   Arguments: {json.dumps(fargs, indent=2)}")
    
    # Find which platform this function belongs to
    selected_platform = None
    for func in functions:
        if func.get("name") == fname:
            selected_platform = func.get("metadata", {}).get("platform", "unknown")
            break
    print(f"   Platform: {selected_platform}\n")

    # ------------------------------------------------------------------
    # PATCH: if the target function expects a 'body' argument but the
    #        LLM omitted it, wrap all non‑path/query fields into 'body'.
    # ------------------------------------------------------------------
    try:
        from app.llm.function_dispatcher import _registry as _FUNC_REG
        target_fn = _FUNC_REG.get(fname)
    except Exception:
        target_fn = None

    if target_fn:
        sig = inspect.signature(target_fn)
        if "body" in sig.parameters and "body" not in fargs:
            other_params = {
                p for p in sig.parameters
                if p not in {"body", "kwargs", "self"}
            }
            body_payload = {k: v for k, v in fargs.items() if k not in other_params}
            for k in body_payload:           # strip wrapped keys
                fargs.pop(k, None)
            if body_payload:                 # only inject if something to wrap
                fargs["body"] = body_payload
                log.debug(
                    "🩹 auto‑wrapped args into 'body' for %s → keys=%s",
                    fname, list(body_payload)
                )


    # 5️⃣ dispatch + SDK
    with tracer.start_as_current_span(f"dispatch.{fname}") as dspan:
        try:
            result = dispatch_function_call(fname, fargs)
            
            # DEBUG: Log the result
            print(f"\n📊 SDK CALL RESULT:")
            print(f"   Result type: {type(result)}")
            if result is None:
                print(f"   Result is None!")
            elif isinstance(result, dict):
                print(f"   Result keys: {list(result.keys())[:10]}")
                if 'error' in result:
                    print(f"   Error: {result['error']}")
            elif isinstance(result, list):
                print(f"   Result length: {len(result)}")
                if result:
                    print(f"   First item type: {type(result[0])}")
            else:
                print(f"   Result preview: {str(result)[:200]}")
            print()
            
        except Exception as exc:
            log.exception("dispatcher_error", name=fname, err=str(exc))
            msg = str(exc)
            if "Meraki API services are available" in msg:
                user_msg = (
                    "It looks like your Meraki organization does not have valid licenses "
                    "to use the Meraki API. Please check your license status or contact Meraki support."
                )
            else:
                user_msg = f"Sorry, I couldn't complete '{fname}': {msg}"
            return {"role": "assistant", "label": "Cisco AI", "response": user_msg}

        dspan.set_attribute("function.name", fname)
        dspan.set_attribute("result.size", len(str(result)))

    # 6️⃣ Second LLM call to turn JSON → NL answer
    with tracer.start_as_current_span("llm#2") as l2span:
        if isinstance(fc.get("arguments"), dict):
            fc["arguments"] = json.dumps(fc["arguments"])

        # Determine which platform this function belongs to by looking at the
        # original list of functions retrieved from the vector store.
        function_platform = platform_map.get(fname)
        
        summarized_content = summarize_api_data(
            result, 
            platform=function_platform,
            function_name=fname
        )

        follow_up = [
            *messages,
            {"role": "assistant", "content": None, "function_call": fc},
            {
                "role": "function",
                "name": fname,
                "content": summarized_content,  
            },
        ]

         # Select the system prompt based on the platform.
        if function_platform == 'sdwan_mngr':
            # Use the specific, detailed prompt for any SD-WAN function.
            system_prompt = HTML_SDWAN_DEVICE_STATUS_PROMPT
            log.info("Using SD-WAN specific response prompt.")
        else:
            # For all other platforms, use the improved generic prompt.
            system_prompt = GENERIC_RESPONSE_PROMPT
            log.info(f"Using generic response prompt for platform: {function_platform or 'unknown'}.")

        # Instruct the model using the selected prompt.
        follow_up[0]["content"] = system_prompt
        print("\n" + "="*50)
        print("  FINAL PAYLOAD BEING SENT TO LLM  ")
        print("="*50)
        # Use json.dumps for pretty printing the complex structure
        print(json.dumps(follow_up, indent=2))
        print("="*50 + "\n")
        final = await llm.chat(follow_up)

    if isinstance(final, str):
        final = {"content": final}
    l2span.set_attribute("llm.final_length", len(final.get("content", "")))

    return {
        "role": "assistant",
        "label": "Cisco AI",
        "response": final.get("content")
            or json.dumps(to_serialisable(result), indent=2),
     }



# ──────────────────────────────── HTTP‐only wrapper
@router.post("")
@router.post("/", include_in_schema=False)
async def chat_endpoint(req: ChatRequest, request: Request):
    """
    Single endpoint: turns a user prompt into an answer or function call
    by delegating to the shared `handle_chat` workflow under a single span.
    """
    with request_latency.time():
        with tracer.start_as_current_span("chat-workflow"):
            return await handle_chat(req, request)


# ── Helper: Cisco Spaces floor-plan ─────────────────────────────────────────
"""
def _handle_floor_plan():
    tenant_id = "15650"
    image_path = (
        "mapservices/floor/..."
    )
    from cisco_integrations.cisco_spaces_client import CiscoSpacesClient
    client = CiscoSpacesClient()
    res = client.get_floor_image(tenant_id, image_path, "png", save_local=True, local_filename="floor.png")
    if isinstance(res, dict) and "error" in res:
        return JSONResponse({"role": "assistant", "label": "Cisco AI", "response": f"Error: {res['error']}"})
    return JSONResponse({"role": "assistant", "label": "Cisco AI", "response": "Floor plan downloaded."})
"""