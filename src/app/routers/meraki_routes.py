"""Auto‑generated FastAPI router for *meraki* (edit me!)."""
from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/meraki", tags=["meraki"])

@router.get("/")
async def meraki_info():
    """Return basic information about the platform."""
    return UnifiedService.meraki_info()
