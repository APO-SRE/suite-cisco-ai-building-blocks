#!/usr/bin/env python3
"""
Count every callable method exposed under session.api, without invoking any network calls.
"""
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
from pathlib import Path
import logging

# suppress any warnings
logging.disable(logging.WARNING)

def count_methods(obj, visited=None) -> int:
    """Recursively count all public callables under obj."""
    if visited is None:
        visited = set()
    if id(obj) in visited:
        return 0
    visited.add(id(obj))

    total = 0
    for attr in dir(obj):
        if attr.startswith('_'):
            continue
        try:
            child = getattr(obj, attr)
        except Exception:
            continue

        # dive into sub‐APIs...
        if hasattr(child, '__dict__') and not callable(child):
            total += count_methods(child, visited)
        # count the method
        elif callable(child):
            total += 1

    return total

def main():
    print("🔍 Counting SDK methods...")
    # create an uninitialized session (no network will be used)
    dummy_auth = vManageAuth(username="", password="")
    session = ManagerSession(base_url="https://dummy", auth=dummy_auth)

    total = count_methods(session.api)
    print(f"✅ Total SDK methods found: {total}")

if __name__ == '__main__':
    main()
