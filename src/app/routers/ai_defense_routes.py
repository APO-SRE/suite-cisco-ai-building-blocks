from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="/ai_defense", tags=["ai_defense"])

@router.get("/")
async def get_ai_defense_info():
    return UnifiedService.ai_defense_info()
