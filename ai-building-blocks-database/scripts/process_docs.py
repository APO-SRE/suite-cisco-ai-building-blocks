
#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/process_docs.py
## Copyright (c) 2025 Jeff Teeter
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
import os
import re
import json
import glob
import hashlib
import logging
from dotenv import load_dotenv

from scripts.utils.chunking import chunk_file
from scripts.utils import pipeline_utils

# 1) Load .env & configure logging
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("process_docs")

# 2) Hard-code your layer:
LAYER = "FASTAPI"

# 3) Read which vector backend & embedding provider we’re using
backend  = os.getenv(f"{LAYER}_VECTOR_BACKEND", "azure").lower()
provider = os.getenv(f"{LAYER}_EMBEDDING_PROVIDER", "azureopenai").lower()
logger.info(f"Layer={LAYER}, VECTOR_BACKEND={backend}, EMBEDDING_PROVIDER={provider}")

# 4) Figure out which environment-variable prefix to use for concurrency
#    (Azure => f"{LAYER}_AZURE_...", Chroma => f"{LAYER}_CHROMA_...", etc.)
_backend_prefix_map = {
    "azure":   "AZURE",
    "chroma":  "CHROMA",
    "elastic": "ELASTIC",
}
prefix_key = _backend_prefix_map.get(backend, "AZURE")

# 5) Pull concurrency from environment:
#    (fastapi_chroma_omp_num_threads, fastapi_chroma_mkl_num_threads, etc.)
omp_var  = os.getenv(f"{LAYER}_{prefix_key}_OMP_NUM_THREADS") or os.getenv("OMP_NUM_THREADS", "1")
mkl_var  = os.getenv(f"{LAYER}_{prefix_key}_MKL_NUM_THREADS") or os.getenv("MKL_NUM_THREADS", "1")
cpus_var = os.getenv(f"{LAYER}_{prefix_key}_NUM_CPUS")       or os.getenv("NUM_CPUS", "1")

logger.info(f"Threads: OMP_NUM_THREADS={omp_var}, MKL_NUM_THREADS={mkl_var}, NUM_CPUS={cpus_var}")

# 6) Apply them to the environment so that libraries pick them up
os.environ["OMP_NUM_THREADS"] = omp_var
os.environ["MKL_NUM_THREADS"] = mkl_var

# Also set {LAYER}_OMP_NUM_THREADS so pipeline_utils uses that for concurrency:
os.environ[f"{LAYER}_OMP_NUM_THREADS"] = cpus_var
logger.info(f"Set {LAYER}_OMP_NUM_THREADS={cpus_var} for pipeline parallelism")

################################################################################
# Helpers to clean text
################################################################################

def clean_markdown(md: str) -> str:
    md = re.sub(r"```.*?```", "", md, flags=re.S)          # remove triple backtick blocks
    md = re.sub(r"`([^`]+)`", r"\1", md)                   # remove inline backticks
    md = re.sub(r"^\s*#{1,6}\s*", "", md, flags=re.M)      # remove headings
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)         # remove HTML comments
    md = re.sub(r"\n{2,}", "\n\n", md)                     # condense blank lines
    return md.strip()

def openapi_to_text(spec: dict) -> str:
    """
    Convert an OpenAPI JSON spec into plain text for indexing.
    """
    lines = []
    info = spec.get("info", {})
    if info.get("title") or info.get("description"):
        lines.append(f"{info.get('title','')}: {info.get('description','')}")
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for m, op in methods.items():
            summary = op.get('summary','')
            lines.append(f"{m.upper()} {path} — {summary}")

            desc = op.get('description','')
            if desc:
                lines.append(desc)

            # handle parameters
            for p in op.get("parameters", []):
                name = p.get("name")
                ptype = p.get("schema", {}).get("type","")
                desc2 = p.get("description","")
                lines.append(f"Param {name} ({ptype}): {desc2}")

    return "\n".join(lines)


################################################################################
# 7) Gather chunks from your local files
################################################################################

# We'll store the chunked text in two lists:
platform_chunks = []
api_chunks = []

# Only gather if FASTAPI_VECTOR_ENABLED=true in .env
if os.getenv(f"{LAYER}_VECTOR_ENABLED", "false").lower() == "true":

    # -- Platform Summaries
    path = "platform_summaries/platform_summaries.json"
    if os.path.exists(path):
        logger.info("Loading platform summaries…")
        with open(path, encoding="utf-8") as f:
            items = json.load(f)

        size    = int(os.getenv(f"{LAYER}_AZURE_CHUNK_SIZE",    "2000"))  # can also handle CHROMA_ or ELASTIC_ if you wish
        overlap = int(os.getenv(f"{LAYER}_AZURE_CHUNK_OVERLAP", "100"))

        for item in items:
            text = (item.get("content") or "").strip()
            if not text:
                continue
            for chunk in chunk_file(text, size, overlap):
                stable_id = hashlib.sha1(chunk.encode("utf-8")).hexdigest()
                platform_chunks.append({
                    "id":       stable_id,
                    "content":  chunk,
                    "platform": item.get("platform", ""),
                    "doc_type": "summary",
                })

        logger.info(f"→ {len(platform_chunks)} platform-summary chunks queued")

    # -- API Docs
    size    = int(os.getenv(f"{LAYER}_AZURE_CHUNK_SIZE",    "2000"))
    overlap = int(os.getenv(f"{LAYER}_AZURE_CHUNK_OVERLAP", "100"))

    # Example platforms subfolders:
    platforms = ["catalyst_center","cisco_spaces","meraki","webex"]
    for plat in platforms:
        for (subdir, ext, cleaner) in [
            ("api-docs",  "*.md",   clean_markdown),
            ("api-specs", "*.json", openapi_to_text)
        ]:
            folder = os.path.join(plat, subdir)
            if not os.path.isdir(folder):
                continue
            for fp in glob.glob(os.path.join(folder, ext)):
                raw = open(fp, encoding="utf-8").read()
                if fp.endswith(".md"):
                    text  = cleaner(raw)
                    title = None
                else:
                    # JSON swagger/OpenAPI spec
                    spec  = json.loads(raw)
                    # pull the top‐level info.title
                    title = spec.get("info", {}).get("title", "")
                    text  = cleaner(spec)
                for chunk in chunk_file(text, size, overlap):
                    stable_id = hashlib.sha1(chunk.encode("utf-8")).hexdigest()

                    api_chunks.append({
                        "id":        stable_id,
                        "title":     title,
                        "content":   chunk,
                        "platform":  plat,
                        "doc_type":  "api-doc",
                    })


    logger.info(f"→ {len(api_chunks)} total API-docs chunks queued")
else:
    logger.info(f"{LAYER}_VECTOR_ENABLED is not true, skipping chunk collection.")


################################################################################
# 8) Indexing / Dispatch to appropriate backend
################################################################################
if backend == "azure":
    from scripts.indexers.azure_indexer import AzureIndexer
    
    # 1) If FASTAPI + Azure => Two distinct indexes
    if LAYER == "FASTAPI":
        plat_name = os.getenv("FASTAPI_AZURE_PLATFORM_INDEX")
        docs_name = os.getenv("FASTAPI_AZURE_DOCS_INDEX")

        logger.info(f"Ensuring platform index '{plat_name}'…")
        AzureIndexer(plat_name, layer_name=LAYER).create_index(recreate=None)

        logger.info(f"Ensuring docs index '{docs_name}'…")
        AzureIndexer(docs_name, layer_name=LAYER).create_index(recreate=None)

        # -- Index platform
        if platform_chunks:
            # Temporarily point AzureVectorIndexer to 'plat_name'
            os.environ[f"{LAYER}_AZURE_INDEX"] = plat_name 
            logger.info(f"Embedding + indexing {len(platform_chunks)} platform chunks → {plat_name}")
            pipeline_utils.index_documents(
            docs=platform_chunks,    
                provider_name=provider,
                backend_name=backend,
                layer_prefix=LAYER
            )

        # -- Index docs
        if api_chunks:
            os.environ[f"{LAYER}_AZURE_INDEX"] = docs_name
            logger.info(f"Embedding + indexing {len(api_chunks)} doc chunks → {docs_name}")
            pipeline_utils.index_documents(
                docs=api_chunks,        
                provider_name=provider,
                backend_name=backend,
                layer_prefix=LAYER
            )

    # 2) If e.g. AGENTIC + Azure => Single index
    else:
        single_name = os.getenv(f"{LAYER}_AZURE_INDEX")
        logger.info(f"Ensuring single index '{single_name}'…")
        AzureIndexer(single_name, layer_name=LAYER).create_index(recreate=None)

        # Merge your chunks or do them separately
        everything = platform_chunks + api_chunks
        if everything:
            os.environ[f"{LAYER}_AZURE_INDEX"] = single_name
            logger.info(f"Embedding + indexing {len(everything)} items → {single_name}")
            pipeline_utils.index_documents(
                docs=[c["content"] for c in everything],
                provider_name=provider,
                backend_name=backend,
                layer_prefix=LAYER
            )





elif backend in ("chroma","elastic"):
    # Let pipeline_utils handle chunk embedding + indexing in sub-batches
    def run_pipeline(chunks, index_name):
        if not chunks:
            return

        if backend == "chroma":
            # Tells pipeline_utils which Chroma collection to use
            os.environ[f"{LAYER}_CHROMA_COLLECTION"] = index_name
        else:
            # Tells pipeline_utils which Elastic index to use
            os.environ[f"{LAYER}_ELASTIC_INDEX"] = index_name

        texts = [c["content"] for c in chunks]
        logger.info(f"Embedding & indexing {len(texts)} docs into '{index_name}' via {backend}…")

        pipeline_utils.index_documents(
            docs=          texts,
            provider_name= provider,
            backend_name=  backend,
            layer_prefix=  LAYER
        )

    # Derive the index/collection name from the env
    if backend == "chroma":
        plat_idx_name = os.getenv(f"{LAYER}_CHROMA_COLLECTION_PLATFORM", "platform-summaries-index")
        docs_idx_name = os.getenv(f"{LAYER}_CHROMA_COLLECTION_DOCS",     "api-docs-index")
    else:
        plat_idx_name = os.getenv(f"{LAYER}_ELASTIC_DOCS_INDEX", "platform-summaries-index")
        docs_idx_name = os.getenv(f"{LAYER}_ELASTIC_PLATFORM_INDEX",     "api-docs-index")

    run_pipeline(platform_chunks, plat_idx_name)
    run_pipeline(api_chunks,      docs_idx_name)

else:
    # fallback: just embed everything in one go
    all_texts = [c["content"] for c in (platform_chunks + api_chunks)]
    if not all_texts:
        logger.info("No chunks found to index. Exiting.")
    else:
        logger.info(f"Embedding & indexing {len(all_texts)} chunks in parallel…")
        pipeline_utils.index_documents(
            docs=          all_texts,
            provider_name= provider,
            backend_name=  backend,
            layer_prefix=  LAYER
        )

logger.info("✅ All done.")
