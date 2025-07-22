"""
Function Dispatcher with SDK Validation
This module provides a validated function dispatcher that ensures called functions
exist in the SDK before attempting to execute them.

-- this is for runtime validation of SDK methods - as opposed to compile-time validation
    currently not being used - but could be usedin platform-scaffolder.py
"""
import importlib
import logging
from typing import Any, Callable, Dict, List, Optional, Set
from pathlib import Path
from app.utils.sdk_introspection import discover_sdk_methods_from_client, check_operation_id_availability

log = logging.getLogger(__name__)


class ValidatedFunctionDispatcher:
    """
    Function dispatcher that validates function availability in SDK before calling.
    """
    
    def __init__(self, sdk_instance):
        """
        Initialize the dispatcher with an SDK instance.
        
        Args:
            sdk_instance: The instantiated SDK client
        """
        self.sdk = sdk_instance
        self.available_methods = self._get_available_methods()
        self._method_cache = {}
        
    def _get_available_methods(self) -> Set[str]:
        """
        Discover all available methods in the SDK instance.
        
        Returns:
            Set of available method names
        """
        try:
            methods = discover_sdk_methods_from_client(self.sdk)
            log.info(f"Discovered {len(methods)} methods in SDK")
            return methods
        except Exception as e:
            log.error(f"Failed to discover SDK methods: {e}")
            return set()
    
    def validate_function(self, function_name: str) -> bool:
        """
        Check if a function is available in the SDK.
        
        Args:
            function_name: Name of the function to validate
            
        Returns:
            True if function is available, False otherwise
        """
        return check_operation_id_availability(function_name, self.available_methods)
    
    def dispatch(self, function_name: str, **kwargs) -> Any:
        """
        Dispatch a function call after validating it exists in the SDK.
        
        Args:
            function_name: Name of the function to call
            **kwargs: Arguments to pass to the function
            
        Returns:
            Result of the function call
            
        Raises:
            ValueError: If function is not available in SDK
            Exception: Any exception raised by the SDK method
        """
        # Check cache first
        if function_name in self._method_cache:
            method = self._method_cache[function_name]
        else:
            # Validate function availability
            if not self.validate_function(function_name):
                available_methods = sorted(self.available_methods)[:10]  # Show first 10
                raise ValueError(
                    f"Function '{function_name}' not available in SDK. "
                    f"Available methods include: {', '.join(available_methods)}..."
                )
            
            # Find the actual method
            method = self._resolve_method(function_name)
            if not method:
                raise ValueError(f"Could not resolve method for function '{function_name}'")
            
            # Cache for future use
            self._method_cache[function_name] = method
        
        # Execute the method
        try:
            log.info(f"Executing {function_name} with args: {list(kwargs.keys())}")
            result = method(**kwargs)
            log.info(f"Successfully executed {function_name}")
            return result
        except Exception as e:
            log.error(f"Error executing {function_name}: {e}")
            raise
    
    def _resolve_method(self, function_name: str) -> Optional[Callable]:
        """
        Resolve a function name to an actual callable method.
        
        Args:
            function_name: Name of the function to resolve
            
        Returns:
            The callable method or None if not found
        """
        import re
        
        # Try direct attribute
        if hasattr(self.sdk, function_name):
            return getattr(self.sdk, function_name)
        
        # Try snake_case conversion
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', function_name).lower()
        if hasattr(self.sdk, snake_case):
            return getattr(self.sdk, snake_case)
        
        # Check sub-clients (Meraki pattern)
        for attr_name in dir(self.sdk):
            if attr_name.startswith('_'):
                continue
            attr = getattr(self.sdk, attr_name)
            if hasattr(attr, function_name):
                return getattr(attr, function_name)
            if hasattr(attr, snake_case):
                return getattr(attr, snake_case)
        
        return None
    
    def get_available_functions(self) -> List[str]:
        """
        Get a list of all available function names.
        
        Returns:
            Sorted list of available function names
        """
        return sorted(self.available_methods)


def create_validated_dispatcher(platform: str, **sdk_kwargs) -> ValidatedFunctionDispatcher:
    """
    Create a validated function dispatcher for a specific platform.
    
    Args:
        platform: The platform name (e.g., 'meraki', 'catalyst')
        **sdk_kwargs: Arguments to pass to the SDK constructor
        
    Returns:
        ValidatedFunctionDispatcher instance
        
    Raises:
        ImportError: If platform client module not found
        ValueError: If SDK instantiation fails
    """
    # Import the platform-specific client
    try:
        client_module = importlib.import_module(f'app.llm.platform_clients.{platform}_client')
        client_class = getattr(client_module, f'{platform.capitalize()}Client')
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not import client for platform '{platform}': {e}")
    
    # Create the SDK instance
    try:
        sdk_instance = client_class(**sdk_kwargs)
    except Exception as e:
        raise ValueError(f"Failed to create SDK instance for '{platform}': {e}")
    
    # Return the validated dispatcher
    return ValidatedFunctionDispatcher(sdk_instance)