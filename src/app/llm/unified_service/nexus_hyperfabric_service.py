# app/llm/unified_service/nexus_hyperfabric_service.py

# Auto-generated – DO NOT EDIT
from app.llm.platform_clients.nexus_hyperfabric_client import Nexus_hyperfabricClient

class Nexus_hyperfabricServiceClient:
    """Generic call-through service used by FastAPI.""" 

    def __init__(self, **sdk_kwargs):
        self.client = Nexus_hyperfabricClient(**sdk_kwargs)

    def call(self, function_name: str, **kwargs):
        try:
            method = getattr(self.client, function_name)
        except AttributeError:
            raise ValueError(
                f"No such method '{function_name}' on Nexus_hyperfabricClient"
            )
        return method(**kwargs)