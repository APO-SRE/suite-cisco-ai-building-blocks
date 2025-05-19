# file: ai-building-blocks-agent/scripts/utils/paths.py
#!/usr/bin/env python3
from pathlib import Path
import os

def get_chroma_root() -> Path:
    """
    Resolve the folder that stores *this layer’s* Chroma collections.
    1) Prefer CHROMA_DB_ROOT if set (for cross-layer sharing).
    2) Fall back to FASTAPI_CHROMA_DB_PATH (legacy var you already have).
    """
    root = os.getenv("CHROMA_DB_ROOT")
    if root:
        return Path(root).expanduser().resolve()

    layer_path = os.getenv("FASTAPI_CHROMA_DB_PATH", "./chroma_dbs/fastapi")
    return Path(layer_path).expanduser().resolve()
