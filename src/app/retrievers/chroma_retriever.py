#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## src/app/retrievers/chroma_retriever.py
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
from app.utils.paths import ensure_abs_env
from typing import Sequence, List, Dict, Any
import chromadb
from chromadb.config import Settings
from concurrent.futures import ThreadPoolExecutor, as_completed

from . import default_pool_size

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
        # dynamically resolve the Chroma DB root directory via ENV or default
        base_dir   = ensure_abs_env(
            f"{self.layer}_CHROMA_DB_PATH",
            "chroma_dbs/fastapi"
        )
        coll_name  = (
            collection_name
            or os.getenv(f"{self.layer}_CHROMA_COLLECTION_PLATFORM", "platform-summaries-index")
        )
        
        # assemble and normalize the collection path
        self.path = (base_dir / coll_name).resolve()
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




# ------------------------------------------------------------------------------
# adapter that dynamic.py expects ----------------------------------------------
class FunctionRetriever:
    def __init__(self, collection_name: str) -> None:
        self._inner = ChromaRetriever(collection_name=collection_name)

    def query(self, *args, **kwargs):
        results = self._inner.query(*args, **kwargs)
        
        # Only display for significant searches (not single result lookups)
        if results and len(results) > 1:
            try:
                from rich.console import Console
                from rich.table import Table
                from rich.panel import Panel
                
                console = Console()
                
                # Only show SD-WAN related results or top results
                sdwan_results = [r for r in results if r.get('platform') == 'sdwan_mngr'][:5]
                top_results = results[:3] if len(sdwan_results) < 3 else []
                display_results = sdwan_results + [r for r in top_results if r not in sdwan_results]
                
                if display_results:
                    # Create a compact table
                    table = Table(show_header=True, header_style="bold cyan", title_style="dim")
                    table.add_column("Function", style="green", width=25)
                    table.add_column("Platform", style="yellow", width=12)
                    table.add_column("Score", style="red", width=8)
                    table.add_column("Description", style="white", max_width=40)
                    
                    for result in display_results[:5]:  # Show top 5
                        func_name = result.get('name', 'N/A')
                        platform = result.get('platform', 'N/A')
                        distance = result.get('distance', 0)
                        
                        # Extract description from content JSON
                        desc = 'N/A'
                        content = result.get('content', '')
                        if isinstance(content, str) and content.startswith('{'):
                            try:
                                import json
                                data = json.loads(content)
                                desc = data.get('description', 'N/A')
                            except:
                                desc = content[:40] + '...' if len(content) > 40 else content
                        
                        if len(desc) > 40:
                            desc = desc[:37] + "..."
                        
                        table.add_row(
                            func_name,
                            platform,
                            f"{distance:.3f}",
                            desc
                        )
                    
                    # Only show if there are SD-WAN results or if it's a significant search
                    if sdwan_results or len(results) > 10:
                        console.print(f"\n[dim]ChromaDB: Found {len(results)} results, showing top {len(display_results)}[/dim]")
                        console.print(table)
            except Exception:
                # Don't break if there's an error
                pass
        
        return results
