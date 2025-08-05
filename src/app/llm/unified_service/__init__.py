# Auto-generated – DO NOT EDIT
from __future__ import annotations
import sys


_SERVICE_REGISTRY = {

}

class UnifiedService:  # pylint: disable=too-few-public-methods
    """Return the correct *ServiceClient for *platform*."""
    def __new__(cls, platform: str, *args, **kwargs):  # noqa: D401
        try:
            impl = _SERVICE_REGISTRY[platform.lower()]
        except KeyError as exc:  # pragma: no cover
            raise ValueError(
                f"Unsupported platform '{platform}'. "
                f"Valid options: {', '.join(_SERVICE_REGISTRY)}"
            ) from exc
        return impl(*args, **kwargs)

__all__ = ['UnifiedService']

# optional top-level alias
sys.modules.setdefault("unified_service", sys.modules[__name__])
