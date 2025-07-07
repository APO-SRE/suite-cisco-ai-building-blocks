#!/usr/bin/env python3
"""
Enhanced smoke-test for Cisco Catalyst (DNA) Center API using env vars.
"""

import os
import sys
import logging

# 1) Try to load a .env file (if you have python-dotenv installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("Loaded .env file (if present)")
except ImportError:
    print("python-dotenv not installed; skipping .env load")

# 2) Read & echo the critical env vars
def get_env(name):
    val = os.getenv(name)
    print(f"{name} = {val!r}")
    return val

USERNAME = get_env("DNACENTER_USERNAME")
PASSWORD = get_env("DNACENTER_PASSWORD")
BASE_URL = get_env("DNACENTER_BASE_URL")
VERSION  = os.getenv("DNACENTER_VERSION", "2.3.7.6")
VERIFY   = os.getenv("DNACENTER_VERIFY_SSL", "true").lower() in ("1","true","yes")

if not (USERNAME and PASSWORD and BASE_URL):
    print("\nERROR: You must export DNACENTER_USERNAME, DNACENTER_PASSWORD, and DNACENTER_BASE_URL")
    sys.exit(1)

# 3) Enable debug logging for HTTP traffic
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logging.getLogger("urllib3").setLevel(logging.DEBUG)

# 4) Import and construct the client
try:
    from dnacentersdk import DNACenterAPI
except ImportError as e:
    print("ERROR: Could not import dnacentersdk:", e)
    print("Please `pip install dnacentersdk` and try again.")
    sys.exit(1)

api = DNACenterAPI(
    username=USERNAME,
    password=PASSWORD,
    base_url=BASE_URL,
    version=VERSION,
    verify=VERIFY
)
print("\n✅ DNACenterAPI client constructed.")

# 5) List available methods that mention “interface”
methods = [m for m in dir(api) if "interface" in m.lower()]
print("\n🔍 interface methods found on DNACenterAPI:")
for m in methods:
    print(" •", m)

# 6) Attempt one of them
preferred = "get_all_interfaces"
if preferred not in methods and methods:
    preferred = methods[0]

print(f"\n▶️  Calling api.{preferred}() …")
try:
    resp = getattr(api, preferred)()
    print("✅ Success! Response:")
    print(resp)
except Exception as e:
    print("❌ Error during API call:", e)
