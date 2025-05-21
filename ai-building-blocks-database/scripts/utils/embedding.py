#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/utils/embedding.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
from __future__ import annotations

"""
DISCLAIMER: USE AT YOUR OWN RISK

This script is provided 'as is' without warranty of any kind. By using this code,
you agree to the terms stated in the LICENSE and above disclaimers.

This module focuses solely on generating embeddings from text, without
summaries/keywords. Summaries & keywords are handled by other code if needed.
"""
import os
import openai
from typing import List, Union
from sentence_transformers import SentenceTransformer
from threading import Lock
_hf_models = {}  # Cache loaded SentenceTransformer models
_hf_lock = Lock()  

def embed_text(text: Union[str, List[str]], layer: str = "FASTAPI") -> List[List[float]]:
    """
    Generate embedding vectors for given text(s), based on environment variables
    indicating whether the layer uses Azure or Hugging Face embeddings, etc.

    Args:
        text (str or List[str]): The text(s) to embed.
        layer (str): The layer name, e.g. "DOMAIN", "FASTAPI", "EVENTS", "AGENTIC".

    Returns:
        List[List[float]]: A list of embedding vectors (one per input string).
    """

    # 1) Ensure input is a list
    if isinstance(text, str):
        texts = [text]
    else:
        texts = text

    # 2) Decide embedding provider
    #    e.g., "AGENTIC_EMBEDDING_PROVIDER" => "azure" or "huggingface" or "elastic"
    provider_var = f"{layer.upper()}_EMBEDDING_PROVIDER"
    provider = os.getenv(provider_var, "huggingface").lower()

    if provider == "azure":
        return _embed_azure(texts, layer)
    elif provider == "huggingface":
        return _embed_huggingface(texts, layer)
    elif provider == "elastic":
        # If you implement Elasticsearch-based embedding logic, you'd do that here.
        raise NotImplementedError("Elastic embedding not implemented in this script.")
    else:
        raise ValueError(f"[embedding.py] Unknown provider '{provider}' for layer '{layer}'")

def _embed_azure(texts: List[str], layer: str) -> List[List[float]]:
    """
    Use Azure OpenAI to embed a list of texts. The code reads environment
    variables like <LAYER>_AZURE_OPENAI_ENDPOINT, <LAYER>_AZURE_OPENAI_KEY,
    <LAYER>_AZURE_EMBEDDING_DEPLOYMENT, etc.
    """
    # 1) Compose env var names
    layer_key = layer.upper()
    azure_endpoint = os.getenv(f"{layer_key}_AZURE_OPENAI_ENDPOINT", "").strip("/")
    azure_key = os.getenv(f"{layer_key}_AZURE_OPENAI_KEY", "")
    azure_deployment = os.getenv(f"{layer_key}_AZURE_OPENAI_EMBEDDING_DEPLOYMENT","")

    if not azure_endpoint or not azure_key or not azure_deployment:
        raise ValueError(f"[embedding.py] Missing Azure env vars for layer '{layer}': "
                         f"{layer_key}_AZURE_OPENAI_ENDPOINT, _KEY, or _EMBEDDING_DEPLOYMENT not set.")

    # 2) Set openai config
    openai.api_type = "azure"
    openai.api_base = azure_endpoint
    openai.api_key = azure_key
    # Possibly read a version like <LAYER>_AZURE_OPENAI_API_VERSION if you want
    openai.api_version = os.getenv(f"{layer_key}_AZURE_OPENAI_API_VERSION", "2024-10-21")

    # 3) Make the request
    resp = openai.Embedding.create(input=texts, engine=azure_deployment)
    # 4) Extract embeddings
    vectors = [item["embedding"] for item in resp["data"]]
    return vectors

def _embed_huggingface(texts: list[str], layer: str) -> list[list[float]]:
    """
    Embeds *texts* with a local / HF SentenceTransformer model.
    Model name comes from  <LAYER>_HUGGINGFACE_MODEL  (env).
    The model is loaded exactly **once** per process, guarded by a lock so
    multi-threaded pipelines don’t race when instantiating it.
    """
    layer_key  = layer.upper()
    model_name = os.getenv(f"{layer_key}_HUGGINGFACE_MODEL", "").strip()
    if not model_name:
        raise ValueError(
            f"[embedding.py] No Hugging Face model specified for layer '{layer}'. "
            f"Set {layer_key}_HUGGINGFACE_MODEL in your env."
        )

    # ── lazy-load the model, but only one thread does the heavy work ─────────
    with _hf_lock:
        if model_name not in _hf_models:
            print(f"[embedding.py] Loading HF model '{model_name}' for layer '{layer}'…")
            from sentence_transformers import SentenceTransformer
            _hf_models[model_name] = SentenceTransformer(model_name, device="cpu")

    model = _hf_models[model_name]

    # encode() is internally parallelised by SentenceTransformers/torch
    ndarray = model.encode(texts, convert_to_numpy=True)
    return [vec.tolist() for vec in ndarray]

