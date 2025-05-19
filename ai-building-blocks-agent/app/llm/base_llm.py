# app/llm/base_llm.py
class BaseLLM:                       # legacy name used by older modules
    """Removed during refactor – kept only for backward-compat."""
    async def chat(self, *a, **kw):   # never called – real work is in llm_factory
        raise NotImplementedError
