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
Very thin wrapper around a *single* Chroma collection.

• query(text, k)               – generic top‑k vector search
• retrieve_event_info(text)    – alias of query(text, 5)
• retrieve_domain_info(text)   – alias of query(text, 5)
• retrieve_api_docs(text, pls) – same, but filtered by platform meta
• FunctionRetriever            – exposes .query exactly as dynamic.py expects
"""
#!/usr/bin/env python3

import os
import logging
from pathlib import Path
from typing import Sequence, List, Dict, Any

import chromadb
from chromadb.config import Settings

log = logging.getLogger(__name__)

class ChromaRetriever:
    def __init__(self, *, layer: str = "FASTAPI", collection_name: str | None = None) -> None:
        layer_uc = layer.upper()
        base_path = os.getenv(f"{layer_uc}_CHROMA_DB_PATH", "./chroma_dbs/fastapi")
        coll_name = collection_name or os.getenv(f"{layer_uc}_CHROMA_COLLECTION_PLATFORM", "platform-summaries-index")

        self.path = Path(base_path).expanduser().resolve() / coll_name
        if not self.path.exists():
            raise FileNotFoundError(f"Chroma collection directory '{self.path}' not found.")

        client = chromadb.PersistentClient(path=str(self.path), settings=Settings(anonymized_telemetry=False))
        self.col = client.get_or_create_collection(coll_name)

    def query(self, text: str, *, k: int = 5, filter: Dict[str, Any] | None = None) -> List[dict]:
        where_clause = filter if filter else None
        res = self.col.query(
            query_texts=[text],
            n_results=k,
            include=["documents", "distances", "metadatas"],
            where=where_clause,
        )
        docs = res.get("documents", [[]])[0]
        metas = res.get("metadatas", [[]])[0]
        dists = (res.get("distances") or [[None]])[0]

        out = []
        for doc, meta, dist in zip(docs, metas, dists):
            item = {"content": doc, **(meta or {}), "distance": dist}
            out.append(item)
        return out

    def retrieve_domain_info(self, text: str) -> List[dict]:
        return self.query(text, k=5)

    def retrieve_api_docs(self, text: str, platforms: Sequence[str]) -> List[dict]:
        if not platforms:
            return []
        return self.query(text, k=8, filter={"platform": {"$in": list(platforms)}})

class FunctionRetriever:
    def __init__(self, collection_name: str) -> None:
        self._inner = ChromaRetriever(collection_name=collection_name)

    def query(self, *args, **kwargs):
        return self._inner.query(*args, **kwargs)
