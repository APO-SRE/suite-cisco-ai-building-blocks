# app/llm/unified_service/sdwan_mngr_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.sdwan_mngr_client import Sdwan_mngrClient

class Sdwan_mngrServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = Sdwan_mngrClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on Sdwan_mngrClient"
            )
        return method(**kwargs)