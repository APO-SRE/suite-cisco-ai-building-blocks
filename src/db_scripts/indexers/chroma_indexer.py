#!/usr/bin/env python3
################################################################################
## suite-cisco-ai-building-blocks/src/db_scripts/indexers/chroma_indexer.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
from __future__ import annotations


"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""

import base64
import json
import os
import re
import shutil
import uuid
from pathlib import Path
from threading import Lock
from typing import Any, Dict, List
from dotenv import load_dotenv
import chromadb
from chromadb import PersistentClient                      # type: ignore
from chromadb.config import Settings                       # type: ignore
from concurrent.futures import ThreadPoolExecutor
from app.utils.embedding import embed_text
from .base_indexer import BaseIndexer
load_dotenv()
# ───────────────────────────── runtime tuning ──────────────────────────────
CPU_WORKERS  = int(os.getenv("FASTAPI_CHROMA_NUM_CPUS", "4") or 4)
DEFAULT_BATCH = int(os.getenv("FASTAPI_CHROMA_BATCH", "500") or 500)

print(
    f"[ChromaIndexer]  ⚙  embedding threads = {CPU_WORKERS}  |  "
    f"default batch size (upsert) = {DEFAULT_BATCH}",
    flush=True,
)

# ───────────────────────────── helpers ─────────────────────────────────────

SAFE_ID_CHARS = re.compile(r"[^A-Za-z0-9_\-=]")

def _safe_id(text: str) -> str:
    cleaned = SAFE_ID_CHARS.sub("_", text)
    return cleaned if len(cleaned) <= 500 else base64.urlsafe_b64encode(text.encode()).decode()[:500]

def dedupe_ids(ids: list[str]) -> list[str]:
    """Append a counter to any duplicate IDs to make them unique."""
    seen: dict[str, int] = {}
    out: list[str] = []
    for _id in ids:
        if _id not in seen:
            seen[_id] = 0
            out.append(_id)
        else:
            seen[_id] += 1
            out.append(f"{_id}_{seen[_id]}")   # e.g. foo, foo_1, foo_2
    return out

# ───────────────────────────── once-per-process guard ──────────────────────
_handled: set[str] = set()
_lock = Lock()            # serialises the decision phase


# ═══════════════════════════════════════════════════════════════════════════
#  BASE CHROMA INDEXER  (mirrors Azure recreation logic)
# ═══════════════════════════════════════════════════════════════════════════
class ChromaIndexer(BaseIndexer):
    """
    Persistent Chroma collection with single-prompt recreate behaviour.
    """

    # ────────────────────────────────────────────────────────────────
    #  constructor  – decide recreate / append exactly once
    # ────────────────────────────────────────────────────────────────
    def __init__(self, index_name: str, layer_name: str = "") -> None:
        super().__init__(index_name)

        self.collection_name = index_name
        self.layer_key       = layer_name.upper().strip() if layer_name else ""

        base_path = os.getenv(f"{self.layer_key}_CHROMA_DB_PATH", "../chroma_dbs")
        self.db_dir = Path(base_path).expanduser().resolve() / self.collection_name

        recreate_env = os.getenv(f"{self.layer_key}_CHROMA_RECREATE_INDEX", "").strip().lower()
        
        # ── decision happens only once per process per collection ──────────
        with _lock:
            if self.collection_name not in _handled:
                exists = self.db_dir.is_dir() and any(self.db_dir.iterdir())

                # ① choose behaviour
                if exists:
                    # env overrides prompt
                    if recreate_env == "true":
                        choice = "r"
                        print(f"[ChromaIndexer] {self.collection_name}: env forces RECREATE")
                    elif recreate_env == "false":
                        choice = "a"
                        print(f"[ChromaIndexer] {self.collection_name}: env forces APPEND")
                    else:
                        ans = input(
                            f"Collection '{self.collection_name}' exists. "
                            "(R)ecreate or (A)ppend? [R/a]: "
                        ).strip().lower()
                        choice = "r" if ans.startswith("r") else "a"

                else:
                    choice = "a"     # nothing to recreate on first run

                # ② carry out choice
                # only delete if the user really chose RECREATE
                if choice == "r" and self.db_dir.exists():
                    print(f"[ChromaIndexer] Deleting {self.db_dir} …")
                    shutil.rmtree(self.db_dir, ignore_errors=True)

                self.db_dir.mkdir(parents=True, exist_ok=True)
                _handled.add(self.collection_name)   # remember

        print(f"[ChromaIndexer] DB directory → {self.db_dir}")

        # ── open (or create) the collection ───────────────────────────────
        self.client: PersistentClient = chromadb.PersistentClient(
            path=str(self.db_dir),
            settings=Settings(anonymized_telemetry=False),
        )
        self.collection = self.client.get_or_create_collection(self.collection_name)
        print(f"[ChromaIndexer] Collection ready – {self.collection.count()} vectors")

    def create_index(self) -> None:          # ← add this method
        """
        Compatibility shim — the collection is fully initialised in __init__,
        so this is just a harmless no-op for callers that still invoke it.
        """
        pass
    # ────────────────────────────────────────────────────────────────
    #  generic bulk-index helper
    # ────────────────────────────────────────────────────────────────
    def index_documents(self, docs: List[Dict[str, Any]]) -> None:
        if not docs:
            return

        ids, contents, embeddings, metadatas = [], [], [], []
        for d in docs:
            ids.append(d.get("id") or str(uuid.uuid4()))
            contents.append(d.get("content", ""))
            embeddings.append(d.get("embedding"))
            metadatas.append({k: v for k, v in d.items() if k not in {"id", "content", "embedding"}})

        payload: Dict[str, Any] = dict(ids=ids, documents=contents, metadatas=metadatas)
        if any(e is not None for e in embeddings):
            payload["embeddings"] = embeddings

        self.collection.add(**payload)
        print(f"[ChromaIndexer] Inserted {len(docs)} documents")

    # thin helper
    def add(
        self,
        *,
        documents: List[str],
        ids: List[str],
        metadatas: List[dict] | None = None,
        embeddings: List[List[float]] | None = None,
    ) -> None:
        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas or [{} for _ in ids],
            embeddings=embeddings,
        )


# ═══════════════════════════════════════════════════════════════════════════
#  PLATFORM-SPECIFIC FUNCTION INDEXER
# ═══════════════════════════════════════════════════════════════════════════
class PlatformFunctionIndexer(ChromaIndexer):
    """
    Diet-function indexer for Chroma that now prints incremental progress
    identical to AzureIndexer.
    """

    def index_functions(
        self,
        platform: str,
        diet_list: List[Dict[str, Any]],
        full_spec: Dict[str, Any],   # kept for parity / future use
    ) -> None:
        # 1 ▸ make sure collection exists / recreate logic already handled
        self.create_index()

        total = len(diet_list)
        print(
            f"[{platform}] embedding {total} functions with "
            f"{CPU_WORKERS} thread(s)…",
            flush=True,
        )

        # ---------- worker used by the thread-pool ----------
        def _prep(fn: dict):
            key  = _safe_id(f"{platform}-{fn['name']}")
            vec  = fn.get("embedding") or embed_text(fn["name"])[0]
            meta = {"platform": platform, "name": fn["name"]}
            return key, json.dumps(fn), meta, vec

        ids, docs, metas, vecs = [], [], [], []

        # use as_completed so we can count finished jobs
        from concurrent.futures import ThreadPoolExecutor, as_completed

        with ThreadPoolExecutor(max_workers=CPU_WORKERS) as pool:
            futures = [pool.submit(_prep, fn) for fn in diet_list]

            for i, fut in enumerate(as_completed(futures), start=1):
                key, doc, meta, vec = fut.result()
                ids.append(key)
                docs.append(doc)
                metas.append(meta)
                vecs.append(vec)

                if i % 100 == 0 or i == total:          # Azure-style ticks
                    print(f"   • processed {i}/{total}", flush=True)

        # ---------- bulk upsert ----------
        print(f"[ChromaIndexer] Upserting {len(ids)} docs into '{self.collection_name}'")
        ids = dedupe_ids(ids)          # ← NEW
        self.collection.upsert(
            ids=ids,
            documents=docs,
            metadatas=metas,
            embeddings=vecs,
)
        print(
            f"[ChromaIndexer]  ✓ finished — {len(ids)} vectors written "
            f"with {CPU_WORKERS} worker(s)",
            flush=True,
        )
        