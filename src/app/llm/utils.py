#!/usr/bin/env python3
# ./suite-cisco-ai-building-blocks/src/app/llm/utils.py
from __future__ import annotations
import os

# Map the suffix in ENABLE_<SUFFIX> to the slug used by your scaffolder/json files
_ALIAS = {
    "CATALYST_CENTER"     : "catalyst_center",
    "CATALYST_SD_WAN"     : "catalyst_sd_wan",
    "CISCO_SPACES"        : "spaces",
    "CISCO_WEBEX"         : "webex",
    "MERAKI"              : "meraki",
    "NEXUS_HYPERFABRIC"   : "nexus_hyperfabric",
    # add new platforms here ⬆
}

def enabled_platforms() -> list[str]:
    """
    Scan env for ENABLE_<PLATFORM>=true and return a list of platform slugs.
    Falls back to ['meraki'] if none are set.
    """
    out: list[str] = []
    for env_key, value in os.environ.items():
        if not env_key.startswith("ENABLE_"):
            continue
        if value.strip().lower() != "true":
            continue
        suffix = env_key[len("ENABLE_"):]
        slug   = _ALIAS.get(suffix, suffix.lower())
        out.append(slug)
    return out or ["meraki"]      # sensible default
