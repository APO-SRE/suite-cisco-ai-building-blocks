#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/indexers/chroma_indexer.py
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
import json
import os
from pathlib import Path
from typing import List, Dict, Any

import chromadb
from chromadb import PersistentClient                      # type: ignore
from chromadb.config import Settings                       # type: ignore

from .base_indexer import BaseIndexer


class ChromaIndexer(BaseIndexer):
    def __init__(self, index_name: str, layer_name: str = "") -> None:
        super().__init__(index_name)

        self.layer_key = layer_name.upper().strip() if layer_name else ""

        # ── 1. Resolve *base* path from the env
        base_path = os.getenv(f"{self.layer_key}_CHROMA_DB_PATH",
                              "./chroma_db")

        # ── 2. Append the collection name ⇒ <base>/<collection>/
        db_dir = Path(base_path).expanduser().resolve() / self.index_name
        db_dir.mkdir(parents=True, exist_ok=True)

        print(f"[ChromaIndexer] DB directory → {db_dir}")

        # ── 3. Create / reuse the local Chroma client
        self.client: PersistentClient = chromadb.PersistentClient(
            path=str(db_dir),
            settings=Settings(anonymized_telemetry=False),
        )
        self.collection = None

    # --------------------------------------------------------------------- #
    # Index management helpers
    # --------------------------------------------------------------------- #
    def create_index(self) -> None:
        if self.collection is None:
            print(f"[ChromaIndexer] create_index('{self.index_name}')")
            self.collection = self.client.get_or_create_collection(
                self.index_name
            )
            print(f"[ChromaIndexer] Collection ready – "
                  f"{self.collection.count()} vectors")

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #
    def index_documents(self, docs: List[Dict[str, Any]]) -> None:
        if not self.collection:
            self.create_index()

        ids, contents, embeddings, metadatas = [], [], [], []

        for doc in docs:
            doc_id = doc.get("id")
            if not doc_id:
                raise ValueError("Each doc must have an 'id' field")

            ids.append(doc_id)
            contents.append(doc.get("content", ""))
            embeddings.append(doc.get("embedding"))
            metadatas.append(
                {k: v for k, v in doc.items() if k not in {"content",
                                                           "embedding"}}
            )

        # omit “embeddings” if all are None – lets Chroma embed later
        kwargs: Dict[str, Any] = dict(
            ids=ids, documents=contents, metadatas=metadatas,
        )
        if any(e is not None for e in embeddings):
            kwargs["embeddings"] = embeddings

        self.collection.add(**kwargs)
        print(f"[ChromaIndexer] Inserted {len(docs)} documents")

    # Small helper used by PlatformFunctionIndexer
    def add(self, *, documents: List[str], ids: List[str],
            metadatas: List[dict] | None = None,
            embeddings: List[List[float]] | None = None) -> None:
        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas or [{} for _ in ids],
            embeddings=embeddings,
        )


class PlatformFunctionIndexer(ChromaIndexer):
    """
    Specialised for diet-function JSON blobs.
    """
    def index_functions(self, platform: str,
                        diet_list: List[Dict[str, Any]],
                        full_spec: Dict[str, Any]) -> None:
        if self.collection is None:
            self.create_index()

        self.collection.upsert(
            ids=[f"{platform}:{fn['name']}" for fn in diet_list],
            documents=[json.dumps(fn) for fn in diet_list],
            metadatas=[{"platform": platform, "name": fn["name"]}
                       for fn in diet_list],
        )

