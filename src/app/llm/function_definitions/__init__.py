# Auto-generated – DO NOT EDIT
# app/llm/function_definitions/__init__.py
""" 
Loads every *.json in this folder into FUNCTION_DEFINITIONS
    { '<platform>': [{…}, … ] , … }
""" 
from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Any

_DIR = Path(__file__).parent
FUNCTION_DEFINITIONS: Dict[str, List[Dict[str, Any]]] = {}

for _fp in _DIR.glob('*.json'):
    try:
        FUNCTION_DEFINITIONS[_fp.stem] = json.loads(_fp.read_text(encoding='utf-8'))
    except Exception as exc:
        print(f'[function_definitions] ⚠️  skipped {_fp.name}: {exc}')

__all__ = ['FUNCTION_DEFINITIONS']
