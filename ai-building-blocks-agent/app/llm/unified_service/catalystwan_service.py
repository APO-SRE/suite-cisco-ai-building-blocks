# app/llm/unified_service/catalystwan_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.catalystwan_client import CatalystwanClient

class CatalystwanServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = CatalystwanClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on CatalystwanClient"
            )
        return method(**kwargs)