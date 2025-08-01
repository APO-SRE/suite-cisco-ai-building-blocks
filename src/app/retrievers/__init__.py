#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## src/app/retrievers/__init__.py
## Copyright (c) 2025 Jeff Teeter
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
from app.config import cfg
import sys

# ════════════════════════════════════════════════════════════════════════
# 1️⃣  Helper that every retriever can safely import
# ════════════════════════════════════════════════════════════════════════
def default_pool_size(layer: str, backend: str, *, fallback: int = 4) -> int:
    """
    Determine how many worker-threads / processes a retriever should use.

    Resolution order (highest-to-lowest):

        1. <LAYER>_<BACKEND>_RETRIEVER_WORKERS
        2. <LAYER>_RETRIEVER_WORKERS
        3. RETRIEVER_WORKERS
        4. fallback (default = 4)
    """
    layer_uc   = layer.upper()
    backend_uc = backend.upper()

    # 1️⃣ layer-specific + backend-specific
    val = cfg(f"{layer_uc}_{backend_uc}_RETRIEVER_WORKERS", cast=int, default=None)
    if val is not None:
        return val

    # 2️⃣ layer-wide
    val = cfg(f"{layer_uc}_RETRIEVER_WORKERS", cast=int, default=None)
    if val is not None:
        return val

    # 3️⃣ global
    return cfg("RETRIEVER_WORKERS", cast=int, default=fallback)


# ════════════════════════════════════════════════════════════════════════
# 2️⃣  Import the concrete retriever implementations
#     (they are free to `from retrievers import default_pool_size`)
# ════════════════════════════════════════════════════════════════════════
from .azure_search_retriever import AzureSearchRetriever   # noqa: E402
from .chroma_retriever       import ChromaRetriever        # noqa: E402
from .elastic_retriever      import ElasticRetriever       # noqa: E402
from .null_retriever         import NullRetriever          # noqa: E402


__all__ = [
    "default_pool_size",
    "AzureSearchRetriever",
    "ChromaRetriever",
    "ElasticRetriever",
    "NullRetriever",
]

# ════════════════════════════════════════════════════════════════════════
# 3️⃣  Alias register: make `import retrievers` work too
# ════════════════════════════════════════════════════════════════════════
# If this module is imported as 'app.retrievers', map the same object to
# the top-level name 'retrievers' so legacy imports continue to work.
if __name__ == "app.retrievers":
    sys.modules.setdefault("retrievers", sys.modules[__name__])




