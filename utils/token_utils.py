"""
Token utilities using tiktoken for estimation and context management.

This module provides:
- Encoding selection per provider/model
- Token counting for text and messages
- Reconciliation of estimated vs actual token usage
- Context-fit guards using truncation
"""

import tiktoken
from typing import Literal, Optional, Any


def pick_encoding(
    provider: Literal["openai", "google", "groq"], model: str
) -> tiktoken.Encoding:
    """
    Select appropriate tiktoken encoding for provider/model.

    OpenAI: Use o200k_base for 4.x/o3 models, cl100k_base as fallback
    Google/Groq: Use o200k_base as approximation (caveat: not exact)

    Args:
        provider: API provider name
        model: Model identifier

    Returns:
        tiktoken.Encoding instance
    """
    if provider == "openai":
        # For GPT-4o, GPT-4, o3 models, prefer o200k_base
        if any(x in model.lower() for x in ["gpt-4o", "gpt-4", "o3", "o1"]):
            try:
                return tiktoken.get_encoding("o200k_base")
            except Exception:
                pass
        # Fallback to cl100k_base for GPT-3.5 and older
        return tiktoken.get_encoding("cl100k_base")

    # For non-OpenAI providers, use o200k_base as approximation
    # Note: This is an approximation only; actual tokenization may differ
    return tiktoken.get_encoding("o200k_base")


def count_messages_tokens(
    messages: list[dict[str, str]],
    provider: Literal["openai", "google", "groq"],
    model: str,
    context_strs: Optional[list[str]] = None,
) -> dict[str, int]:
    """
    Count tokens in a messages array, separating input vs context.

    Input tokens: system + user messages
    Context tokens: additional context strings (e.g., RAG documents)
    Estimated total: input + context + overhead

    Args:
        messages: OpenAI-style messages array
        provider: API provider
        model: Model identifier
        context_strs: Optional list of context strings to count separately

    Returns:
        Dict with input_tokens, context_tokens, estimated_total
    """
    enc = pick_encoding(provider, model)

    # Count input tokens (system + user messages)
    input_tokens = 0
    for msg in messages:
        content = msg.get("content", "")
        # Add role overhead (typically ~4 tokens per message in OpenAI format)
        input_tokens += 4
        input_tokens += len(enc.encode(content, disallowed_special=()))

    # Count context tokens separately
    context_tokens = 0
    if context_strs:
        for ctx in context_strs:
            context_tokens += len(enc.encode(ctx, disallowed_special=()))

    # Add base overhead for message formatting
    overhead = 3  # for message array structure

    return {
        "input_tokens": input_tokens,
        "context_tokens": context_tokens,
        "estimated_total": input_tokens + context_tokens + overhead,
    }


def reconcile_usage(
    estimate: dict[str, int], provider_usage: Optional[dict[str, Any]] = None
) -> dict[str, int]:
    """
    Merge estimated vs actual token usage from provider.

    Args:
        estimate: Dict with input_tokens, context_tokens, estimated_total
        provider_usage: Optional usage dict from provider API response

    Returns:
        Dict with both estimated and actual fields
    """
    result = {
        "input_tokens_est": estimate.get("input_tokens", 0),
        "context_tokens_est": estimate.get("context_tokens", 0),
        "total_est": estimate.get("estimated_total", 0),
        "prompt_tokens_actual": None,
        "completion_tokens_actual": None,
        "total_tokens_actual":  provider_usage.get("totalTokenCount"),
    }

    if provider_usage:
        # OpenAI format
        if "prompt_tokens" in provider_usage:
            result["prompt_tokens_actual"] = provider_usage["prompt_tokens"]
            result["completion_tokens_actual"] = provider_usage.get(
                "completion_tokens", 0
            )
            result["total_tokens_actual"] = provider_usage.get("total_tokens", 0)
        # Google Gemini format (uses different field names)
        elif "promptTokenCount" in provider_usage:
            result["prompt_tokens_actual"] = provider_usage.get("promptTokenCount") or 0
            result["completion_tokens_actual"] = (
                provider_usage.get("candidatesTokenCount") or 0
            )
            result["total_tokens_actual"] = (
                result["prompt_tokens_actual"] + result["completion_tokens_actual"]
            )

    return result

