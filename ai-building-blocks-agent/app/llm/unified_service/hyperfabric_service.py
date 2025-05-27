# app/llm/unified_service/hyperfabric_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.hyperfabric_client import HyperfabricClient

class HyperfabricServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = HyperfabricClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on HyperfabricClient"
            )
        return method(**kwargs)