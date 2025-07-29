# app/llm/unified_service/ai_defense_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.ai_defense_client import Ai_defenseClient

class Ai_defenseServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = Ai_defenseClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on Ai_defenseClient"
            )
        return method(**kwargs)