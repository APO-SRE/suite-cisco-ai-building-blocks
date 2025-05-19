#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/retrievers/__init__.py
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

from .azure_search_retriever import AzureSearchRetriever
from .chroma_retriever import ChromaRetriever
from .elastic_retriever import ElasticRetriever
from .null_retriever import NullRetriever

__all__ = [
    "AzureSearchRetriever",
    "ChromaRetriever",
    "ElasticRetriever",
    "NullRetriever",
]
