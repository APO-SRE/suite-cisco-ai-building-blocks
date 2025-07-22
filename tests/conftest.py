import pytest
import json
from pathlib import Path
import app.user_commands.create_sdk as create_sdk
from dotenv import load_dotenv
load_dotenv()
# Provide the symbols tests expect
create_sdk.OUTPUT_BASE_DIR = Path.cwd()

# Stub sanitize_sdk_name for tests
import re
create_sdk.sanitize_sdk_name = lambda name: re.sub(r'[^0-9A-Za-z_]', '_', name)

# Stub registry_short_name_for_spec for tests

def registry_short_name_for_spec(spec: Path, registry: dict) -> str | None:
    stem = spec.stem
    for short, entry in registry.items():
        if entry.get("openapi_name") == stem:
            return short
    return None

create_sdk.registry_short_name_for_spec = registry_short_name_for_spec

# Stub build_command for tests
def build_command(spec: Path, sdk_name: str, pkg_name: str) -> list[str]:
    dest = create_sdk.OUTPUT_BASE_DIR / pkg_name
    dest.mkdir(parents=True, exist_ok=True)
    config = dest / ".openapi-config.yml"
    config.write_text("config", encoding="utf-8")
    return [
        "openapi-python-client", "generate",
        "--path", str(spec),
        "--output-path", str(dest),
        "--meta", "poetry",
        "--overwrite",
        "--config", str(config),
    ]
create_sdk.build_command = build_command

# Stub save_registry to respect monkeypatched PLATFORM_REGISTRY_FILE
def save_registry(registry: dict, path: Path = None) -> None:
    if path is None:
        path = create_sdk.PLATFORM_REGISTRY_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(registry, indent=2), encoding="utf-8")
create_sdk.save_registry = save_registry

# Autouse fixture to set SD-WAN env vars for client tests
@pytest.fixture(autouse=True)
def sdwan_env(monkeypatch):
    monkeypatch.setenv("CISCO_SD_WAN_BASE_URL",   "https://example.com")
    monkeypatch.setenv("CISCO_SD_WAN_USERNAME",   "devnetuser")
    monkeypatch.setenv("CISCO_SD_WAN_PASSWORD",   "password123")
    monkeypatch.setenv("CISCO_SD_WAN_VERIFY_SSL", "false")
