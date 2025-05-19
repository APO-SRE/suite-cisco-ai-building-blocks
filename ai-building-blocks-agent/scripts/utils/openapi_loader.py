#suite-cisco-ai-building-blocks/ai-building-blocks-agent/scripts/utils/openapi_loader.py
from pathlib import Path
import json


def load_spec(path: Path) -> dict:
    """Load an OpenAPI JSON/YAML file into a dict."""
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8") as f:
        return json.load(f)
