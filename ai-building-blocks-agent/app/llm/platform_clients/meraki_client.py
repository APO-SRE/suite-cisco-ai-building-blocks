import meraki as _sdk
import os

class MerakiClient:
    """Thin wrapper around `DashboardAPI` with fuzzy attribute lookup."""

    def __init__(self, **kwargs):
        api_key = os.getenv('CISCO_MERAKI_API_KEY')
        if not api_key:
            raise ValueError('Missing CISCO_MERAKI_API_KEY environment variable')
        # always use the right key
        kwargs['api_key'] = api_key

        # ─── Disable the SDK’s file & console logging ───────────────────────────
        # no meraki_api_log_*.log files
        kwargs.setdefault('output_log', False)
        # no console spamming
        kwargs.setdefault('print_console', False)
        # completely mute any SDK logger handlers
        kwargs.setdefault('suppress_logging', True)
        # ────────────────────────────────────────────────────────────────────────

        self._sdk = _sdk.DashboardAPI(**kwargs)

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
