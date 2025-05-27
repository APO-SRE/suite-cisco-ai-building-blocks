#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/indexers/azure_indexer.py
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
import os, json, re, base64
from dotenv import load_dotenv

from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchableField,
    SearchField,
    ComplexField,
    SearchFieldDataType,
    VectorSearch,
    VectorSearchProfile,
    HnswParameters,
    SemanticConfiguration,
    SemanticPrioritizedFields,
    SemanticField,
    SemanticSearch,
    CorsOptions
)
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
from ..utils.embedding import embed_text
from concurrent.futures import ThreadPoolExecutor, as_completed

CPU_WORKERS = int(os.getenv("FASTAPI_AZURE_NUM_CPUS", "4") or 4)
# show thread-pool size and default batch size once
DEFAULT_BATCH = int(os.getenv("FASTAPI_AZURE_BATCH", "500") or 500)
print(
    f"[AzureIndexer]  ⚙  embedding threads = {CPU_WORKERS}  |  "
    f"default batch-upload = {DEFAULT_BATCH}",
    flush=True,
)

from .base_indexer import BaseIndexer
_already_finalised: set[str] = set()

load_dotenv()

class AzureIndexer(BaseIndexer):
    def __init__(self, index_name: str, layer_name: str = ""):
        super().__init__(index_name)
        # store layer key for use in other methods
        self.layer_key = layer_name.upper().strip() if layer_name else ""
        self.docs_index_name = os.getenv(f"{self.layer_key}_AZURE_DOCS_INDEX")
        self.platform_index_name = os.getenv(f"{self.layer_key}_AZURE_PLATFORM_INDEX")

        endpoint = os.getenv(f"{self.layer_key}_AZURE_ENDPOINT")
        key = os.getenv(f"{self.layer_key}_AZURE_KEY")
        api_ver = os.getenv(f"{self.layer_key}_AZURE_API_VERSION", "2024-07-01")
        if not endpoint or not key:
            raise ValueError(f"Missing AI Azure Search endpoint/key for layer '{layer_name}'")

        self.endpoint = endpoint
        self.key = key
        self.api_version = api_ver

        # interactive recreate logic
        raw_local = os.getenv(f"{self.layer_key}_AZURE_RECREATE_INDEX", None)
        raw_global = os.getenv("AZURE_RECREATE_INDEX", None)
        raw = raw_local if raw_local is not None else raw_global
        self.recreate_index = None if raw is None or raw.strip() == "" else raw.lower() == "true"

        print(f"[AzureIndexer] Layer='{layer_name}', Endpoint={endpoint}, IndexName={index_name}, Recreate? {self.recreate_index}")

        self.credential = AzureKeyCredential(self.key)
        self.index_client = SearchIndexClient(
            endpoint=self.endpoint,
            credential=self.credential,
            api_version=self.api_version
        )
        self.search_client = None

    # ────────────────────────────────────────────────────────────────
    #  Index bootstrap  — delete-once-per-run logic
    # ────────────────────────────────────────────────────────────────
    def create_index(self, recreate: bool | None = None):
        """
        • If self.recreate_index is *True* we delete the index **only once per
          process** (tracked in the _already_recreated set).
        • If it is *False* we always append.
        • If it is *None* we prompt the user exactly once; subsequent calls
          reuse the remembered choice without asking again.
        """
        global _already_finalised   # use the module-level guard

        # ── 0️⃣  fast-path: decision already made in this process ──────
        if self.index_name in _already_finalised:
            # we have already *created* or *kept* the index in this run
            self.recreate_index = False          # always append
            recreate            = False          # caller override ignored
            print(
                f"[AzureIndexer] add → '{self.index_name}' (decision cached)",
                flush=True,
            )

             
        # allow caller to override the env-derived value
        if recreate is not None:
            self.recreate_index = recreate

        # ── does the index exist? ────────────────────────────────────
        print(f"[AzureIndexer] Checking if index '{self.index_name}' exists…")
        try:
            existing = self.index_client.get_index(self.index_name)
            print(f"[AzureIndexer] Index '{self.index_name}' found.")
        except ResourceNotFoundError:
            existing = None
            print(f"[AzureIndexer] Index '{self.index_name}' does not exist.")
        except HttpResponseError as exc:
            print(f"[AzureIndexer] Error checking index: {exc}")
            raise

        # ── ask the question only if we still don’t know what to do ──
        if existing is not None and self.recreate_index is None:
            resp = input(
                f"Index '{self.index_name}' already exists. (R)ecreate or "
                "(A)ppend? [R/a]: "
            ).strip().lower()
            self.recreate_index = resp.startswith("r")

        # ── delete once per run if requested ────────────────────────
 


        if existing and self.recreate_index:
            print(
                f"[AzureIndexer] recreate_index=True → deleting "
                f"'{self.index_name}'…"
            )
            self.index_client.delete_index(self.index_name)
            existing = None
 

        # ── create if missing (either new or just deleted) ──────────
        if existing is None:
            schema = self.build_index_schema(self.index_name)
            self.index_client.create_index(schema)
            print(f"[AzureIndexer] Created new index '{self.index_name}'")
            # remember the decision so next platforms just append
            _already_finalised.add(self.index_name)
            self.recreate_index = False          # subsequent calls append
        else:
            print(f"[AzureIndexer] Reusing existing index '{self.index_name}'")
            _already_finalised.add(self.index_name)   # mark as handled

        # ── finally set up the SearchClient for uploads ─────────────
        self.search_client = SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=self.credential,
            api_version=self.api_version,
            logging_enable=True,
        )


    # ────────────────────────────────────────────────
    #  Schema factory
    # ────────────────────────────────────────────────
    def build_index_schema(self, index_name: str) -> SearchIndex:
        # read embedding dimension from env or default
        dim_env = os.getenv(f"{self.layer_key}_AZURE_DIM") or os.getenv("AZURE_DIM")
        try:
            EMBEDDING_DIM = int(dim_env)
        except (TypeError, ValueError):
            EMBEDDING_DIM = 1536

        # normalize for comparison
        idx = index_name.lower()
        docs_idx = (self.docs_index_name or "").lower()
        plat_idx = (self.platform_index_name or "").lower()


        if idx == "function-definitions-index":
            fields = [
                SearchableField(
                    name="id", type=SearchFieldDataType.String,
                    key=True, filterable=True, searchable=True
                ),
                SearchableField(
                    name="platform", type=SearchFieldDataType.String,
                    filterable=True, searchable=True, facetable=True
                ),
                SearchableField(
                    name="name", type=SearchFieldDataType.String,
                    filterable=True, searchable=True
                ),
                SearchableField(
                    name="content", type=SearchFieldDataType.String,
                    searchable=True
                ),
                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True,
                    filterable=False,
                    sortable=False,
                    facetable=False,
                    vector_search_dimensions=EMBEDDING_DIM,
                    vector_search_profile_name="fnDefHnswProfile",
                ),
            ]

            semantic_config = SemanticConfiguration(
                name="fnDefSemanticConfig",
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=SemanticField(field_name="name"),
                    content_fields=[SemanticField(field_name="content")],
                    keywords_fields=[SemanticField(field_name="platform")],
                ),
            )
            vector_search = VectorSearch(
                algorithms=[
                    {
                        "name": "fnDefHnsw",
                        "kind": "hnsw",
                        "parameters": HnswParameters(
                            m=4,
                            ef_construction=400,
                            ef_search=500,
                            metric="cosine"
                        )
                    }
                ],
                profiles=[
                    VectorSearchProfile(
                        name="fnDefHnswProfile",
                        algorithm_configuration_name="fnDefHnsw"
                    )
                ]
            )


            cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

            return SearchIndex(
                name=index_name,
                fields=fields,
                vector_search=vector_search,
                semantic_search=SemanticSearch(configurations=[semantic_config]),
                cors_options=cors_options,
            )

################################################################################
# In azure_indexer.py -> AzureIndexer.build_index_schema()
################################################################################

        if index_name.startswith("domain-"):
            fields = [
                SearchableField(
                    name="id",
                    type=SearchFieldDataType.String,
                    key=True,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="content",
                    type=SearchFieldDataType.String,
                    searchable=True
                ),
                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True,
                    filterable=False,
                    sortable=False,
                    facetable=False,
                    vector_search_dimensions=EMBEDDING_DIM,
                    vector_search_profile_name="domainHnswProfile"   # Referencing the profile name below
                ),
                SearchableField(
                    name="metadata",
                    type=SearchFieldDataType.String,
                    searchable=True,
                    filterable=False
                )
            ]

            semantic_config_name = f"{index_name}-semantic-config"
            semantic_config = SemanticConfiguration(
                name=semantic_config_name,
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=None,
                    content_fields=[SemanticField(field_name="content")],
                    keywords_fields=[]
                )
            )

            # Notice we rename both the "name" and the "algorithm_configuration_name"
            # to "domainHnsw", so they match exactly.
            vector_search = VectorSearch(
                algorithms=[
                    {
                        "name": "domainHnsw",    # must match algorithm_configuration_name
                        "kind": "hnsw",
                        "parameters": HnswParameters(
                            m=4,
                            ef_construction=400,
                            ef_search=500,
                            metric="cosine"
                        )
                    }
                ],
                profiles=[
                    VectorSearchProfile(
                        name="domainHnswProfile",                # used by the field
                        algorithm_configuration_name="domainHnsw" # must match algorithms[].name
                    )
                ]
            )

            cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

            return SearchIndex(
                name=index_name,
                fields=fields,
                vector_search=vector_search,
                semantic_search=SemanticSearch(configurations=[semantic_config]),
                cors_options=cors_options
            )


        # events-index
        elif index_name == "events-index":
            fields = [
                SearchableField(
                    name="id",
                    type=SearchFieldDataType.String,
                    key=True,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="event_id",
                    type=SearchFieldDataType.String,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="event_name",
                    type=SearchFieldDataType.String,
                    searchable=True
                ),
                SearchableField(
                    name="event_type",
                    type=SearchFieldDataType.String,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="content",
                    type=SearchFieldDataType.String,
                    searchable=True
                ),
                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True,
                    filterable=False,
                    sortable=False,
                    facetable=False,
                    vector_search_dimensions=EMBEDDING_DIM,
                    vector_search_profile_name="myHnswProfile"
                ),
                ComplexField(
                    name="additional_info",
                    fields=[
                        SearchableField(
                            name="zone_id",
                            type=SearchFieldDataType.String,
                            filterable=True,
                            searchable=True
                        ),
                        SearchField(
                            name="timestamp",
                            type=SearchFieldDataType.DateTimeOffset,
                            filterable=True,
                            sortable=True,
                            facetable=False
                        ),
                        SearchableField(
                            name="camera_id",
                            type=SearchFieldDataType.String,
                            filterable=True,
                            searchable=True
                        ),
                        SearchableField(
                            name="building",
                            type=SearchFieldDataType.String,
                            filterable=True,
                            searchable=True
                        ),
                        SearchableField(
                            name="floor",
                            type=SearchFieldDataType.String,
                            filterable=True,
                            searchable=True
                        ),
                        SearchableField(
                            name="location",
                            type=SearchFieldDataType.String,
                            filterable=True,
                            searchable=True
                        ),
                        SearchableField(
                            name="cisco_ai",
                            type=SearchFieldDataType.String,
                            filterable=True,
                            searchable=True
                        ),
                        SearchField(
                            name="recommended_actions",
                            type=SearchFieldDataType.Collection(SearchFieldDataType.String),
                            searchable=True,
                            filterable=False,
                            sortable=False,
                            facetable=False
                        ),
                        SearchField(
                            name="urls_for_further_action",
                            type=SearchFieldDataType.Collection(SearchFieldDataType.String),
                            searchable=True,
                            filterable=False,
                            sortable=False,
                            facetable=False
                        ),
                        SearchField(
                            name="extra_notes",
                            type=SearchFieldDataType.Collection(SearchFieldDataType.String),
                            searchable=True,
                            filterable=False,
                            sortable=False,
                            facetable=False
                        )
                    ]
                )
            ]

            semantic_config = SemanticConfiguration(
                name="myEventsSemanticConfig",
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=SemanticField(field_name="event_name"),
                    content_fields=[SemanticField(field_name="content")],
                    keywords_fields=[
                        SemanticField(field_name="event_type"),
                        SemanticField(field_name="event_id")
                    ]
                )
            )

            vector_search = VectorSearch(
                algorithms=[
                    {
                        "name": "myHnsw",
                        "kind": "hnsw",
                        "parameters": HnswParameters(
                            m=4,
                            ef_construction=400,
                            ef_search=500,
                            metric="cosine"
                        )
                    }
                ],
                profiles=[
                    VectorSearchProfile(
                        name="myHnswProfile",
                        algorithm_configuration_name="myHnsw"
                    )
                ]
            )

            cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

            return SearchIndex(
                name=index_name,
                fields=fields,
                vector_search=vector_search,
                semantic_search=SemanticSearch(configurations=[semantic_config]),
                cors_options=cors_options
            )

 
        elif idx == docs_idx:
          
            fields = [
                SearchableField(name="id", type=SearchFieldDataType.String, key=True, filterable=True, searchable=True),
                SearchableField(name="title", type=SearchFieldDataType.String, searchable=True),
                SearchableField(name="content", type=SearchFieldDataType.String, searchable=True),
                SearchableField(name="platform", type=SearchFieldDataType.String, filterable=True, searchable=True),
                SearchableField(name="doc_type", type=SearchFieldDataType.String, filterable=True, searchable=True),
                #SearchableField(name="summary", type=SearchFieldDataType.String, searchable=True, filterable=False),
                #SearchableField(name="keywords", type=SearchFieldDataType.String, searchable=True, filterable=False),
                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True,
                    vector_search_dimensions=EMBEDDING_DIM,
                    vector_search_profile_name="apiDocsHnswProfile"
                )
            ]

            semantic_config = SemanticConfiguration(
                name="apiDocsSemanticConfig",
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=SemanticField(field_name="title"),
                    content_fields=[SemanticField(field_name="content")],
                    keywords_fields=[SemanticField(field_name="platform")]
                )
            )

            vector_search = VectorSearch(
                algorithms=[{
                    "name": "apiDocsHnsw",
                    "kind": "hnsw",
                    "parameters": HnswParameters(m=4, ef_construction=400, ef_search=500, metric="cosine")
                }],
                profiles=[VectorSearchProfile(name="apiDocsHnswProfile", algorithm_configuration_name="apiDocsHnsw")]
            )

            cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

            return SearchIndex(
                name=index_name,
                fields=fields,
                vector_search=vector_search,
                semantic_search=SemanticSearch(configurations=[semantic_config]),
                cors_options=cors_options
            )

        
        elif idx == plat_idx:

            fields = [
                SearchableField(
                    name="id",
                    type=SearchFieldDataType.String,
                    key=True,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="platform",
                    type=SearchFieldDataType.String,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="doc_type",
                    type=SearchFieldDataType.String,
                    filterable=True,
                    searchable=True
                ),
                SearchableField(
                    name="content",
                    type=SearchFieldDataType.String,
                    searchable=True
                ),
                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True,
                    filterable=False,
                    sortable=False,
                    facetable=False,
                    vector_search_dimensions=EMBEDDING_DIM,
                    vector_search_profile_name="platformHnswProfile"
                )
            ]

            semantic_config = SemanticConfiguration(
                name="platformSummariesSemanticConfig",
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=None,
                    content_fields=[SemanticField(field_name="content")],
                    keywords_fields=[
                        SemanticField(field_name="platform"),
                        SemanticField(field_name="doc_type")
                    ]
                )
            )

            vector_search = VectorSearch(
                algorithms=[{
                    "name": "platformHnsw",
                    "kind": "hnsw",
                    "parameters": HnswParameters(
                        m=4, ef_construction=400, ef_search=500, metric="cosine"
                    )
                }],
                profiles=[VectorSearchProfile(
                    name="platformHnswProfile",
                    algorithm_configuration_name="platformHnsw"
                )]
            )

            cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)

            return SearchIndex(
                name=index_name,
                fields=fields,
                vector_search=vector_search,
                semantic_search=SemanticSearch(configurations=[semantic_config]),
                cors_options=cors_options
            )

        else:
            # if you hit here, you’ll immediately get a clear error instead of None
            raise ValueError(f"[AzureIndexer] No schema defined for index '{index_name}'")
        

    def index_documents(self, docs: list, batch_size: int = 500):
        if not self.search_client:
            self.search_client = SearchClient(
                endpoint=self.endpoint,
                index_name=self.index_name,
                credential=self.credential,
                api_version=self.api_version,
                logging_enable=True
            )

        total = len(docs)

        print(
            f"[AzureIndexer]  ⚙  upload thread-pool = "
            f"{min(4, (total + batch_size - 1)//batch_size)}  |  "
            f"batch size = {batch_size}",
            flush=True,
        )
        def _push(batch):
            return self.search_client.upload_documents(documents=batch)

        batches = [docs[i : i + batch_size] for i in range(0, total, batch_size)]
        with ThreadPoolExecutor(max_workers=min(4, len(batches))) as pool:
            futs = {pool.submit(_push, b): idx for idx, b in enumerate(batches, 1)}
            for fut in as_completed(futs):
                idx = futs[fut]
                try:
                    fut.result()
                    print(f"[AzureIndexer] ✓ batch {idx}/{len(batches)}", flush=True)
                except Exception as exc:        # noqa: BLE001
                    print(f"[AzureIndexer] ✗ batch {idx} – {exc}", flush=True)
        print(f"[AzureIndexer] All {total} documents uploaded.")



class PlatformFunctionIndexer(AzureIndexer):
    SAFE_KEY_CHARS = re.compile(r"[^A-Za-z0-9_\-=]")

    @staticmethod
    def _safe_key(text: str) -> str:
        """
        Return a key that satisfies Azure Search rules:
        • only A-Z a-z 0-9 _ - =
        • length ≤ 500 (Azure limit is 1024, we keep head-room)
        """
        cleaned = PlatformFunctionIndexer.SAFE_KEY_CHARS.sub("_", text)
        if len(cleaned) <= 500:
            return cleaned
        # fallback: URL-safe base64, then trim to 500 chars
        return base64.urlsafe_b64encode(text.encode()).decode()[:500]

    def index_functions(
        self,
        platform: str,
        diet_list: list[dict],
        full_spec: dict,   # kept for parity
    ):
 
        # ── 1️⃣ ensure the index exists ──────────────────────────────
        self.create_index()

        # ── 2️⃣ build docs with a mini progress counter ──────────────
        total = len(diet_list)

        print(
            f"[{platform}] embedding {total} functions "
            f"with {CPU_WORKERS} thread(s)…",
            flush=True,
        )
        def _prepare(fn: dict) -> dict:
            key = self._safe_key(f"{platform}-{fn['name']}")
            vec = fn.get("embedding") or embed_text(fn["name"])[0]
            return {
                "id":       key,
                "platform": platform,
                "name":     fn["name"],
                "content":  json.dumps(fn),
                "embedding": vec,
            }

        docs: list[dict] = []
        with ThreadPoolExecutor(max_workers=CPU_WORKERS) as pool:
            for i, fut in enumerate(
                as_completed(pool.submit(_prepare, f) for f in diet_list), start=1
            ):
                docs.append(fut.result())
                if i % 100 == 0 or i == total:
                    print(f"   • processed {i}/{total}", flush=True)



        # ── 3️⃣ upload the batch ────────────────────────────────────────
        self.index_documents(docs)        
   


        



