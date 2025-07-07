# Auto-generated – DO NOT EDIT
# This file was rebuilt by platform_scaffolder.py

_SERVICE_REGISTRY: dict[str, type] = {}

try:
    from .catalyst_service import CatalystServiceClient
    _SERVICE_REGISTRY['catalyst'] = CatalystServiceClient
except ImportError:
    CatalystServiceClient = None

try:
    from .intersight_service import IntersightServiceClient
    _SERVICE_REGISTRY['intersight'] = IntersightServiceClient
except ImportError:
    IntersightServiceClient = None

try:
    from .meraki_service import MerakiServiceClient
    _SERVICE_REGISTRY['meraki'] = MerakiServiceClient
except ImportError:
    MerakiServiceClient = None

try:
    from .nexus_hyperfabric_service import Nexus_hyperfabricServiceClient
    _SERVICE_REGISTRY['nexus_hyperfabric'] = Nexus_hyperfabricServiceClient
except ImportError:
    Nexus_hyperfabricServiceClient = None

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
    'CatalystServiceClient',
    'IntersightServiceClient',
    'MerakiServiceClient',
    'Nexus_hyperfabricServiceClient',
]
