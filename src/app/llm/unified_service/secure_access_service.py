# app/llm/unified_service/secure_access_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.secure_access_client import Secure_accessClient

class Secure_accessServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = Secure_accessClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on Secure_accessClient"
            )
        return method(**kwargs)