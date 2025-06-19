#!/usr/bin/env python3
"""
Scan app/llm/function_definitions for names that OpenAI will reject.
"""
import json, re, sys
from pathlib import Path

SAFE = re.compile(r'^[A-Za-z0-9_.-]{1,64}$')
root = Path('app/llm/function_definitions')
bad  = []

for fp in root.glob('*.json'):
    data = json.loads(fp.read_text(encoding='utf-8'))
    for i, fn in enumerate(data, 1):
        name = fn.get('name', '')
        if not SAFE.match(name):
            bad.append((fp.name, i, name))

if not bad:
    print('✅  All function names are OpenAI‑safe')
    sys.exit(0)

print('❌  Found invalid names:\n')
for file, idx, name in bad:
    print(f'  {file:<35}  functions[{idx}]  →  {name!r}')
sys.exit(1)
