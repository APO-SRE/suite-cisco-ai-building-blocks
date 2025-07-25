#!/usr/bin/env python3
#src/scripts/platform_customizations/__init__.py
"""
Platform customizations package.

This package contains modular configurations for platform-specific behaviors:
- platform_overrides: Platform-specific rules and overrides
- injection_config: Parameter injection configurations
- aliases: Function alias generation logic
"""

from .platform_overrides import PLATFORM_OVERRIDES
from .injection_config import INJECTION_CONFIG
from .aliases import generate_aliases

__all__ = ['PLATFORM_OVERRIDES', 'INJECTION_CONFIG', 'generate_aliases']