"""
Unified service generation for the platform scaffolder.
"""

import logging
from pathlib import Path

log = logging.getLogger("scaffolder")

# Platforms to include in unified service
UNIFIED_PLATFORMS = ["catalyst", "meraki", "intersight", "nexus_hyperfabric", "sdwan_mngr"]


def regenerate_unified_service_init(out_dir: Path) -> None:
    """
    Regenerate the unified __init__.py file that imports all platform services.
    
    This allows users to do:
        from app.llm.cisco import meraki, catalyst, intersight
    """
    init_lines = [
        '"""',
        'Unified namespace for all Cisco platform services.',
        '',
        'This module provides a convenient way to access all platform services:',
        '',
        '    from app.llm.cisco import meraki, catalyst, intersight',
        '    ',
        '    # Use the services',
        '    meraki_svc = meraki.MerakiService()',
        '    catalyst_svc = catalyst.CatalystService()',
        '"""',
        '',
    ]
    
    # Add imports for each platform
    for platform in UNIFIED_PLATFORMS:
        init_lines.extend([
            f'try:',
            f'    from . import {platform}',
            f'except ImportError as e:',
            f'    # Platform module not available',
            f'    {platform} = None',
            f'    import warnings',
            f'    warnings.warn(f"Could not import {platform}: {{e}}")',
            '',
        ])
    
    # Add __all__ export
    init_lines.extend([
        '',
        '__all__ = [',
        *[f'    "{platform}",' for platform in UNIFIED_PLATFORMS],
        ']',
        '',
        '# For backwards compatibility, also expose the service classes directly',
    ])
    
    # Add service class imports
    for platform in UNIFIED_PLATFORMS:
        init_lines.extend([
            f'try:',
            f'    from .{platform} import {platform.capitalize()}Service',
            f'except (ImportError, AttributeError):',
            f'    {platform.capitalize()}Service = None',
            '',
        ])
    
    # Write the file
    init_file = out_dir / "__init__.py"
    init_file.parent.mkdir(parents=True, exist_ok=True)
    init_file.write_text('\n'.join(init_lines))
    
    log.info("✍  regenerated unified __init__.py")


def emit_unified_service(platform: str, out_dir: Path) -> None:
    """
    Generate the service wrapper for a platform.
    
    This creates <platform>/__init__.py that provides a high-level service interface.
    """
    service_lines = [
        '"""',
        f'{platform.capitalize()} service wrapper.',
        '',
        'This module provides a high-level interface to the {platform} platform.',
        '"""',
        '',
        'import logging',
        f'from app.llm.cisco_clients.{platform}_client import {platform.capitalize()}Client',
        '',
        f'log = logging.getLogger("cisco.{platform}")',
        '',
        '',
        f'class {platform.capitalize()}Service:',
        f'    """High-level service interface for {platform}."""',
        '    ',
        '    def __init__(self, **kwargs):',
        f'        """Initialize {platform} service with optional configuration."""',
        f'        self.client = {platform.capitalize()}Client(**kwargs)',
        '    ',
        '    def __getattr__(self, name):',
        '        """Delegate attribute access to the client."""',
        '        return getattr(self.client, name)',
        '    ',
        '    def __repr__(self):',
        f'        return f"<{platform.capitalize()}Service>"',
        '',
        '',
        '# For convenience, create a default instance',
        f'default_service = {platform.capitalize()}Service()',
        '',
        '# Export the service class',
        f'__all__ = ["{platform.capitalize()}Service", "default_service"]',
    ]
    
    # Write the service file
    service_dir = out_dir / platform
    service_dir.mkdir(parents=True, exist_ok=True)
    
    init_file = service_dir / "__init__.py"
    init_file.write_text('\n'.join(service_lines) + '\n')
    
    log.info("✍  wrote %s/__init__.py", platform)