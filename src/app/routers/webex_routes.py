#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/routers/webex_routes.py
## Copyright (c) 2025 Jeff Teeter
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

from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

# Create a router instance for Webex endpoints, following the standard pattern.
# This file's primary purpose is to be discovered by main.py so the platform
# is recognized as "active". The actual tool calls are handled by the
# function dispatcher in chat_routes.py.
router = APIRouter(prefix="/webex", tags=["webex"])

@router.get("/")
async def webex_info():
    """
    Returns basic information about the Webex platform integration.
    """
    # Note: We do not need to instantiate the service here. The UnifiedService
    # is called automatically by the dispatcher when a Webex tool is used.
    # This endpoint simply confirms the router is active.
    return {
        "platform": "webex",
        "status": "active",
        "description": "Provides tool-calling capabilities for the Webex API."
    }