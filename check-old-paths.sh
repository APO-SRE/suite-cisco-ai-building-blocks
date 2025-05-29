#!/usr/bin/env bash
set -euo pipefail

# Patterns to look for (grep -E regexes)
patterns=(
  "app_scripts"
  "ai-building-blocks-agent"
  "ai-building-blocks-database"
  "db_scripts"
  "source_open_api"
  "output_sdk"
  "user_commands\."
  "platform_dynamic_cache"


)

echo "🔍 Scanning for old paths and imports…"
for pat in "${patterns[@]}"; do
  echo
  echo "─── Pattern: ${pat} ─────────────────────────────────"
  grep -RInE \
    --exclude=check-old-paths.sh \
    --exclude=tests/test_imports.py
    --exclude-dir=src \
    --exclude-dir=.git \
    --exclude-dir=.git \
    --exclude-dir=venv \
    --exclude-dir=env \
    --exclude-dir=__pycache__ \
    --exclude-dir=*.egg-info \
    --exclude-dir=src/app/llm/platform_dynamic_cache \
    --exclude-dir=src/db_scripts/output_sdk \
    --exclude-dir=src/output_sdk \
    --include=*.py \
    --include=*.md \
    --include=*.yml \
    --include=*.yaml \
    --include=*.sh \
    --include=Makefile \
    --include=Dockerfile \
    --include=*.ini \
    -n "${pat}" . || true
done

echo
echo "✅ Done.  Review any hits above and update those paths/imports."
