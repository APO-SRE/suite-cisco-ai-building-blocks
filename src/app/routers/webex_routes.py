
#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/app/routers/webex_routes.py
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

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging
import os

# Import the unified service that encapsulates Webex functionality.
 

# Create a router instance for Webex endpoints.
router = APIRouter()

@router.get("/webex/meetings")
def get_webex_meetings():
    """
    Retrieve a list of Webex meetings.
    This stub endpoint uses the unified service to obtain a response.
    """
    try:
        service = CiscoUnifiedService(
            catalyst_username=os.getenv("CISCO_CATALYST_USERNAME", ""),
            catalyst_password=os.getenv("CISCO_CATALYST_PASSWORD", ""),
            catalyst_url=os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443"),
            catalyst_version=os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6"),
            meraki_api_key=os.getenv("CISCO_MERAKI_API_KEY", ""),
            spaces_token=os.getenv("CISCO_SPACES_API_KEY", ""),
            webex_token=os.getenv("CISCO_WEBEX_TOKEN", "")
        )
        # Call the stub method for Webex meetings.
        result = service.get_webex_meetings()
        return JSONResponse(content={"webex_meetings": result})
    except Exception as e:
        logging.error(f"Error retrieving Webex meetings: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webex/meetings/{meeting_id}")
def get_webex_meeting_by_id(meeting_id: str):
    """
    Retrieve details of a specific Webex meeting by its meeting ID.
    """
    try:
        service = CiscoUnifiedService(
            catalyst_username=os.getenv("CISCO_CATALYST_USERNAME", ""),
            catalyst_password=os.getenv("CISCO_CATALYST_PASSWORD", ""),
            catalyst_url=os.getenv("CISCO_CATALYST_URL", "https://sandboxdnac.cisco.com:443"),
            catalyst_version=os.getenv("CISCO_CATALYST_VERSION", "2.3.7.6"),
            meraki_api_key=os.getenv("CISCO_MERAKI_API_KEY", ""),
            spaces_token=os.getenv("CISCO_SPACES_API_KEY", ""),
            webex_token=os.getenv("CISCO_WEBEX_TOKEN", "")
        )
        result = service.get_webex_meeting_by_id(meeting_id)
        return JSONResponse(content={"webex_meeting": result})
    except Exception as e:
        logging.error(f"Error retrieving Webex meeting with ID {meeting_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))