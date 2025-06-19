"""Auto‑generated FastAPI router for *catalyst* (edit me!)."""
from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/catalyst", tags=["catalyst"])

@router.get("/")
async def catalyst_info():
    """Return basic information about the platform."""
    return UnifiedService.catalyst_info()
