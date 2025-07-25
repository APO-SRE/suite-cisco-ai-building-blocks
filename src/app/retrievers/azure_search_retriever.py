#! /usr/bin/env python3
from __future__ import annotations
################################################################################
# src/app/retrievers/azure_search_retriever.py
# Copyright (c) 2025 Jeff Teeter, Ph.D. – Cisco Systems, Inc.
# Apache-2.0  (see LICENSE) – Provided “AS IS”, no warranties.
################################################################################
"""
Domain-first retriever for **Azure AI Search** (formerly Cognitive Search).

Environment variables (layer-aware – replace <LAYER> with FASTAPI / DOMAIN / …):

    <LAYER>_AZURE_ENDPOINT             https://<svc>.search.windows.net
    <LAYER>_AZURE_KEY                  <admin-key-or-query-key>
    <LAYER>_AZURE_API_VERSION          2024-11-01-preview  (default)

    # Index names
    <LAYER>_AZURE_DOMAIN_INDEX         domain-index            (required)
    <LAYER>_AZURE_PLATFORM_INDEX       function-definitions-index
    <LAYER>_AZURE_API_DOCS_INDEX       api-docs-index
    <LAYER>_AZURE_EVENTS_INDEX         events-index

    # Embedding creds (Azure OpenAI)
    <LAYER>_AZURE_OPENAI_ENDPOINT
    <LAYER>_AZURE_OPENAI_KEY
    <LAYER>_AZURE_OPENAI_EMBEDDING_DEPLOYMENT
"""

import logging
import re
import json
from typing import Dict, List, Optional

import requests

from app.config import cfg
from concurrent.futures import ThreadPoolExecutor, as_completed
from . import default_pool_size
_logger = logging.getLogger(__name__)


def _sanitize_filename(text: str, max_len: int = 100) -> str:  # noqa: D401
    """Remove nasty chars so Windows/macOS don’t choke if files ever get saved."""
    return re.sub(r"[\\/:*?\"<>|]", "_", text)[:max_len].rstrip()


class AzureSearchRetriever:
    """Lightweight wrapper around the *vector + semantic* hybrid query API."""

    def __init__(self, *, layer: str | None = None, top_k: int | None = None):
        self.layer = (layer or cfg("ACTIVE_LAYER", default="FASTAPI")).upper()

        # ------------------------------------------------------------------ #
        # Connection & auth
        # ------------------------------------------------------------------ #
        self.search_endpoint = cfg("AZURE_ENDPOINT", layer=self.layer)
        self.search_key = cfg("AZURE_KEY", layer=self.layer)
        self.api_version = cfg(
            "AZURE_API_VERSION", layer=self.layer, default="2024-11-01-preview"
        )

        if not (self.search_endpoint and self.search_key):
            raise RuntimeError(
                f"[{self.layer}] Missing AZURE_ENDPOINT or AZURE_KEY – check your .env"
            )

        # ------------------------------------------------------------------ #
        # Index names
        # ------------------------------------------------------------------ #
        self.domain_index = cfg(
            "AZURE_DOMAIN_INDEX", layer=self.layer, default="domain-index"
        )
        self.platform_summaries_index = cfg(
            "AZURE_PLATFORM_INDEX", layer=self.layer, default="function-definitions-index"
        )
        self.api_docs_index = cfg("AZURE_API_DOCS_INDEX", layer=self.layer, default="")
        self.events_index = cfg("AZURE_EVENTS_INDEX", layer=self.layer, default="")

        # ------------------------------------------------------------------ #
        # Embedding (Azure OpenAI)
        # ------------------------------------------------------------------ #
        self.openai_endpoint = cfg("AZURE_OPENAI_ENDPOINT", layer=self.layer)
        self.openai_key = cfg("AZURE_OPENAI_KEY", layer=self.layer)
        self.embedding_deployment = cfg("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", layer=self.layer)
        self.openai_api_version = cfg(
            "AZURE_OPENAI_API_VERSION", layer=self.layer, default="2023-05-15"
        )

        if not all((self.openai_endpoint, self.openai_key, self.embedding_deployment)):
            raise RuntimeError(
                f"[{self.layer}] Missing Azure OpenAI embedding creds – "
                "AZURE_OPENAI_ENDPOINT / AZURE_OPENAI_KEY / AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
            )

        # Misc
        self.vector_field = cfg(
            "AZURE_VECTOR_COLUMNS", layer=self.layer, default="embedding"
        )
        self.top_k = int(
            top_k
            if top_k is not None
            else cfg("AZURE_TOP_K", layer=self.layer, cast=int, default=5)
        )
        # ────────────── concurrent-embed pool size ────────────────
        self.pool_size = default_pool_size(self.layer, "azure", fallback=4)
        # One informative line at construction time
        print(
            f"[{self.layer}/AzureRetriever]  ⚙  embed-workers = {self.pool_size}",
            flush=True,
        )

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #
    def _embed(self, text: str) -> List[float]:
        body = {
            "input": text,                 # single string is fine
            "encoding_format": "float",    # <-- THE important line
            # "dimensions": 1536           # only if you want to shorten vectors
    }
        url = (
            f"{self.openai_endpoint}/openai/deployments/"
            f"{self.embedding_deployment}/embeddings"
            f"?api-version={self.openai_api_version}"
        )
        resp = requests.post(
            url,
            headers={"api-key": self.openai_key, "Content-Type": "application/json"},
            json=body,
            timeout=30,
        )
        if resp.status_code >= 400:
            print("Azure returned:", resp.text)   
        resp.raise_for_status()
        return resp.json()["data"][0]["embedding"]

    def _query(self, index: str, payload: Dict) -> List[Dict]:
        url = (
            f"{self.search_endpoint}/indexes('{index}')/docs/search"
            f"?api-version={self.api_version}"
        )
        try:
            resp = requests.post(
                url,
                headers={"api-key": self.search_key, "Content-Type": "application/json"},
                json=payload,
                timeout=60,
            )
            resp.raise_for_status()
            return resp.json().get("value", [])
        except requests.RequestException as exc:  # noqa: BLE001
            _logger.error("Azure AI Search error on %s → %s", index, exc)
            if exc.response is not None:
                _logger.error("Response text: %s", exc.response.text)
            return []
        
    def _embed_many(self, queries: list[str]) -> list[list[float]]:
        """
        Parallel embeds with `self.pool_size` workers.
        """
        with ThreadPoolExecutor(max_workers=self.pool_size) as pool:
            futs = {pool.submit(self._embed, q): i for i, q in enumerate(queries)}
            vecs = [None] * len(queries)                         # pre-allocate
            for fut in as_completed(futs):
                vecs[futs[fut]] = fut.result()
        return vecs

    # ------------------------------------------------------------------ #
    # Public retrieval methods
    # ------------------------------------------------------------------ #
    def retrieve_domain_info(self, query: str) -> List[Dict]:
        vec = self._embed(query)
        payload = {
            "search": query,
            "queryType": "semantic",
            "semanticConfiguration": "domain-index-semantic-config",
            "top": self.top_k,
            "vectorQueries": [
                {
                    "kind": "vector",
                    "fields": self.vector_field,
                    "vector": vec,
                    "k": self.top_k,
                }
            ],
            "select": "id,content,metadata",
        }
        return self._query(self.domain_index, payload)

    def retrieve_platform_summaries(self, query: str) -> List[Dict]:
        """
        Search the *function-definitions* index.  Behaviour can be tuned with
        two env-vars:

        • FASTAPI_AZURE_PLATFORM_SEMCONF   » name of the semantic-config
          (set it **empty** to disable semantic ranking).
        • FASTAPI_AZURE_PLATFORM_SELECT    » comma-sep list of fields to return
          (must exist in the index doc-schema).
        """
        if not self.platform_summaries_index:
            return []

        semconf = cfg(
            "AZURE_PLATFORM_SEMCONF",
            layer=self.layer,
            default="platform-summaries-semantic-config",
        )
        select = cfg(
            "AZURE_PLATFORM_SELECT",
            layer=self.layer,
            default="platform,name,content",     # no doc_type by default
        )

        vec = self._embed(query)
        payload: Dict = {
            "search": query,
            "top": self.top_k,
            "vectorQueries": [
                {
                    "kind": "vector",
                    "fields": self.vector_field,
                    "vector": vec,
                    "k": self.top_k,
                }
            ],
            "select": select,
        }
        if semconf:
            payload.update(
                {
                    "queryType": "semantic",
                    "semanticConfiguration": semconf,
                }
            )

                # Get the flat results from the Azure API
        hits = self._query(self.platform_summaries_index, payload)

        # Re-hydrate the results into the nested structure the application expects
        rehydrated_functions = []
        for hit in hits:
            try:
                # 1. Parse the clean function definition from the 'content' field.
                content_str = hit.get('content', '{}')
                func_def = json.loads(content_str)

                # 2. Create the metadata dictionary from the other top-level fields.
                db_meta = {
                    'platform': hit.get('platform'),
                    'name': hit.get('name'),
                    'search_score': hit.get('@search.score')
                }
                
                # 3. CRITICAL STEP: Attach the metadata to the function object.
                func_def['metadata'] = db_meta
                
                rehydrated_functions.append(func_def)
            except (json.JSONDecodeError, TypeError) as e:
                _logger.error(f"Error processing Azure result: {e}. Hit: {hit}")
                continue
        
        return rehydrated_functions


 

    def retrieve_event_info(self, query: str, event_type: Optional[str] = None) -> List[Dict]:
        if not self.events_index:
            return []
        vec = self._embed(query)
        payload = {
            "search": query,
            "queryType": "semantic",
            "semanticConfiguration": "events-semantic-config",
            "top": self.top_k,
            "vectorQueries": [
                {
                    "kind": "vector",
                    "fields": self.vector_field,
                    "vector": vec,
                    "k": self.top_k,
                }
            ],
            "select": "event_id,event_name,event_type,content,additional_info",
        }
        if event_type:
            payload["filter"] = f"event_type eq '{event_type}'"
        return self._query(self.events_index, payload)

 
    # ------------------------------------------------------------------ #
    # Generic vector query – API-compatible with ChromaRetriever
    # ------------------------------------------------------------------ #
    def query(
        self,
        text: str,
        *,
        k: int = 128,
        filter: Optional[dict] = None,
    ) -> List[Dict]:
        """
        Wrapper used by dynamic.build_functions_for_llm().
        Just redirect to the trusted retrieve_platform_summaries().
        """
        # honour the simple platform filter, if present
        if filter and "platform" in filter:
            clause = filter["platform"]
            if isinstance(clause, dict) and "$in" in clause:
                platforms = clause["$in"]
                if platforms and self.platform_summaries_index:
                    # form Azure $filter clause
                    self._extra_filter = " or ".join(
                        [f"platform eq '{p}'" for p in platforms]
                    )
        else:
            self._extra_filter = None

        # call the original method (it already embeds + does semantic search)
        hits = self.retrieve_platform_summaries(text)

        # keep only top-k (retrieve_platform_summaries already uses self.top_k,
        # but dynamic.py may pass k < self.top_k)
        return hits[:k]