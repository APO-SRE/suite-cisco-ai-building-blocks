#! /usr/bin/env python3
from __future__ import annotations
################################################################################
# ai-building-blocks-agent/retrievers/azure_search_retriever.py
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
    <LAYER>_AZURE_PLATFORM_INDEX       platform-summaries-index
    <LAYER>_AZURE_API_DOCS_INDEX       api-docs-index
    <LAYER>_AZURE_EVENTS_INDEX         events-index

    # Embedding creds (Azure OpenAI)
    <LAYER>_AZURE_OPENAI_ENDPOINT
    <LAYER>_AZURE_OPENAI_KEY
    <LAYER>_AZURE_EMBEDDING_DEPLOYMENT
"""

import logging
import re
from typing import Dict, List, Optional

import requests

from app.config import cfg

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
            "AZURE_PLATFORM_INDEX", layer=self.layer, default=""
        )
        self.api_docs_index = cfg("AZURE_API_DOCS_INDEX", layer=self.layer, default="")
        self.events_index = cfg("AZURE_EVENTS_INDEX", layer=self.layer, default="")

        # ------------------------------------------------------------------ #
        # Embedding (Azure OpenAI)
        # ------------------------------------------------------------------ #
        self.openai_endpoint = cfg("AZURE_OPENAI_ENDPOINT", layer=self.layer)
        self.openai_key = cfg("AZURE_OPENAI_KEY", layer=self.layer)
        self.embedding_deployment = cfg("AZURE_EMBEDDING_DEPLOYMENT", layer=self.layer)
        self.openai_api_version = cfg(
            "AZURE_OPENAI_API_VERSION", layer=self.layer, default="2023-05-15"
        )

        if not all((self.openai_endpoint, self.openai_key, self.embedding_deployment)):
            raise RuntimeError(
                f"[{self.layer}] Missing Azure OpenAI embedding creds – "
                "AZURE_OPENAI_ENDPOINT / AZURE_OPENAI_KEY / AZURE_EMBEDDING_DEPLOYMENT"
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

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #
    def _embed(self, text: str) -> List[float]:
        url = (
            f"{self.openai_endpoint}/openai/deployments/"
            f"{self.embedding_deployment}/embeddings"
            f"?api-version={self.openai_api_version}"
        )
        resp = requests.post(
            url,
            headers={"api-key": self.openai_key, "Content-Type": "application/json"},
            json={"input": [text]},
            timeout=30,
        )
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
        if not self.platform_summaries_index:
            return []
        vec = self._embed(query)
        payload = {
            "search": query,
            "queryType": "semantic",
            "semanticConfiguration": "platform-summaries-semantic-config",
            "top": self.top_k,
            "vectorQueries": [
                {
                    "kind": "vector",
                    "fields": self.vector_field,
                    "vector": vec,
                    "k": self.top_k,
                }
            ],
            "select": "platform,doc_type,content",
        }
        return self._query(self.platform_summaries_index, payload)

    def retrieve_api_docs(self, query: str, platforms: Optional[List[str]] = None) -> List[Dict]:
        if not self.api_docs_index:
            return []
        vec = self._embed(query)
        payload = {
            "search": query,
            "queryType": "semantic",
            "semanticConfiguration": "api-docs-semantic-config",
            "top": self.top_k,
            "vectorQueries": [
                {
                    "kind": "vector",
                    "fields": self.vector_field,
                    "vector": vec,
                    "k": self.top_k,
                }
            ],
            "select": "title,content,platform,doc_type",
        }
        if platforms:
            payload["filter"] = " or ".join([f"platform eq '{p}'" for p in platforms])
        return self._query(self.api_docs_index, payload)

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
