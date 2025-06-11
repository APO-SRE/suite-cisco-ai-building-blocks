#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/routers/catalyst_routes.py
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
import os
from fastapi import APIRouter, FastAPI # type: ignore
from app.llm.unified_service.catalyst_service import CatalystServiceClient

router = APIRouter()

# Read environment variables for Catalyst Center
CATALYST_USERNAME = os.getenv("CISCO_CATALYST_USERNAME", "")
CATALYST_PASSWORD = os.getenv("CISCO_CATALYST_PASSWORD", "")
CATALYST_URL = os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443")
CATALYST_VERSION = os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6")

@router.get("/devices")
async def get_catalyst_devices():
    svc = CatalystServiceClient(
        catalyst_username=CATALYST_USERNAME,
        catalyst_password=CATALYST_PASSWORD,
        catalyst_url=CATALYST_URL,
        catalyst_version=CATALYST_VERSION
    )
    data = svc.get_all_catalyst_devices()
    return data

@router.get("/devices/{device_id}")
async def get_catalyst_device_by_id(device_id: str):
    """
    GET /catalyst/devices/{device_id}

    Returns details for a single device, by device_id in Catalyst Center (DNA Center).
    """
    svc = CatalystServiceClient(
        catalyst_username=CATALYST_USERNAME,
        catalyst_password=CATALYST_PASSWORD,
        catalyst_url=CATALYST_URL,
        catalyst_version=CATALYST_VERSION
    )
    data = service.get_catalyst_device_by_id(device_id)
    return data
