from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/intersight", tags=["intersight"])

@router.get("/")
async def get_intersight_info():
    return UnifiedService.intersight_info()
