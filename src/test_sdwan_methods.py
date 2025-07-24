#!/usr/bin/env python3
"""Test SD-WAN method discovery directly"""
import catalystwan.api as api_module
import pkgutil
import importlib
import inspect

def test_direct_discovery():
    print("Testing direct SD-WAN API discovery...")
    
    method_count = 0
    
    # Iterate through all API submodules
    for importer, modname, ispkg in pkgutil.iter_modules(api_module.__path__):
        if modname in ['api_container', 'versions_utils']:  # Skip non-API modules
            continue
            
        try:
            # Import the API module
            full_module_name = f'catalystwan.api.{modname}'
            api_submodule = importlib.import_module(full_module_name)
            
            print(f"\nChecking module: {modname}")
            
            # Find API classes in the module
            for class_name, class_obj in inspect.getmembers(api_submodule, inspect.isclass):
                # Skip imported classes and base classes
                if (class_obj.__module__ != full_module_name or 
                    class_name.startswith('_') or
                    class_name in ['ABC', 'BaseModel']):
                    continue
                    
                print(f"  Found API class: {class_name}")
                
                # Count methods
                class_methods = 0
                for method_name, method in inspect.getmembers(class_obj):
                    if (not method_name.startswith('_') and 
                        callable(method) and 
                        not isinstance(method, type)):
                        class_methods += 1
                        
                print(f"    Methods: {class_methods}")
                method_count += class_methods
                
                # Show first few methods
                if class_methods > 0:
                    methods = [m for m, _ in inspect.getmembers(class_obj) 
                              if not m.startswith('_') and callable(getattr(class_obj, m))]
                    print(f"    Examples: {methods[:3]}")
                    
        except Exception as e:
            print(f"Error with {modname}: {e}")
    
    print(f"\nTotal methods found: {method_count}")
    return method_count

if __name__ == "__main__":
    test_direct_discovery()