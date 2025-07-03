"""Auto‑generated FastAPI router for *intersight* (edit me!)."""
from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/intersight", tags=["intersight"])

@router.get("/")
async def intersight_info():
    """Return basic information about the platform."""
    return UnifiedService.intersight_info()
