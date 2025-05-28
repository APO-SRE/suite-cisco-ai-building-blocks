
#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/process_events.py
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
import json
import uuid
import logging
from dotenv import load_dotenv

from scripts.utils.chunking import chunk_file
from scripts.utils import pipeline_utils

# 1) Load .env & configure logging
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("process_events")

# 2) Hard-code the layer
LAYER = "EVENTS"

# 3) Read which vector backend & embedding provider we’re using
backend  = os.getenv(f"{LAYER}_VECTOR_BACKEND",    "azure").lower()
provider = os.getenv(f"{LAYER}_EMBEDDING_PROVIDER", "azure").lower()
logger.info(f"Layer={LAYER}, VECTOR_BACKEND={backend}, EMBEDDING_PROVIDER={provider}")

# 4) Decide concurrency prefix (for OMP_NUM_THREADS, etc.)
_prefix_map = {"azure": "AZURE", "chroma": "CHROMA", "elastic": "ELASTIC"}
prefix_key = _prefix_map.get(backend, "AZURE")

# 5) Pull concurrency from environment
omp_var  = os.getenv(f"{LAYER}_{prefix_key}_OMP_NUM_THREADS") or os.getenv("OMP_NUM_THREADS", "1")
mkl_var  = os.getenv(f"{LAYER}_{prefix_key}_MKL_NUM_THREADS") or os.getenv("MKL_NUM_THREADS", "1")
cpus_var = os.getenv(f"{LAYER}_{prefix_key}_NUM_CPUS")       or os.getenv("NUM_CPUS", "1")

logger.info(f"Threads: OMP_NUM_THREADS={omp_var}, MKL_NUM_THREADS={mkl_var}, NUM_CPUS={cpus_var}")

# 6) Apply them so that libraries & pipeline_utils pick them up
os.environ["OMP_NUM_THREADS"] = omp_var
os.environ["MKL_NUM_THREADS"] = mkl_var
os.environ[f"{LAYER}_OMP_NUM_THREADS"] = cpus_var
logger.info(f"Set {LAYER}_OMP_NUM_THREADS={cpus_var} for pipeline parallelism")

# 7) Only proceed if vector indexing is enabled
if os.getenv(f"{LAYER}_VECTOR_ENABLED", "false").lower() != "true":
    logger.info(f"{LAYER}_VECTOR_ENABLED is not true → skipping.")
    exit(0)

logger.info(f"Using backend={backend!r} for indexing…")

# 8) For Azure backend, explicitly ensure the Azure Search index exists
#    (Chroma & Elastic get created/prompted automatically inside pipeline_utils.)
if backend == "azure":
    from scripts.indexers.azure_indexer import AzureIndexer
    idx = os.getenv(f"{LAYER}_AZURE_INDEX", f"{LAYER.lower()}-index")
    logger.info(f"Ensuring Azure Search index '{idx}'…")

    AzureIndexer(idx, layer_name=LAYER).create_index(recreate=None)
    os.environ[f"{LAYER}_AZURE_INDEX"] = idx

# 9) Load & chunk your events JSON
events_path = "events/sample_events.json"
if not os.path.exists(events_path):
    logger.warning(f"Missing {events_path}, nothing to do.")
    exit(0)

with open(events_path, "r", encoding="utf-8") as f:
    events_data = json.load(f)
if not isinstance(events_data, list) or not events_data:
    logger.warning("No events found in JSON, exiting.")
    exit(0)

# 10) Convert each event to text + chunk
CHUNK_SIZE    = int(os.getenv(f"{LAYER}_{prefix_key}_CHUNK_SIZE",    "2000"))
CHUNK_OVERLAP = int(os.getenv(f"{LAYER}_{prefix_key}_CHUNK_OVERLAP", "100"))

event_chunks = []
for evt in events_data:
    info = evt.get("additional_info", {})
    # Example short text from event
    snippet = (
        f"Event: {evt.get('event_type','unknown')} "
        f"in zone {info.get('zone_id','N/A')} at {info.get('timestamp','N/A')}."
    )


    for chunk in chunk_file(snippet, CHUNK_SIZE, CHUNK_OVERLAP):
        event_chunks.append({
            "id":             evt.get("id"),
            "event_id":       evt.get("event_id"),
            "event_name":     evt.get("event_name"),
            "event_type":     evt.get("event_type"),
            "content":        chunk,
            "additional_info": info
        })

logger.info(f"Prepared {len(event_chunks)} event-chunks from {len(events_data)} events.")



 

# 11) Let pipeline_utils do embedding + indexing.
#     For Chroma, it will:
#       - Check if the collection name already exists
#       - If so and if EVENTS_CHROMA_RECREATE_INDEX is not set to "true"
#         it will prompt for (R)ecreate or (A)ppend
#     Same pattern if you eventually implement the process_docs, process_domain, etc.
logger.info(f"Embedding & indexing {len(event_chunks)} chunks via {backend}…")

pipeline_utils.index_documents(
    docs=          event_chunks,
    provider_name= provider,
    backend_name=  backend,
    layer_prefix=  LAYER
)

logger.info("✅ All done.")