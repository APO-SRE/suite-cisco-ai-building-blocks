from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/nexus_hyperfabric", tags=["nexus_hyperfabric"])

@router.get("/")
async def get_nexus_hyperfabric_info():
    return UnifiedService.nexus_hyperfabric_info()
