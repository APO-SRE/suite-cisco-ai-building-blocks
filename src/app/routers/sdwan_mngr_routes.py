"""Auto‑generated FastAPI router for *sdwan_mngr* (edit me!)."""
from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/sdwan_mngr", tags=["sdwan_mngr"])

@router.get("/")
async def sdwan_mngr_info():
    """Return basic information about the platform."""
    return UnifiedService.sdwan_mngr_info()
