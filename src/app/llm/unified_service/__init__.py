# Auto-generated – DO NOT EDIT
# This file was rebuilt by platform_scaffolder.py

_SERVICE_REGISTRY: dict[str, type] = {}

try:
    from .intersight_service import IntersightServiceClient
    _SERVICE_REGISTRY['intersight'] = IntersightServiceClient
except ImportError:
    IntersightServiceClient = None

class UnifiedService:
    """Return the correct ServiceClient for a given platform"""

    def __new__(cls, platform: str, *args, **kwargs):
        try:
            impl = _SERVICE_REGISTRY[platform.lower()]
        except KeyError as exc:
            valid = ', '.join(_SERVICE_REGISTRY.keys())
            raise ValueError(
                f"Unsupported platform '{platform}'. Valid options: {valid}"
            ) from exc
        return impl(*args, **kwargs)

__all__ = ['UnifiedService',
    'IntersightServiceClient',
]
