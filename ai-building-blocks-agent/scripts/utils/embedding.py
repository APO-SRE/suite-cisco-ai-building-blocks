#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/scripts/utils/embedding.py
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
import os
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

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

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None



# e.g. "azure_openai", "openai", or "huggingface"
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "azure_openai").lower()


# 1) Azure OpenAI Embedding
#    Set environment variables:
#      AZURE_OPENAI_EMBEDDING_KEY
#      AZURE_OPENAI_EMBEDDING_ENDPOINT
#      AZURE_OPENAI_API_VERSION
#      AZURE_OPENAI_EMBEDDING_DEPLOYMENT

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
def _azure_embed_text(text: str) -> list:
    azure_openai_key = os.getenv("AZURE_OPENAI_EMBEDDING_KEY")
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT")
    azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    azure_openai_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")

    if not all([azure_openai_key, azure_openai_endpoint, azure_openai_api_version, azure_openai_deployment]):
        raise ValueError("Missing Azure OpenAI env vars")

    openai.api_key = azure_openai_key
    openai.api_base = azure_openai_endpoint
    openai.api_type = "azure"
    openai.api_version = azure_openai_api_version

    resp = openai.Embedding.create(
        input=text,
        engine=azure_openai_deployment
    )
    embedding = resp["data"][0]["embedding"]
    return embedding



# 2) OpenAI (public) Embedding
#    Set environment variables:
#      OPENAI_API_KEY
#      OPENAI_EMBEDDING_MODEL (e.g. "text-embedding-ada-002")

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
def _openai_embed_text(text: str) -> list:
    openai_key = os.getenv("OPENAI_API_KEY")
    openai_model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")
    if not openai_key:
        raise ValueError("Missing OPENAI_API_KEY for public OpenAI embeddings")

    openai.api_key = openai_key
    openai.api_base = "https://api.openai.com/v1"

    resp = openai.Embedding.create(
        input=text,
        model=openai_model
    )
    embedding = resp["data"][0]["embedding"]
    return embedding



# 3) Hugging Face Embedding (local or downloaded model)
#    If using in CPU only server - 
#       1. install torch with CPU support: pip install torch --index-url https://download.pytorch.org/wh1/nightly/cpu
#       2. pip install sentence-transformers
#       3. set environment variable HUGGINGFACE_MODEL_NAME to the model name (e.g. "sentence-transformers/all-MiniLM-L6-v2")

_hf_model = None
def _huggingface_embed_text(text: str) -> list:
    global _hf_model
    model_name = os.getenv("HUGGINGFACE_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
    if not SentenceTransformer:
        raise ValueError("sentence-transformers is not installed. Please `pip install sentence-transformers`.")
    if _hf_model is None:
        print(f"Loading Hugging Face model: {model_name}")
        _hf_model = SentenceTransformer(model_name)
    # Encode returns a numpy array; convert to Python list for consistency
    return _hf_model.encode(text).tolist()


def embed_text(text: str) -> list:
    """
    Main embedding function that dispatches based on EMBEDDING_PROVIDER:
      - "azure_openai": call _azure_embed_text
      - "openai": call _openai_embed_text
      - "huggingface": call _huggingface_embed_text
    """
    if EMBEDDING_PROVIDER == "azure_openai":
        return _azure_embed_text(text)
    elif EMBEDDING_PROVIDER == "openai":
        return _openai_embed_text(text)
    elif EMBEDDING_PROVIDER == "huggingface":
        return _huggingface_embed_text(text)
    else:
        raise ValueError(f"Unknown EMBEDDING_PROVIDER: {EMBEDDING_PROVIDER}")
