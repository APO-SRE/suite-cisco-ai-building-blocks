# app/llm/platform_clients/catalyst_client.py
# Auto-generated – DO NOT EDIT
import dnacentersdk as _sdk

class CatalystClient:
    """Thin wrapper around `DNACenterAPI` with fuzzy attribute lookup."""

    def __init__(self, **kwargs):
        self._sdk = _sdk.DNACenterAPI(**kwargs)

    def __getattr__(self, item):
        # ① direct attribute on DashboardAPI
        if hasattr(self._sdk, item):
            return getattr(self._sdk, item)

        # ② first-level sub-clients (organizations, networks, …)
        for name in dir(self._sdk):
            if name.startswith('_'):
                continue
            sub = getattr(self._sdk, name)
            if hasattr(sub, item):
                return getattr(sub, item)

        raise AttributeError(f"{self.__class__.__name__} has no attribute {item!r}")
