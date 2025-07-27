#!/usr/bin/env python3
"""
Count every callable exposed on session.api without making any network calls.
"""
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
import inspect

def collect_callables(obj, seen=None):
    seen = seen or set()
    methods = set()

    # Prevent cycles
    if id(obj) in seen:
        return methods
    seen.add(id(obj))

    for name in dir(obj):
        if name.startswith('_'):
            continue
        try:
            member = getattr(obj, name)
        except Exception:
            continue

        # If it's a sub‑API object, recurse
        if hasattr(member, '__dict__') and not callable(member):
            methods |= collect_callables(member, seen)
        # If it’s callable, record its name
        elif callable(member):
            methods.add(name)

    return methods

def main():
    # Dummy session, no network calls will succeed
    sess = ManagerSession(
        base_url="https://dummy", 
        auth=vManageAuth(username="", password="")
    )

    all_methods = collect_callables(sess.api)
    print(f"📦 Total unique callables under session.api: {len(all_methods)}")
    # If you want to inspect them:
    # for m in sorted(all_methods):
    #     print(" -", m)

if __name__ == "__main__":
    main()
