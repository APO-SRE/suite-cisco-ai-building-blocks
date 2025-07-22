#!/usr/bin/env python3
"""
suite-cisco-ai-building-blocks/src/app/utils/sdk_initialization.py
SDK Initialization Helper
Handles automatic SDK client initialization based on the registry
"""
import json
import importlib
import inspect
import logging
from typing import Dict, Any, Optional, Tuple
from pathlib import Path
import os

log = logging.getLogger(__name__)


class SDKInitializer:
    """Handles SDK initialization for all Cisco platforms"""
    
    def __init__(self, registry_path: Optional[str] = None):
        """
        Initialize with SDK registry
        
        Args:
            registry_path: Path to platform_registry.json
        """
        if registry_path is None:
            # Look for platform_registry.json in the llm folder
            registry_path = Path(__file__).parent.parent / "llm" / "platform_registry.json"
        
        with open(registry_path, 'r') as f:
            self.registry = json.load(f)
    
    def get_required_env_vars(self, platform: str) -> Dict[str, str]:
        """
        Get required environment variables for a platform
        
        Returns:
            Dict mapping env var names to descriptions
        """
        if platform not in self.registry:
            raise ValueError(f"Unknown platform: {platform}")
        
        platform_config = self.registry[platform]
        auth_config = platform_config.get('auth_config', {})
        env_var_mapping = auth_config.get('env_vars', {})
        
        # Return the actual env vars from the registry
        env_vars = {}
        for param_name, env_var in env_var_mapping.items():
            env_vars[env_var] = f"{param_name.replace('_', ' ').title()} for {platform}"
        
        return env_vars
    
    def initialize_sdk(self, platform: str, **kwargs) -> Tuple[Any, Dict[str, Any]]:
        """
        Initialize an SDK client for the given platform
        
        Args:
            platform: Platform name (e.g., 'meraki', 'catalyst_center')
            **kwargs: Override parameters for initialization
            
        Returns:
            Tuple of (initialized_client, initialization_params)
        """
        if platform not in self.registry:
            raise ValueError(f"Unknown platform: {platform}")
        
        platform_config = self.registry[platform]
        sdk_module_name = platform_config.get('sdk_module', '')
        main_class_name = platform_config.get('sdk_class', 'Client')
        
        if not sdk_module_name:
            raise ValueError(f"No SDK module configured for {platform}")
        
        # Import the SDK module
        try:
            sdk_module = importlib.import_module(sdk_module_name)
        except ImportError as e:
            log.error(f"Failed to import {sdk_module_name}: {e}")
            raise RuntimeError(f"SDK module {sdk_module_name} not installed. Run: pip install {sdk_module_name}")
        
        # Get the main class
        main_class = getattr(sdk_module, main_class_name, None)
        if main_class is None:
            # Try to find it by searching
            for name, obj in inspect.getmembers(sdk_module, inspect.isclass):
                if main_class_name.lower() in name.lower():
                    main_class = obj
                    break
        
        if main_class is None:
            raise RuntimeError(f"Could not find class {main_class_name} in {sdk_module_name}")
        
        # Build initialization parameters
        init_params = self._build_init_params(platform, platform_config, kwargs)
        
        # Initialize the client
        try:
            if platform == 'intersight':
                # Special handling for Intersight
                client = self._init_intersight(sdk_module, init_params)
            else:
                client = main_class(**init_params)
            
            log.info(f"Successfully initialized {platform} SDK client")
            return client, init_params
            
        except Exception as e:
            log.error(f"Failed to initialize {platform} client: {e}")
            raise
    
    def _build_init_params(self, platform: str, config: Dict, overrides: Dict) -> Dict[str, Any]:
        """Build initialization parameters from env vars and overrides"""
        params = {}
        auth_config = config.get('auth_config', {})
        auth_type = auth_config.get('type', 'api_key')
        env_var_mapping = auth_config.get('env_vars', {})
        
        # Get parameters from environment variables using mapping from registry
        required_params = auth_config.get('init_params', {}).get('required', [])
        
        if auth_type == 'api_key':
            api_key_env = env_var_mapping.get('api_key', f'{platform.upper()}_API_KEY')
            api_key = overrides.get('api_key') or os.getenv(api_key_env)
            if not api_key and 'api_key' in required_params:
                raise ValueError(f"Missing API key for {platform}")
            if api_key:
                params['api_key'] = api_key
            
        elif auth_type == 'api_key_secret':
            api_key_env = env_var_mapping.get('api_key') or env_var_mapping.get('key', f'{platform.upper()}_API_KEY')
            api_secret_env = env_var_mapping.get('api_secret') or env_var_mapping.get('secret', f'{platform.upper()}_API_SECRET')
            api_key = overrides.get('api_key') or overrides.get('key') or os.getenv(api_key_env)
            api_secret = overrides.get('api_secret') or overrides.get('secret') or os.getenv(api_secret_env)
            
            # Map to correct parameter names based on platform
            if platform == 'intersight':
                if not api_key or not api_secret:
                    raise ValueError(f"Missing API key or secret for {platform}")
                params['api_key'] = api_key
                params['api_secret'] = api_secret
            else:
                # For others like umbrella
                key_param = 'key' if 'key' in required_params else 'api_key'
                secret_param = 'secret' if 'secret' in required_params else 'api_secret'
                if not api_key or not api_secret:
                    raise ValueError(f"Missing API key or secret for {platform}")
                params[key_param] = api_key
                params[secret_param] = api_secret
            
        elif auth_type == 'basic_auth':
            username = overrides.get('username') or os.getenv(f'{platform_upper}_USERNAME')
            password = overrides.get('password') or os.getenv(f'{platform_upper}_PASSWORD')
            base_url = overrides.get('base_url') or os.getenv(f'{platform_upper}_BASE_URL')
            if not all([username, password, base_url]):
                raise ValueError(f"Missing credentials or base URL for {platform}")
            params.update({
                'username': username,
                'password': password,
                'base_url': base_url
            })
            
        elif auth_type == 'bearer_token':
            access_token = overrides.get('access_token') or os.getenv(f'{platform_upper}_ACCESS_TOKEN')
            if not access_token:
                raise ValueError(f"Missing access token for {platform}")
            params['access_token'] = access_token
            
        elif auth_type == 'session_based':
            host = overrides.get('host') or os.getenv(f'{platform_upper}_HOST')
            username = overrides.get('username') or os.getenv(f'{platform_upper}_USERNAME')
            password = overrides.get('password') or os.getenv(f'{platform_upper}_PASSWORD')
            if not all([host, username, password]):
                raise ValueError(f"Missing host or credentials for {platform}")
            
            # Handle different parameter names
            if platform == 'sdwan':
                params['vmanage_host'] = host
            else:
                params['host'] = host
            params.update({
                'username': username,
                'password': password
            })
            
        elif auth_type == 'duo_auth':
            ikey = overrides.get('ikey') or os.getenv(f'{platform_upper}_IKEY')
            skey = overrides.get('skey') or os.getenv(f'{platform_upper}_SKEY')
            host = overrides.get('host') or os.getenv(f'{platform_upper}_HOST')
            if not all([ikey, skey, host]):
                raise ValueError(f"Missing Duo credentials for {platform}")
            params.update({
                'ikey': ikey,
                'skey': skey,
                'host': host
            })
        
        # Add any additional overrides
        params.update(overrides)
        
        return params
    
    def _init_intersight(self, sdk_module, params: Dict) -> Any:
        """Special initialization for Intersight SDK"""
        configuration = sdk_module.Configuration()
        configuration.host = params.get('host', 'https://intersight.com/api/v1')
        
        if 'api_key' in params and 'api_secret' in params:
            configuration.api_key['api_key'] = params['api_key']
            configuration.api_key_secret = params['api_secret']
        
        return sdk_module.ApiClient(configuration)
    
    def validate_sdk_installation(self, platform: str) -> bool:
        """
        Check if SDK is installed for a platform
        
        Returns:
            True if SDK is installed, False otherwise
        """
        if platform not in self.registry:
            return False
        
        sdk_module_name = self.registry[platform].get('sdk_module', '')
        if not sdk_module_name:
            return False
        
        try:
            importlib.import_module(sdk_module_name)
            return True
        except ImportError:
            return False
    
    def get_missing_sdks(self) -> Dict[str, str]:
        """
        Get list of platforms with missing SDKs
        
        Returns:
            Dict mapping platform to pip install command
        """
        missing = {}
        
        for platform, config in self.registry.items():
            if not self.validate_sdk_installation(platform):
                sdk_module = config.get('sdk_module', '')
                if sdk_module:
                    # Map module names to pip packages
                    pip_package = self._get_pip_package_name(sdk_module)
                    missing[platform] = f"pip install {pip_package}"
        
        return missing
    
    def _get_pip_package_name(self, module_name: str) -> str:
        """Map module names to pip package names"""
        # Some modules have different pip package names
        package_mapping = {
            'meraki': 'meraki',
            'dnacentersdk': 'dnacentersdk',
            'webexteamssdk': 'webexteamssdk',
            'intersight': 'intersight',
            'nd_sdk': 'cisco-nd-sdk',
            'nexus_hyperfabric': 'cisco-nexus-hyperfabric',
            'vmanage_sdk': 'cisco-sdwan',
            'cisco_ai_defense': 'cisco-ai-defense',
            'cloudlock_sdk': 'cisco-cloudlock',
            'duo_client': 'duo-client',
            'umbrella_sdk': 'cisco-umbrella'
        }
        
        return package_mapping.get(module_name, module_name)


# Example usage and testing
if __name__ == "__main__":
    # Initialize the helper
    initializer = SDKInitializer()
    
    # Check what env vars are needed for each platform
    print("Required environment variables by platform:")
    print("-" * 50)
    
    for platform in ['meraki', 'catalyst', 'intersight', 'umbrella']:
        try:
            env_vars = initializer.get_required_env_vars(platform)
            print(f"\n{platform}:")
            for var, desc in env_vars.items():
                print(f"  {var}: {desc}")
        except Exception as e:
            print(f"\n{platform}: Error - {e}")
    
    # Check for missing SDKs
    print("\n\nMissing SDKs:")
    print("-" * 50)
    missing = initializer.get_missing_sdks()
    if missing:
        for platform, install_cmd in missing.items():
            print(f"{platform}: {install_cmd}")
    else:
        print("All SDKs are installed!")
    
    # Try to initialize a client (example)
    # client, params = initializer.initialize_sdk('meraki', api_key='test_key')