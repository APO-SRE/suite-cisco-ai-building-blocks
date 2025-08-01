"""Auto‑generated FastAPI router for *catalyst* (edit me!)."""
from fastapi import APIRouter, HTTPException
from app.llm.unified_service import UnifiedService
from typing import Optional, Dict, Any
import os

router = APIRouter(prefix="/catalyst", tags=["catalyst"])

@router.get("/")
async def catalyst_info():
    """Return basic information about the DNA Center platform."""
    try:
        service = UnifiedService("catalyst")
        # Get system health as a basic info endpoint
        health = service.call("system_health")
        return {
            "platform": "Cisco DNA Center (Catalyst)",
            "status": "connected",
            "base_url": os.getenv("DNACENTER_BASE_URL"),
            "version": os.getenv("DNACENTER_VERSION", "2.3.7.6"),
            "health_summary": {
                "total_events": len(health.get("healthEvents", [])),
                "errors": sum(1 for e in health.get("healthEvents", []) if e.get("severity") == 1),
                "warnings": sum(1 for e in health.get("healthEvents", []) if e.get("severity") == 2),
                "ok": sum(1 for e in health.get("healthEvents", []) if e.get("severity") == 3)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/devices")
async def get_devices():
    """Get list of devices from DNA Center."""
    try:
        service = UnifiedService("catalyst")
        result = service.call("get_device_list")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sites")
async def get_sites():
    """Get list of sites from DNA Center."""
    try:
        service = UnifiedService("catalyst")
        result = service.call("get_site")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def get_health():
    """Get system health from DNA Center."""
    try:
        service = UnifiedService("catalyst")
        result = service.call("system_health")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
