#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/app/llm/llm_factory.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
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
import asyncio
import json
import logging
import os
import sys
import typing
from functools import partial
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Union
import aiohttp
import openai
from app.config import cfg

"""LLM Factory – async wrapper over multiple back‑ends.

Supported providers (pick via `<LAYER>_LLM_PROVIDER`):
----------------------------------------------------
* **azure**   – Azure OpenAI Chat Completions
* **openai**  – Public OpenAI API
* **llama3**  – Ollama‑style `/api/generate` (or any HTTP that follows that schema)
* **hf_local** – On‑prem model via *transformers* **or** *llama‑cpp‑python* (CPU‑friendly)
* **tgi** / **vllm** – Generic OpenAI‑compatible REST service (HuggingFace TGI 1.4+, vLLM ≥0.4)

Each client exposes `await chat(messages, **kwargs) -> str` where
`messages = [{"role": "user"|"assistant"|"system", "content": "..."}]`.
"""
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Base interface
# ---------------------------------------------------------------------------
class LLMClientBase:
    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:  # noqa: D401
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Azure OpenAI
# ---------------------------------------------------------------------------
class AzureOpenAIClient(LLMClientBase):
    def __init__(self, *, layer: str):
        self.deployment   = cfg("OPENAI_MODEL",    layer=layer, provider="AZURE")
        self.endpoint     = cfg("OPENAI_ENDPOINT", layer=layer, provider="AZURE")
        self.api_key      = cfg("OPENAI_KEY",      layer=layer, provider="AZURE")
        self.api_version  = cfg("OPENAI_API_VERSION",
                                layer=layer, provider="AZURE", default="2023-05-15")

        if not all((self.deployment, self.endpoint, self.api_key)):
            raise ValueError("Azure OpenAI credentials incomplete.")
        openai.api_type    = "azure"
        openai.api_base    = self.endpoint
        openai.api_version = self.api_version
        openai.api_key     = self.api_key

    # NEW implementation ─ keeps the whole dict when a function call is returned
    async def chat(
        self,
        messages: List[Dict[str, str]],
        **kwargs,
) -> Union[str, Dict[str, Any]]:       # <-- use Union from typing

 
        """
        • If the model answers with plain text → return that string.  
        • If the model decides to call a function → return the *entire*
          message dict so `function_call` is preserved.
        """
        resp = await openai.ChatCompletion.acreate(
            deployment_id=self.deployment,
            messages=messages,
            **kwargs,
        )
        msg = resp.choices[0].message.to_dict()
        return msg if msg.get("function_call") else msg.get("content", "")
    
# ---------------------------------------------------------------------------
# Public OpenAI
# ---------------------------------------------------------------------------
class OpenAIClient(LLMClientBase):
    def __init__(self, *, layer: str):
        self.api_key = cfg("OPENAI_API_KEY", layer=layer)
        self.model = cfg("OPENAI_MODEL", layer=layer, default="gpt-4o-mini")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY missing")
        openai.api_key = self.api_key

    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:  # noqa: D401
        resp = await openai.ChatCompletion.acreate(model=self.model, messages=messages, **kwargs)  # type: ignore[attr-defined]
        return resp.choices[0].message.content


# ---------------------------------------------------------------------------
# Llama 3 via simple generate endpoint (e.g. Ollama)
# ---------------------------------------------------------------------------
class Llama3Client(LLMClientBase):
    def __init__(self, *, layer: str):
        self.base_url = cfg("LLAMA3_BASE_URL", layer=layer, default="http://localhost:11434")
        self.model = cfg("LLAMA3_MODEL_NAME", layer=layer, default="llama3")

    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:  # noqa: D401
        prompt = "\n".join([m["content"] for m in messages])
        async with aiohttp.ClientSession() as sess:
            async with sess.post(f"{self.base_url}/api/generate", json={"model": self.model, "prompt": prompt, **kwargs}, timeout=60) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data["response"]


# ---------------------------------------------------------------------------
# HF‑Local (transformers *or* llama‑cpp‑python)
# ---------------------------------------------------------------------------
class HFLocalClient(LLMClientBase):
    """Runs a model in‑process – good for CPU‑only boxes."""

    def __init__(self, *, layer: str):
        self.engine = cfg("HF_LOCAL_ENGINE", layer=layer, default="transformers").lower()
        self.model_path = cfg("HF_LOCAL_MODEL_PATH", layer=layer)  # local .gguf or HF model id
        self.model_name = cfg("HF_LOCAL_MODEL_NAME", layer=layer, default="mistralai/Mistral-7B-Instruct-v0.2")
        self.max_new = cfg("HF_LOCAL_MAX_TOKENS", layer=layer, cast=int, default=256)

        if self.engine == "transformers":
            try:
                from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline  # type: ignore
            except ImportError:
                raise ImportError("transformers not installed – pip install transformers sentencepiece")
            model_id = self.model_path or self.model_name
            logger.info("Loading transformers model %s (this may take a while)…", model_id)
            tok = AutoTokenizer.from_pretrained(model_id)
            mod = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", trust_remote_code=True)
            self.pipe = pipeline("text-generation", model=mod, tokenizer=tok)
        elif self.engine == "llama_cpp":
            try:
                from llama_cpp import Llama  # type: ignore
            except ImportError:
                raise ImportError("llama-cpp-python not installed – pip install llama-cpp-python")
            gguf_path = Path(self.model_path or "./model.gguf")
            if not gguf_path.exists():
                raise FileNotFoundError(f"GGUF model not found at {gguf_path}")
            self.llm = Llama(model_path=str(gguf_path), n_ctx=4096)
        else:
            raise ValueError(f"Unknown HF_LOCAL_ENGINE '{self.engine}' (transformers | llama_cpp)")

    async def _run_blocking(self, prompt: str) -> str:
        if self.engine == "transformers":
            res = self.pipe(prompt, max_new_tokens=self.max_new, do_sample=True)
            return res[0]["generated_text"][len(prompt) :].strip()
        else:  # llama_cpp
            res = self.llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], max_tokens=self.max_new)
            return res["choices"][0]["message"]["content"].strip()

    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:  # noqa: D401
        prompt = "\n".join([m["content"] for m in messages])
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, partial(self._run_blocking, prompt))


# ---------------------------------------------------------------------------
# TGI / vLLM remote server (OpenAI compatible)
# ---------------------------------------------------------------------------
class TGIClient(LLMClientBase):
    def __init__(self, *, layer: str):
        self.base_url = cfg("TGI_BASE_URL", layer=layer, default="http://localhost:8000")
        self.model = cfg("TGI_MODEL_NAME", layer=layer, default="local-model")
        self.timeout = cfg("TGI_TIMEOUT_S", layer=layer, cast=int, default=60)

    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:  # noqa: D401
        payload = {"model": self.model, "messages": messages, **kwargs}
        async with aiohttp.ClientSession() as sess:
            async with sess.post(f"{self.base_url}/v1/chat/completions", json=payload, timeout=self.timeout) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data["choices"][0]["message"]["content"].strip()


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------
ProviderType = Literal["azure", "openai", "llama3", "hf_local", "tgi", "vllm"]


def get_llm(layer: str | None = None) -> LLMClientBase:  # noqa: D401
    layer = (layer or cfg("ACTIVE_LAYER", default="FASTAPI")).upper()
    provider: ProviderType = cfg("LLM_PROVIDER", layer=layer, default="azure").lower()  # type: ignore[assignment]
    logger.info("LLM factory – layer=%s provider=%s", layer, provider)
    # Bail out early if the layer says "no LLM"

    if not cfg("LLM_ENABLED", layer=layer, cast=bool, default=True):
        class _Dummy(LLMClientBase):
            async def chat(self, messages, **kw):      # noqa: D401
                return "⚠️  LLM disabled for this layer."
        return _Dummy()

    if provider == "azure":
        return AzureOpenAIClient(layer=layer)
    if provider == "openai":
        return OpenAIClient(layer=layer)
    if provider == "llama3":
        return Llama3Client(layer=layer)
    if provider == "hf_local":
        return HFLocalClient(layer=layer)
    if provider in {"tgi", "vllm"}:
        return TGIClient(layer=layer)

    raise ValueError(f"Unsupported LLM provider '{provider}'.")


__all__ = [
    "LLMClientBase",
    "AzureOpenAIClient",
    "OpenAIClient",
    "Llama3Client",
    "HFLocalClient",
    "TGIClient",
    "get_llm",
]
