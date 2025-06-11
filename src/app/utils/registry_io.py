import json
from pathlib import Path

AGENT_ROOT = Path(__file__).resolve().parents[2]   # utils → app
REGISTRY_FILE = AGENT_ROOT / "llm" / "platform_registry.json"

def load_registry() -> dict:
    try:
        return json.loads(REGISTRY_FILE.read_text("utf-8"))
    except Exception:
        return {}

def save_registry(reg: dict) -> None:
    REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_FILE.write_text(json.dumps(reg, indent=2), encoding="utf-8")
