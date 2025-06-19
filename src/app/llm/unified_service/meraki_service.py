# app/llm/unified_service/meraki_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.meraki_client import MerakiClient

class MerakiServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = MerakiClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on MerakiClient"
            )
        return method(**kwargs)