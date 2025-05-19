import importlib
import inspect
#suite-cisco-ai-building-blocks/ai-building-blocks-agent/scripts/utils/sdk_loader.py

def load_client(module_name: str):
    """
    Dynamically load the *dashboard* client (Meraki) or any class whose name
    ends with 'DashboardAPI' or 'Client'.
    """
    mod = importlib.import_module(module_name)
    for attr in dir(mod):
        candidate = getattr(mod, attr)
        if inspect.isclass(candidate) and (
            attr.lower().endswith("dashboardapi") or attr.lower().endswith("client")
        ):
            return candidate
    raise RuntimeError(f"No SDK client found in {module_name}")
