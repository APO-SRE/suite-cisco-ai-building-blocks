
#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/process_domain.py
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
import glob
import json
import hashlib
import logging
from dotenv import load_dotenv

from scripts.utils.chunking import chunk_file
from scripts.utils import pipeline_utils

# 1) Load .env & configure logging
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("process_domain")

# 2) Hard-code the layer name:
LAYER = "DOMAIN"

# 3) Determine backend & provider
backend  = os.getenv(f"{LAYER}_VECTOR_BACKEND",    "azure").lower()
provider = os.getenv(f"{LAYER}_EMBEDDING_PROVIDER", "azure").lower()
logger.info(f"Layer={LAYER}, VECTOR_BACKEND={backend}, EMBEDDING_PROVIDER={provider}")

# 4) Decide concurrency prefix (for OMP_NUM_THREADS, etc.)
_backend_prefix_map = {
    "azure":   "AZURE",
    "chroma":  "CHROMA",
    "elastic": "ELASTIC",
}
prefix_key = _backend_prefix_map.get(backend, "AZURE")

# 5) Pull concurrency from environment
omp_var  = os.getenv(f"{LAYER}_{prefix_key}_OMP_NUM_THREADS") or os.getenv("OMP_NUM_THREADS", "1")
mkl_var  = os.getenv(f"{LAYER}_{prefix_key}_MKL_NUM_THREADS") or os.getenv("MKL_NUM_THREADS", "1")
cpus_var = os.getenv(f"{LAYER}_{prefix_key}_NUM_CPUS")       or os.getenv("NUM_CPUS", "1")

logger.info(f"Threads: OMP_NUM_THREADS={omp_var}, MKL_NUM_THREADS={mkl_var}, NUM_CPUS={cpus_var}")
os.environ["OMP_NUM_THREADS"] = omp_var
os.environ["MKL_NUM_THREADS"] = mkl_var
os.environ[f"{LAYER}_OMP_NUM_THREADS"] = cpus_var
logger.info(f"Set {LAYER}_OMP_NUM_THREADS={cpus_var} for pipeline parallelism")

# 6) Check if vector indexing is enabled
if os.getenv(f"{LAYER}_VECTOR_ENABLED", "false").lower() != "true":
    logger.info(f"{LAYER}_VECTOR_ENABLED is not true → skipping domain processing.")
    exit(0)

logger.info(f"Using backend='{backend}' for domain data indexing…")

# 7) If using Azure, ensure index is created
if backend == "azure":
    from scripts.indexers.azure_indexer import AzureIndexer
    idx_name = os.getenv(f"{LAYER}_AZURE_INDEX", f"{LAYER.lower()}-index")
    logger.info(f"Ensuring Azure Search index '{idx_name}'…")
    AzureIndexer(idx_name, layer_name=LAYER).create_index(recreate=None)
    os.environ[f"{LAYER}_AZURE_INDEX"] = idx_name

def deterministic_id(*parts: str, algo: str = "sha1") -> str:
    """
    Build a repeatable ID from any number of text fragments.

    Example
    -------
    deterministic_id("domain", "/path/file.json", "42", "3")  ->
        '6a4e8f85d0c3715f824d4e0c890d503f1ca89e23'
    """
    joined = "§".join(parts)          # unlikely to appear in file names
    h      = hashlib.new(algo)
    h.update(joined.encode())
    return h.hexdigest()

################################################################################
# 8) Gather domain data from domain_samples/<folder_name>/...
################################################################################

folder_name = os.getenv("DOMAIN_SAMPLES_INDEX_FOLDER_NAME", "")  # e.g. "airline"
if not folder_name:
    logger.warning("No DOMAIN_SAMPLES_INDEX_FOLDER_NAME specified in .env; defaulting to 'domain_samples'")
domain_samples_dir = os.path.join("domain_samples", folder_name)  
# e.g. domain_samples/airline

json_files = glob.glob(os.path.join(domain_samples_dir, "*.json"))
if not json_files:
    logger.warning(f"No .json files found in '{domain_samples_dir}'. Nothing to index.")
    exit(0)

all_chunks = []
CHUNK_SIZE    = int(os.getenv(f"{LAYER}_{prefix_key}_CHUNK_SIZE",    "2000"))
CHUNK_OVERLAP = int(os.getenv(f"{LAYER}_{prefix_key}_CHUNK_OVERLAP", "100"))

for fp in json_files:
    logger.info(f"Loading domain data from: {fp}")
    try:
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Could not read/parse {fp}: {e}")
        continue

    # data might be a list or single dict
    records = data if isinstance(data, list) else [data]

    # chunk each record
    for rec_idx, record in enumerate(records):
        # Convert everything to text
        text_parts = []
        for key, val in record.items():
            if isinstance(val, str):
                text_parts.append(val.strip())
            elif isinstance(val, (list, dict)):
                # Optionally flatten further
                pass

        combined_text = "\n".join(text_parts).strip()
        if not combined_text:
            continue
        for chunk_idx, chunk in enumerate(
            chunk_file(combined_text, CHUNK_SIZE, CHUNK_OVERLAP)
        ):
            all_chunks.append({
                "id": deterministic_id("domain", fp, str(rec_idx), str(chunk_idx)),
                "content":  chunk,
                "metadata": record
            })
 

logger.info(f"Prepared {len(all_chunks)} domain-chunks from {len(json_files)} files in {domain_samples_dir}.")

if not all_chunks:
    logger.info("No domain chunks found; nothing to index.")
    exit(0)

logger.info(f"Embedding & indexing {len(all_chunks)} domain-chunks via {backend}…")

pipeline_utils.index_documents(
    docs=          all_chunks,
    provider_name= provider,
    backend_name=  backend,
    layer_prefix=  LAYER
)

logger.info("✅ Domain indexing complete.")