# app/llm/unified_service/cloudlock_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.cloudlock_client import CloudlockClient

class CloudlockServiceClient:
    """Generic call-through service used by FastAPI."""

    def __init__(self, **sdk_kwargs):
        self.client = CloudlockClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on CloudlockClient"
            )
        return method(**kwargs)