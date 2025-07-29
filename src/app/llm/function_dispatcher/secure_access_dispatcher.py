# app/llm/function_dispatcher/secure_access_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.secure_access_client import Secure_accessClient

@register('createAuthToken')
def createAuthToken(grant_type: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if grant_type is not None:
        final_kwargs['grant_type'] = grant_type

    # No body parameter for this function.
    body_payload = None

    client = Secure_accessClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.createAuthToken

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
