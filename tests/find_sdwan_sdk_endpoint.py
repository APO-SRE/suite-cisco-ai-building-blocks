#!/usr/bin/env python3
import os
import sys
import json
import urllib3
import logging
from dotenv import load_dotenv
from catalystwan.session import create_manager_session, ManagerSession


def explore(obj, prefix, out, visited):
    """
    Recursively explore `obj`, collect callable paths into `out`, and avoid cycles via `visited`.
    """
    if isinstance(obj, (str, bytes, int, float, bool)):
        return
    obj_id = id(obj)
    if obj_id in visited:
        return
    visited.add(obj_id)

    for name in sorted(n for n in dir(obj) if not n.startswith('_')):
        try:
            val = getattr(obj, name)
        except Exception:
            continue
        full = f"{prefix}.{name}"
        if callable(val):
            out.append(full)
        else:
            explore(val, full, out, visited)


def update_registry(endpoints, registry_path, output_path):
    """
    Load the registry JSON, replace placeholder sdk_endpoint with matches from collected endpoints,
    and write updated registry to output_path.
    """
    with open(registry_path) as f:
        registry = json.load(f)

    # Build a map from method name to full endpoint paths
    name_map = {}
    for ep in endpoints:
        key = ep.split('.')[-1]
        name_map.setdefault(key, []).append(ep)

    updated = False
    for op in registry.get('operations', []):
        if op.get('sdk_endpoint') == '!!!_NEEDS_MANUAL_FIX_!!!':
            op_name = op.get('operationId') or op.get('name')
            candidates = name_map.get(op_name)
            if candidates:
                # if exactly one candidate, fill it in
                if len(candidates) == 1:
                    op['sdk_endpoint'] = candidates[0]
                    updated = True
                else:
                    print(f"Multiple matches for {op_name}: {candidates}")
            else:
                print(f"No SDK endpoint found for {op_name}")

    if updated:
        with open(output_path, 'w') as f:
            json.dump(registry, f, indent=2)
        print(f"✅ Registry updated and written to {output_path}")
    else:
        print("⚠️ No placeholders were automatically replaced. Check matching logic or candidate lists.")


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Part 1: Collect endpoints
    url  = os.getenv('CISCO_SD_WAN_BASE_URL')
    user = os.getenv('CISCO_SD_WAN_USERNAME')
    pwd  = os.getenv('CISCO_SD_WAN_PASSWORD')
    if not all([url, user, pwd]):
        print("ERROR: set CISCO_SD_WAN_BASE_URL, CISCO_SD_WAN_USERNAME & CISCO_SD_WAN_PASSWORD")
        sys.exit(1)

    session: ManagerSession = None
    try:
        session = create_manager_session(
            url=url,
            username=user,
            password=pwd,
            logger=logging.getLogger("catalystwan")
        )
        session.request_timeout = 30
        session.polling_requests_timeout = 10

        print("✅ Connected to vManage")

        endpoints = []
        visited = set()
        explore(session.api, 'session.api', endpoints, visited)

    except Exception as e:
        print(f"Unexpected error during exploration: {e}")
        logging.exception("Full traceback:")
        sys.exit(2)

    finally:
        if session and getattr(session, 'is_logged_in', False):
            session.logout()
            print("✅ Logged out")

    # Part 2: Update registry
    registry_in  = 'src/app/llm/sdwan_operation_registry_CORRECTED.json'
    registry_out = 'src/app/llm/sdwan_operation_registry_UPDATED.json'
    update_registry(endpoints, registry_in, registry_out)


if __name__ == '__main__':
    main()
