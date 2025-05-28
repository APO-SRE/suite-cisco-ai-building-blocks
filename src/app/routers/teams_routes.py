#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/app/routers/teams_routes.py
## Microsoft Teams integration – Activity-based webhook handler for Bot Framework
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
DISCLAIMER: USE AT YOUR OWN RISK

This module handles incoming Activity payloads from Microsoft Teams via Bot Framework.
It responds using the Bot Framework REST API with a valid bearer token obtained from Azure AD.

******** For notes on how to integraet this code - see suite-cisco-ai-building-blocks/docs/teams_integration.md   ********
"""

import json, logging, os, time, requests
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from opentelemetry import trace
import structlog

log = structlog.get_logger("teams_routes")
tracer = trace.get_tracer("teams_routes")

router = APIRouter(tags=["teams"])

# ──────────────────────────────── Helper: Access token retrieval
def get_botframework_access_token() -> str:
    token_url = f"https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token"
    app_id     = os.getenv("TEAMS_APP_ID")
    app_secret = os.getenv("TEAMS_APP_PASSWORD")

    if not app_id or not app_secret:
        raise RuntimeError("Missing TEAMS_APP_ID or TEAMS_APP_PASSWORD in environment.")

    resp = requests.post(
        token_url,
        data={
            "grant_type": "client_credentials",
            "client_id": app_id,
            "client_secret": app_secret,
            "scope": "https://api.botframework.com/.default"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=10
    )

    if resp.status_code != 200:
        log.error("Failed to get Bot Framework token", status=resp.status_code, text=resp.text)
        raise RuntimeError("Could not obtain Bot Framework token")

    return resp.json().get("access_token")

# ──────────────────────────────── Activity schema (simplified)
class Activity(BaseModel):
    type: str
    id: str | None = None
    text: str | None = None
    conversation: dict
    from_: dict = None  # 'from' is a keyword
    recipient: dict
    replyToId: str | None = None
    serviceUrl: str

# ──────────────────────────────── POST endpoint for Teams webhooks
@router.post("/teams/webhook")
async def teams_webhook(req: Request):
    """
    Handles POSTs from Microsoft Teams via Bot Framework.
    """
    raw = await req.json()
    activity = Activity(**raw)

    log.info("[TEAMS] Received activity", activity=raw)

    # Only handle user-to-bot messages
    if activity.type != "message" or not activity.text:
        return JSONResponse({"status": "ignored"})

    user_text = activity.text.strip()

    # Build reply payload
    bot_reply = {
        "type": "message",
        "text": f"You said: {user_text}"  # Replace with LLM integration if needed
    }

    # Send reply back via Bot Framework
    reply_url = (
        f"{activity.serviceUrl}/v3/conversations/"
        f"{activity.conversation['id']}/activities/"
        f"{activity.replyToId or activity.id}"
    )

    token = get_botframework_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    resp = requests.post(reply_url, headers=headers, json=bot_reply)
    if resp.status_code >= 400:
        log.error("TEAMS reply error", status=resp.status_code, text=resp.text)
        raise HTTPException(status_code=502, detail="Failed to send reply to Teams")

    return JSONResponse({"status": "sent"})
 