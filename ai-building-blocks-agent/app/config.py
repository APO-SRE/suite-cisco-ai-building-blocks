#!/usr/bin/env python3
from __future__ import annotations
################################################################################
# ai-building-blocks-agent/app/config.py
# Copyright (c) 2025 Jeff Teeter
# Cisco Systems, Inc.
# Licensed under the Apache License, Version 2.0 (see LICENSE)
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
"""Centralised environment-variable resolver.

*   Guarantees a **single source of truth** (no scattered ``os.getenv`` calls).
*   Supports the hierarchical naming scheme::

        <LAYER>_[<PROVIDER>_]KEY

    Examples:
        * ``FASTAPI_AZURE_LLM_MODEL=gpt-4o``
        * ``DOMAIN_CHROMA_VECTOR_BACKEND=chroma``
        * ``EVENTS_DEBUG_MODE=false``

If a requested var is missing, resolution falls back gracefully:

1. ``<LAYER>_<PROVIDER>_<KEY>``
2. ``<LAYER>_<KEY>``
3. ``<KEY>``
4. Provided ``default`` (if any)

Boolean casting accepts common truthy strings: ``1, true, yes, on`` (case-insensitive).
"""



import logging
import os
from typing import Any, Callable, Optional, TypeVar

from dotenv import load_dotenv

# --------------------------------------------------------------------------- #
# Initialisation                                                              #
# --------------------------------------------------------------------------- #

load_dotenv(override=False)  # never clobber system-exported envs
_logger = logging.getLogger(__name__)

T = TypeVar("T")

# Default layer when the caller omits *layer* and ACTIVE_LAYER is unset
DEFAULT_LAYER: str = os.getenv("ACTIVE_LAYER", "FASTAPI").upper()

# --------------------------------------------------------------------------- #
# Helpers                                                                     #
# --------------------------------------------------------------------------- #


def _to_bool(raw: str | bool | None) -> bool:
    """Cast an env string to bool with generous truthy values."""
    if isinstance(raw, bool):
        return raw
    if raw is None:
        return False
    return raw.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


_CASTERS: dict[type, Callable[[str], Any]] = {
    bool: _to_bool,
    int: int,
    float: float,
    str: str,
}

# --------------------------------------------------------------------------- #
# Public API                                                                  #
# --------------------------------------------------------------------------- #


class Config:
    """Callable env-lookup utility."""

    def __call__(
        self,
        key: str,
        *,
        layer: str | None = None,
        provider: str | None = None,
        default: Optional[T] = None,
        cast: type[T] = str,  # type: ignore[assignment]
    ) -> T | None:
        """Resolve and cast an environment variable.

        Parameters
        ----------
        key
            Core variable name (case-insensitive), e.g. ``"LLM_MODEL"``.
        layer
            Layer prefix (``FASTAPI``, ``DOMAIN``, …).
            Defaults to ``DEFAULT_LAYER``.
        provider
            Optional provider infix (``AZURE``, ``CHROMA`` …).
        default
            Fallback value if the env var is absent *or* cannot be cast.
        cast
            Desired return type – one of ``str``, ``int``, ``float``, ``bool``.
        """
        if cast not in _CASTERS:
            raise TypeError(
                f"Unsupported cast type: {cast!r}. "
                f"Choose from {', '.join(t.__name__ for t in _CASTERS)}."
            )

        parts: list[str] = []
        if layer := (layer or DEFAULT_LAYER):
            parts.append(layer.upper())
        if provider:
            parts.append(provider.upper())
        parts.append(key.upper())
        env_key = "_".join(parts)

        val: str | None = os.getenv(env_key)

        # 2️⃣ try without provider
        if val is None and provider:
            val = os.getenv(f"{layer}_{key}".upper())

        # 3️⃣ fall back to plain key
        if val is None:
            val = os.getenv(key.upper())

        if val is None:
            return default  # type: ignore[return-value]

        try:
            return _CASTERS[cast](val)  # type: ignore[return-value]
        except Exception as exc:  # noqa: BLE001
            _logger.warning(
                "CONFIG: failed to cast %s=%r to %s – %s",
                env_key,
                val,
                cast.__name__,
                exc,
            )
            return default  # type: ignore[return-value]


cfg = Config()

# Convenience wrappers – purely syntactic sugar
get_bool = lambda k, **kw: cfg(k, cast=bool, **kw)  # noqa: E731
get_int = lambda k, **kw: cfg(k, cast=int, **kw)  # noqa: E731
get_float = lambda k, **kw: cfg(k, cast=float, **kw)  # noqa: E731
get_str = lambda k, **kw: cfg(k, cast=str, **kw)  # noqa: E731

# --------------------------------------------------------------------------- #
# Quick self-test                                                             #
# --------------------------------------------------------------------------- #

if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level="INFO", format="%(levelname)s: %(message)s")

    print("ACTIVE_LAYER:", DEFAULT_LAYER)
    print("FASTAPI -> DEBUG_MODE (bool):",
          cfg("DEBUG_MODE", layer="FASTAPI", cast=bool))
    print("FASTAPI+AZURE -> LLM_MODEL (str):",
          cfg("LLM_MODEL", layer="FASTAPI", provider="AZURE"))
