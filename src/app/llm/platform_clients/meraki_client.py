# app/llm/platform_clients/meraki_client.py
# Auto‑generated – DO NOT EDIT
import meraki as _sdk
import os

class MerakiClient:
    """Thin wrapper around `DashboardAPI` with fuzzy attribute lookup."""

    def __init__(self, **kwargs):
        api_key = os.getenv('CISCO_MERAKI_API_KEY')
        if not api_key:
            raise ValueError('Missing CISCO_MERAKI_API_KEY environment variable')
        kwargs['api_key'] = api_key
        
        self._sdk = _sdk.DashboardAPI(**kwargs)

    def _inject_org_id(self, func_name: str, kwargs: dict) -> dict:
        """If the method looks org‑scoped and organisation ID is missing, inject it."""
        org_keys = {'organizationId', 'organization_id'}
        if 'organization' in func_name.lower() and not any(k in kwargs for k in org_keys):
            org_id = os.getenv('MERAKI_ORG_ID')
            if org_id:
                kwargs['organizationId'] = org_id
        return kwargs

    def __getattr__(self, item):
        def _wrapper(*args, **kwargs):
            kwargs = self._inject_org_id(item, kwargs)

            # ① direct attribute
            if hasattr(self._sdk, item):
                return getattr(self._sdk, item)(*args, **kwargs)

            # ② sub‑clients
            for name in dir(self._sdk):
                if name.startswith('_'):
                    continue
                sub = getattr(self._sdk, name)
                if hasattr(sub, item):
                    return getattr(sub, item)(*args, **kwargs)

            raise AttributeError(f"{self.__class__.__name__} has no attribute {item!r}")
        return _wrapper
