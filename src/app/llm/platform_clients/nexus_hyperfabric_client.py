# app/llm/platform_clients/nexus_hyperfabric_client.py
# Auto‑generated – DO NOT EDIT
import nexus_hyperfabric as _sdk
import os

class Nexus_hyperfabricClient:
    """Thin wrapper around `AuthenticatedClient` with fuzzy attribute lookup."""

    def __init__(self, **kwargs):
        base_url = os.getenv('NEXUS_HYPERFABRIC_BASE_URL')
        token = os.getenv('NEXUS_HYPERFABRIC_BEARER_TOKEN')
        if not base_url or not token:
            raise ValueError('Missing NEXUS_HYPERFABRIC_BASE_URL or NEXUS_HYPERFABRIC_BEARER_TOKEN')
        kwargs.setdefault('base_url', base_url)
        kwargs.setdefault('token', token)

        self._sdk = _sdk.AuthenticatedClient(**kwargs)

    def __getattr__(self, item):
        if hasattr(self._sdk, item):
            return getattr(self._sdk, item)

        for name in dir(self._sdk):
            if name.startswith('_'):
                continue
            sub = getattr(self._sdk, name)
            if hasattr(sub, item):
                return getattr(sub, item)

        raise AttributeError(f"{self.__class__.__name__} has no attribute {item!r}")
