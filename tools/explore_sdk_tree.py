#!/usr/bin/env python3
"""
Count and list all endpoint functions in catalystwan.endpoints,
then compare against what explore_sdk_tree(session.api) finds.
"""
import pkgutil
import importlib
import inspect
import json
from pathlib import Path
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
from your_tools.generate_sdwan_registry import explore_sdk_tree, camel_case  # adjust import as needed

def list_all_endpoint_functions() -> set[str]:
    """
    Walk through catalystwan.endpoints, import each module, and collect
    every function name as camelCase(module_func_name).
    """
    import catalystwan.endpoints as eps_pkg
    all_funcs = set()
    for finder, mod_name, ispkg in pkgutil.iter_modules(eps_pkg.__path__):
        full_mod = importlib.import_module(f"catalystwan.endpoints.{mod_name}")
        for name, obj in inspect.getmembers(full_mod, inspect.isfunction):
            # skip private/helpers
            if name.startswith("_"):
                continue
            all_funcs.add(camel_case(name))
    return all_funcs

def list_session_api_methods() -> set[str]:
    """
    Use your existing explorer on a dummy session to collect what session.api exposes.
    """
    dummy_auth = vManageAuth(username="", password="")
    sess = ManagerSession(base_url="https://dummy", auth=dummy_auth)
    sdk_map = explore_sdk_tree(sess.api)  # returns { key: (endpoint, method) }
    return set(sdk_map.keys())

def main():
    eps = list_all_endpoint_functions()
    api = list_session_api_methods()

    print(f"Total functions under catalystwan.endpoints: {len(eps)}")
    print(f"Total methods surfaced via session.api:  {len(api)}")
    print(f"Intersection (mapped):                    {len(eps & api)}")
    print(f"Only in endpoints  (not in session.api): {len(eps - api)}")
    print(f"Only in session.api (not real endpoints):{len(api - eps)}")

    if eps - api:
        print("\nExamples of endpoints missing from session.api:")
        for missing in sorted(list(eps - api))[:20]:
            print("  ", missing)

    if api - eps:
        print("\nExamples of methods in session.api with no matching endpoint module:")
        for extra in sorted(list(api - eps))[:20]:
            print("  ", extra)

    # Write results for further inspection
    out = {
        "all_endpoints": sorted(eps),
        "session_api": sorted(api),
    }
    Path("tools/sdk_endpoint_compare.json").write_text(json.dumps(out, indent=2))
    print("\nWrote detailed lists to tools/sdk_endpoint_compare.json")

if __name__ == "__main__":
    main()
