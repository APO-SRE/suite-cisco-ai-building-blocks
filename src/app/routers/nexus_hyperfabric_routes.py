"""Auto‑generated FastAPI router for *nexus_hyperfabric* (edit me!)."""
from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/nexus_hyperfabric", tags=["nexus_hyperfabric"])

@router.get("/")
async def nexus_hyperfabric_info():
    """Return basic information about the platform."""
    return UnifiedService.nexus_hyperfabric_info()
