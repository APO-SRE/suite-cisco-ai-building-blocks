# app/llm/function_dispatcher/ai_defense_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.ai_defense_client import Ai_defenseClient

@register('inspectChat')
def inspectChat():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Ai_defenseClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.inspectChat

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('inspectHttp')
def inspectHttp():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Ai_defenseClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.inspectHttp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
