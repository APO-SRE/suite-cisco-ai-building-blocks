# Auto-generated – DO NOT EDIT
# This file was rebuilt by platform_scaffolder.py

_SERVICE_REGISTRY: dict[str, type] = {}

try:
    from .ai_defense_service import Ai_defenseServiceClient
    _SERVICE_REGISTRY['ai_defense'] = Ai_defenseServiceClient
except ImportError:
    Ai_defenseServiceClient = None

try:
    from .catalyst_service import CatalystServiceClient
    _SERVICE_REGISTRY['catalyst'] = CatalystServiceClient
except ImportError:
    CatalystServiceClient = None

try:
    from .cloudlock_service import CloudlockServiceClient
    _SERVICE_REGISTRY['cloudlock'] = CloudlockServiceClient
except ImportError:
    CloudlockServiceClient = None

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
    from .nexus_dashboard_service import Nexus_dashboardServiceClient
    _SERVICE_REGISTRY['nexus_dashboard'] = Nexus_dashboardServiceClient
except ImportError:
    Nexus_dashboardServiceClient = None

try:
    from .nexus_hyperfabric_service import Nexus_hyperfabricServiceClient
    _SERVICE_REGISTRY['nexus_hyperfabric'] = Nexus_hyperfabricServiceClient
except ImportError:
    Nexus_hyperfabricServiceClient = None

try:
    from .sdwan_mngr_service import Sdwan_mngrServiceClient
    _SERVICE_REGISTRY['sdwan_mngr'] = Sdwan_mngrServiceClient
except ImportError:
    Sdwan_mngrServiceClient = None

try:
    from .secure_access_service import Secure_accessServiceClient
    _SERVICE_REGISTRY['secure_access'] = Secure_accessServiceClient
except ImportError:
    Secure_accessServiceClient = None

try:
    from .umbrella_service import UmbrellaServiceClient
    _SERVICE_REGISTRY['umbrella'] = UmbrellaServiceClient
except ImportError:
    UmbrellaServiceClient = None

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
    'Ai_defenseServiceClient',
    'CatalystServiceClient',
    'CloudlockServiceClient',
    'IntersightServiceClient',
    'MerakiServiceClient',
    'Nexus_dashboardServiceClient',
    'Nexus_hyperfabricServiceClient',
    'Sdwan_mngrServiceClient',
    'Secure_accessServiceClient',
    'UmbrellaServiceClient',
]
