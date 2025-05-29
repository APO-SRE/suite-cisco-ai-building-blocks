
#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/routers/spaces_routes.py
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
import os
from fastapi import APIRouter


router = APIRouter()

# Read the API key from the environment variable (adjust if needed).
# If your Spaces token is actually in "CISCO_SPACES_TOKEN", update accordingly.
SPACES_TOKEN = os.getenv("CISCO_SPACES_API_KEY", "")

@router.get("/devices")
async def get_spaces_devices():
    """
    GET /spaces/devices

    Returns a list of active devices from Cisco Spaces.
    """
    service = CiscoUnifiedService(spaces_token=SPACES_TOKEN)
    devices = service.get_spaces_active_devices()
    return devices

@router.get("/floor/{floor_id}")
async def get_spaces_floor_details(floor_id: str):
    """
    GET /spaces/floor/{floor_id}

    Returns floor details for a specific floor from Cisco Spaces.
    """
    service = CiscoUnifiedService(spaces_token=SPACES_TOKEN)
    floor_details = service.get_spaces_floor_details(floor_id)
    return floor_details