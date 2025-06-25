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
)
from app.retrievers.chroma_retriever import FunctionRetriever
from app.routers._domain_keywords import DOMAIN_KEYWORDS_MAP
from app.main import request_latency  # prometheus histogram

# ──────────────────────────────── env / logging / tracing
load_dotenv()
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
platforms = enabled_platforms()
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

# ---------------------------------------------------------------------------
# Utility – convert SDK objects (attrs classes) into plain JSON‑serialisable
# structures before we pass them to json.dumps().
# ---------------------------------------------------------------------------
def to_serialisable(obj):
    if hasattr(obj, "to_dict"):            # openapi‑python‑client models
        return obj.to_dict()
    if isinstance(obj, (list, tuple, set)):
        return [to_serialisable(x) for x in obj]
    if isinstance(obj, dict):
        return {k: to_serialisable(v) for k, v in obj.items()}
    return obj                             # primitives stay unchanged


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
        functions: List[dict] = []
        if VECTOR_BACKEND == "chroma":
            raw_hits = func_retriever.query(prompt, k=500, filter={"platform": {"$in": platforms}})
            hits     = sorted(raw_hits, key=lambda x: x.get("distance", 1.0))[:128]
            for h in hits:
                try:
                    schema = json.loads(h["content"])
                    # ─── ensure array parameters have an 'items' definition ────────────────
                    for prop in schema.get("parameters", {}).get("properties", {}).values():
                        if prop.get("type") == "array" and "items" not in prop:
                            prop["items"] = {"type": "string"}
                    # ─── (leave the rest of your sanitize code here as before) ─────────────
                    functions.append(schema)
                    '''
                    schema = json.loads(h["content"])
                    for ps in schema.get("parameters", {}).get("properties", {}).values():
                        if ps.get("type") == "array" and "items" not in ps:
                            ps["items"] = {"type": "string"}
                    functions.append(schema) '''
                except Exception as exc:
                    log.warning("bad_schema", name=h.get("name"), err=str(exc))
        else:
            functions = build_functions_for_llm(prompt, platforms)
      

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
    fname = fc["name"].removeprefix("functions.")
    fargs = fc.get("arguments", {})
    if isinstance(fargs, str):
        fargs = json.loads(fargs)

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

        follow_up = [
            *messages,
            {"role": "assistant", "content": None, "function_call": fc},
            {
                "role": "function",
                "name": fname,
                "content": json.dumps(to_serialisable(result)),
            },
        ]
        follow_up[0]["content"] = (
            "You are a helpful Cisco AI assistant. "
            "Use the data returned by the function to answer the user's question "
            "in plain language. Do **NOT** output JSON."
        )
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