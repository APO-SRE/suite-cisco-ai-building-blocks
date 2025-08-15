"""
Platform customizations for the scaffolder.
"""

from .platform_overrides import PLATFORM_OVERRIDES
from .injection_config import INJECTION_CONFIG
from .aliases import generate_aliases

__all__ = [
    'PLATFORM_OVERRIDES',
    'INJECTION_CONFIG', 
    'generate_aliases',
]