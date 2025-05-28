#!/usr/bin/env python3
from __future__ import annotations
################################################################################
# ai-building-blocks-agent/app/routers/meraki_routes.py
# Copyright (c) 2025 Jeff Teeter, Ph.D.
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
Organizational Meraki endpoints powered by your unified_service layer.
"""
import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.llm.unified_service.meraki_service import MerakiServiceClient

router = APIRouter()

# Pull Meraki API key from env
MERAKI_API_KEY = os.getenv("CISCO_MERAKI_API_KEY", "")


@router.get("/meraki/organizations")
def list_meraki_organizations():
    """
    Return all Meraki organizations.
    """
    if not MERAKI_API_KEY:
        raise HTTPException(status_code=400, detail="CISCO_MERAKI_API_KEY is missing.")

    service = MerakiServiceClient(api_key=MERAKI_API_KEY)
    try:
        organizations = service.call("getOrganizations")
        return JSONResponse(content={"organizations": organizations})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/meraki/organizations/{organization_id}/networks")
def list_meraki_networks(organization_id: str):
    """
    Return all Meraki networks in the given organization.
    """
    if not MERAKI_API_KEY:
        raise HTTPException(status_code=400, detail="CISCO_MERAKI_API_KEY is missing.")

    service = MerakiServiceClient(api_key=MERAKI_API_KEY)
    try:
        networks = service.call("getOrganizationNetworks", organizationId=organization_id)
        return JSONResponse(content={"networks": networks})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/meraki/networks/{network_id}")
def get_meraki_network(network_id: str):
    """
    Return details of a single Meraki network by ID.
    """
    if not MERAKI_API_KEY:
        raise HTTPException(status_code=400, detail="CISCO_MERAKI_API_KEY is missing.")

    service = MerakiServiceClient(api_key=MERAKI_API_KEY)
    try:
        network = service.call("getNetwork", networkId=network_id)
        return JSONResponse(content={"network": network})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
