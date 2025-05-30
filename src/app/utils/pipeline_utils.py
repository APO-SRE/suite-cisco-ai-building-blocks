#!/usr/bin/env python3
################################################################################
## suite-cisco-ai-building-blocks/src/app/utils/pipeline_utils.py
## Copyright (c) 2025 ...
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
#################################################################################
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

import os
import uuid
import shutil
import chromadb
from dotenv import load_dotenv
from chromadb.config import Settings
from typing import List, Union
import json
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
load_dotenv()

################################################################################
# Embedding providers (Azure-OpenAI, OpenAI, HuggingFace, Cohere)
################################################################################
class EmbeddingProviderBase:
    def embed(self, texts):
        raise NotImplementedError

class OpenAIEmbedding(EmbeddingProviderBase):
    def __init__(self, prefix):
        import openai
        key = os.getenv(f"{prefix}_OPENAI_API_KEY")
        if not key:
            raise RuntimeError(f"{prefix}_OPENAI_API_KEY not set")
        openai.api_key = key
        self.model = os.getenv(f"{prefix}_OPENAI_EMBEDDING_MODEL",
                               "text-embedding-ada-002")

    def embed(self, texts):
        import openai
        resp = openai.Embedding.create(input=texts, model=self.model)
        return [d["embedding"] for d in resp["data"]]

class AzureOpenAIEmbedding(EmbeddingProviderBase):
    def __init__(self, prefix):
        import openai
        api_key    = os.getenv(f"{prefix}_AZURE_OPENAI_KEY")
        endpoint   = os.getenv(f"{prefix}_AZURE_OPENAI_ENDPOINT")
        deployment = os.getenv(f"{prefix}_AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
        api_version= os.getenv(f"{prefix}_AZURE_OPENAI_API_VERSION", "2023-05-15")
        if not (api_key and endpoint and deployment):
            raise RuntimeError(
                f"[pipeline_utils] Azure OpenAI creds missing for {prefix}. "
                "Make sure you have set "
                f"{prefix}_AZURE_OPENAI_KEY, "
                f"{prefix}_AZURE_OPENAI_ENDPOINT, "
                f"{prefix}_AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
            )
        openai.api_type    = "azure"
        openai.api_base    = endpoint
        openai.api_version = api_version
        openai.api_key     = api_key
        self.deployment    = deployment

    def embed(self, texts):
        import openai
        resp = openai.Embedding.create(input=texts, engine=self.deployment)
        return [d["embedding"] for d in resp["data"]]

class HuggingFaceEmbedding(EmbeddingProviderBase):
    def __init__(self, prefix):
        from sentence_transformers import SentenceTransformer
        model = os.getenv(f"{prefix}_HUGGINGFACE_MODEL",
                          "sentence-transformers/all-MiniLM-L6-v2")
        self.model = SentenceTransformer(model)

    def embed(self, texts):
        arr = self.model.encode(texts, convert_to_numpy=True)
        return [v.tolist() for v in arr]

class CohereEmbedding(EmbeddingProviderBase):
    def __init__(self, prefix):
        import cohere
        key = os.getenv(f"{prefix}_COHERE_API_KEY")
        if not key:
            raise RuntimeError(f"{prefix}_COHERE_API_KEY not set")
        self.client = cohere.Client(key)
        self.model  = os.getenv(f"{prefix}_COHERE_EMBEDDING_MODEL", None)

    def embed(self, texts):
        if self.model:
            return self.client.embed(texts=texts, model=self.model).embeddings
        return self.client.embed(texts=texts).embeddings

def get_embedding_provider(name, prefix):
    n = name.strip().lower()
    if n in ("openai","openai-api"):     return OpenAIEmbedding(prefix)
    if n in ("azure","azure-openai"):    return AzureOpenAIEmbedding(prefix)
    if n in ("huggingface","hf","local"):return HuggingFaceEmbedding(prefix)
    if n == "cohere":                    return CohereEmbedding(prefix)
    raise ValueError(f"Unknown embedding provider '{name}'")

################################################################################
# Vector Indexers
################################################################################
class VectorIndexerBase:
    def index_batch(self, docs, embeddings): raise NotImplementedError

class AzureVectorIndexer(VectorIndexerBase):
    def __init__(self, prefix: str):
        endpoint  = os.getenv(f"{prefix}_AZURE_ENDPOINT")
        key       = os.getenv(f"{prefix}_AZURE_KEY")
        indexname = (
            os.getenv(f"{prefix}_AZURE_INDEX")
            or os.getenv(f"{prefix}_AZURE_PLATFORM_INDEX")
            or os.getenv(f"{prefix}_AZURE_DOCS_INDEX")
        )
        if not (endpoint and key and indexname):
            raise RuntimeError(f"Azure Search not configured for {prefix}")
        cred = AzureKeyCredential(key)
        self.client = SearchClient(endpoint, indexname, cred)
        self.field  = os.getenv(f"{prefix}_AZURE_VECTOR_COLUMNS", "embedding")


    def index_batch(self, docs: List[dict], embeddings: List[List[float]]) -> None:
        payload = []
        for doc, emb in zip(docs, embeddings):
            # base fields
            item = {
                "id":      doc.get("id", str(uuid.uuid4())),
                "content": doc.get("content", ""),
                self.field: emb
            }

            # flatten everything else:
            for k, v in doc.items():
                if k in ("id", "content"):
                    continue
                if k == "metadata":
                    # domain-index expects a string
                    item[k] = json.dumps(v)
                else:
                    # events-index (and others) expect dicts/lists as-is
                    item[k] = v

            payload.append(item)

        print(f"[AzureVectorIndexer] Uploading {len(payload)} docs to '{self.client._index_name}'")
        result = self.client.upload_documents(documents=payload)
        print(f"[AzureVectorIndexer] Upload result: {result}")

class ChromaVectorIndexer(VectorIndexerBase):
    """
    Uses the LAYER prefix to decide recreate behavior, and accepts
    either List[str] or List[dict] with metadata (or auto-extracts one).
    """
    def __init__(self, collection_name: str, layer_prefix: str):
        self.collection_name = collection_name
        self.layer_prefix    = layer_prefix

        base_db_path    = os.getenv(f"{layer_prefix}_CHROMA_DB_PATH", "./chroma_db")
        recreate_env    = os.getenv(f"{layer_prefix}_CHROMA_RECREATE_INDEX", "").strip().lower()
        self.db_path    = os.path.join(base_db_path, collection_name)

        print(f"[ChromaVectorIndexer] collection='{collection_name}', db_path='{self.db_path}'")

        already = os.path.isdir(self.db_path) and os.listdir(self.db_path)
        if already:
            print(f"[ChromaVectorIndexer] Found existing data in {self.db_path}")
            if recreate_env == "":
                ans = input(f"Collection '{collection_name}' found. (R)ecreate or (A)ppend? [R/a]: ").strip().lower()
                if ans.startswith("r"):
                    self._recreate()
            elif recreate_env == "true":
                self._recreate()
            else:
                print(f"[ChromaVectorIndexer] Appending (env said 'false').")
        else:
            print(f"[ChromaVectorIndexer] No existing data. Creating {self.db_path}…")
            os.makedirs(self.db_path, exist_ok=True)

        self.client     = chromadb.PersistentClient(
            path=self.db_path,
            settings=Settings(allow_reset=True, anonymized_telemetry=False)
        )
        self.collection = self.client.get_or_create_collection(collection_name)
        print(f"[ChromaVectorIndexer] Ready for docs in collection '{collection_name}'")

    def _recreate(self):
        print(f"[ChromaVectorIndexer] Recreating by removing {self.db_path}…")
        try:
            shutil.rmtree(self.db_path)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"[ChromaVectorIndexer] Warning: failed to remove {self.db_path}: {e}")
        os.makedirs(self.db_path, exist_ok=True)
        print(f"[ChromaVectorIndexer] Done. Fresh start at {self.db_path}.")

    def index_batch(
        self,
        docs: List[Union[str, dict]],
        embeddings: List[List[float]]
    ) -> None:
        if not docs or not embeddings:
            raise ValueError("Docs and embeddings cannot be empty")
        if len(docs) != len(embeddings):
            raise ValueError("Docs and embeddings must have the same length")

        # DICT CASE: grab id/content, auto-extract metadata if missing
        if isinstance(docs[0], dict):
            ids       = [doc.get("id", str(uuid.uuid4())) for doc in docs]
            contents  = [doc["content"]               for doc in docs]
            metadatas = []

            for doc in docs:
                # prefer an explicit metadata field…
                raw_meta = doc.get("metadata", None)
                if raw_meta is None:
                    # …otherwise pack every other key into metadata
                    raw_meta = { k: v for k, v in doc.items() if k not in ("id", "content") }

                # flatten any non-primitive values
                flat = {}
                for k, v in raw_meta.items():
                    if isinstance(v, (str, int, float, bool)):
                        flat[k] = v
                    else:
                        flat[k] = json.dumps(v)
                metadatas.append(flat)

            print(f"[ChromaVectorIndexer] Adding {len(ids)} docs with metadata to '{self.collection_name}'")
            self.collection.upsert(
                ids=ids,
                documents=contents,
                embeddings=embeddings,
                metadatas=metadatas
            )

        # STRING CASE: exactly as before
        else:
            ids = [str(uuid.uuid4()) for _ in docs]
            print(f"[ChromaVectorIndexer] Adding {len(ids)} plain docs to '{self.collection_name}'")
            self.collection.upsert(
                documents=docs,
                embeddings=embeddings,
                ids=ids
            )




class ElasticVectorIndexer(VectorIndexerBase):
    def __init__(self, prefix):
        from elasticsearch import Elasticsearch
        host = os.getenv(f"{prefix}_ELASTIC_HOST", "localhost:9200")
        user = os.getenv(f"{prefix}_ELASTIC_USER")
        pw   = os.getenv(f"{prefix}_ELASTIC_PASSWORD")
        self.client = Elasticsearch(hosts=[host], http_auth=(user,pw) if user else None)
        self.index  = os.getenv(f"{prefix}_ELASTIC_INDEX") or os.getenv(f"{prefix}_INDEX_NAME")

    def index_batch(self, docs, embeddings):
        from elasticsearch.helpers import bulk
        actions = [{
          "_index": self.index,
          "_id":    str(uuid.uuid4()),
          "_source": {"content": t, "vector": v}
        } for t,v in zip(docs, embeddings)]
        bulk(self.client, actions)

def get_vector_indexer(backend_name: str, layer_prefix: str):
    n = backend_name.strip().lower()
    if n == "azure":
        return AzureVectorIndexer(layer_prefix)
    elif n == "chroma":
        # read the actual collection name from e.g. "EVENTS_CHROMA_COLLECTION" 
        # or fallback to "EVENTS_CHROMA_INDEX"
        # or default to e.g. f"{layer_prefix.lower()}-index"
        col_name = (
            os.getenv(f"{layer_prefix}_CHROMA_COLLECTION")
            or os.getenv(f"{layer_prefix}_CHROMA_INDEX")
            or f"{layer_prefix.lower()}-index"
        )
        return ChromaVectorIndexer(col_name, layer_prefix)
    elif n in ("elastic","es"):
        return ElasticVectorIndexer(layer_prefix)
    else:
        raise ValueError(f"Unknown vector backend '{backend_name}'")

################################################################################
# The embedding + indexing pipeline 
################################################################################

def _worker(chunk: List[str], provider_name: str, backend_name: str, prefix: str):
    embedder = get_embedding_provider(provider_name, prefix)
    indexer  = get_vector_indexer(backend_name, prefix)

    batch_sz = int(os.getenv(f"{prefix}_EMBED_BATCH_SIZE", "64"))
    for i in range(0, len(chunk), batch_sz):
        batch = chunk[i : i + batch_sz]

        # if we received dicts, pull out the text for embedding…
        if isinstance(batch[0], dict):
            texts = [item["content"] for item in batch]
            docs  = batch
        else:
            texts = batch
            docs  = batch

        embeddings = embedder.embed(texts)
        indexer.index_batch(docs, embeddings)

def index_documents(docs: List[str], provider_name: str, backend_name: str, layer_prefix: str):
    if not docs:
        return

    num = int(os.getenv(f"{layer_prefix}_OMP_NUM_THREADS", "1"))
    # Force concurrency=1 for Chroma:
    if backend_name.lower() == "chroma":
        num = 1

    if num > 1:
        size = len(docs) // num or len(docs)
        chunks = [docs[i:i+size] for i in range(0, len(docs), size)]
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=num) as ex:
            for c in chunks:
                ex.submit(_worker, c, provider_name, backend_name, layer_prefix)
    else:
        _worker(docs, provider_name, backend_name, layer_prefix)