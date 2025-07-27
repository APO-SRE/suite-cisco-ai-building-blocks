#!/usr/bin/env python3
import pkgutil
import inspect
import importlib
import catalystwan.endpoints as endpoints_pkg

count = 0
for finder, modname, ispkg in pkgutil.walk_packages(endpoints_pkg.__path__, endpoints_pkg.__name__ + "."):
    module = importlib.import_module(modname)
    funcs = [name for name, obj in inspect.getmembers(module, inspect.isfunction)]
    if funcs:
        print(f"{modname}: {len(funcs)} functions")
        count += len(funcs)

print(f"\nTotal endpoint functions found: {count}")
