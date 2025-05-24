#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/retrievers/chroma_retriever.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
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

"""
Very thin wrapper around a *single* Chroma collection.

• query(text, k)               – generic top‑k vector search
• retrieve_event_info(text)    – alias of query(text, 5)
• retrieve_domain_info(text)   – alias of query(text, 5)
• retrieve_api_docs(text, pls) – same, but filtered by platform meta
• FunctionRetriever            – exposes .query exactly as dynamic.py expects
"""
 
import os
import logging
from pathlib import Path
from typing import Sequence, List, Dict, Any

import chromadb
from chromadb.config import Settings
from concurrent.futures import ThreadPoolExecutor, as_completed

from retrievers import default_pool_size          # ← safe (defined early)

log = logging.getLogger(__name__)


class ChromaRetriever:
    # ────────────────────────────────────────────────────────────────────
    # construction
    # ────────────────────────────────────────────────────────────────────
    def __init__(
        self,
        *,
        layer: str = "FASTAPI",
        collection_name: str | None = None,
    ) -> None:
        self.layer = layer.upper()
        base_path  = os.getenv(f"{self.layer}_CHROMA_DB_PATH", "./chroma_dbs/fastapi")
        coll_name  = (
            collection_name
            or os.getenv(f"{self.layer}_CHROMA_COLLECTION_PLATFORM", "platform-summaries-index")
        )

        self.path = Path(base_path).expanduser().resolve() / coll_name
        if not self.path.exists():
            raise FileNotFoundError(
                f"Chroma collection directory '{self.path}' not found."
            )

        client = chromadb.PersistentClient(
            path=str(self.path),
            settings=Settings(anonymized_telemetry=False),
        )
        self.col = client.get_or_create_collection(coll_name)

        # ── concurrency knobs ─────────────────────────────────────────
        self.pool_size = default_pool_size(self.layer, "chroma", fallback=4)
        print(
            f"[{self.layer}/ChromaRetriever]  ⚙  workers = {self.pool_size}",
            flush=True,
        )

    # ────────────────────────────────────────────────────────────────────
    # core query helpers
    # ────────────────────────────────────────────────────────────────────
    def _query_one(
        self,
        text: str,
        *,
        k: int,
        where_clause: Dict[str, Any] | None,
    ) -> List[dict]:
        res = self.col.query(
            query_texts=[text],
            n_results=k,
            include=["documents", "distances", "metadatas"],
            where=where_clause,
        )
        docs  = res.get("documents", [[]])[0]
        metas = res.get("metadatas", [[]])[0]
        dists = (res.get("distances") or [[None]])[0]

        return [
            {"content": doc, **(meta or {}), "distance": dist}
            for doc, meta, dist in zip(docs, metas, dists)
        ]

    # public – single text ------------------------------------------------
    def query(
        self,
        text: str,
        *,
        k: int = 5,
        filter: Dict[str, Any] | None = None,
    ) -> List[dict]:
        return self._query_one(text, k=k, where_clause=filter)

    # public – many texts (parallel) -------------------------------------
    def query_many(
        self,
        texts: Sequence[str],
        *,
        k: int = 5,
        filter: Dict[str, Any] | None = None,
    ) -> List[List[dict]]:
        if not texts:
            return []

        with ThreadPoolExecutor(max_workers=self.pool_size) as pool:
            futs = {
                pool.submit(self._query_one, t, k=k, where_clause=filter): idx
                for idx, t in enumerate(texts)
            }
            results: List[List[dict]] = [None] * len(texts)  # type: ignore
            for fut in as_completed(futs):
                results[futs[fut]] = fut.result()
        return results

    # convenience aliases -------------------------------------------------
    def retrieve_domain_info(self, text: str) -> List[dict]:
        return self.query(text, k=5)

    def retrieve_api_docs(
        self,
        text: str,
        platforms: Sequence[str],
    ) -> List[dict]:
        if not platforms:
            return []
        return self.query(text, k=8, filter={"platform": {"$in": list(platforms)}})


# ------------------------------------------------------------------------------
# adapter that dynamic.py expects ----------------------------------------------
class FunctionRetriever:
    def __init__(self, collection_name: str) -> None:
        self._inner = ChromaRetriever(collection_name=collection_name)

    def query(self, *args, **kwargs):
        return self._inner.query(*args, **kwargs)
