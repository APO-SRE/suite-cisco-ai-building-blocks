#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/indexers/__init__.py
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
# ai-building-blocks-database/scripts/__init__.py
import sys, types

# Make everything in this folder importable as "db_scripts.…"
module = types.ModuleType("db_scripts")
module.__path__ = __path__          # type: ignore  # inherit the same path list
sys.modules["db_scripts"] = module

from .azure_indexer import AzureIndexer
from .chroma_indexer import ChromaIndexer
from .elastic_indexer import ElasticIndexer
from .base_indexer import BaseIndexer
# from .base_indexer import BaseIndexer
# from .chroma_indexer import ChromaIndexer
# from .elastic_indexer import ElasticIndexer

