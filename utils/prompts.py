from dataclasses import dataclass
from string import Template
from typing import Optional, List, Dict, Tuple


@dataclass
class PromptSpec:

    id: str
    purpose: str
    template: str
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None


# Central prompt registry
PROMPTS: Dict[str, PromptSpec] = {
    "zero_shot.v1": PromptSpec(
        id="zero_shot.v1",
        purpose="Direct instruction-first prompt",
        template=(
            "You are ${role}. Follow the instructions precisely.\n"
            "Instruction: ${instruction}\n"
            "Constraints: ${constraints}\n"
            "Output format: ${format}\n"
        ),
        temperature=0.2,
    ),
    "few_shot.v1": PromptSpec(
        id="few_shot.v1",
        purpose="Few-shot with explicit examples block",
        template=(
            "You are ${role}. Learn from the examples, then answer the query.\n\n"
            "Examples:\n${examples}\n\n"
            "Query: ${query}\n"
            "Constraints: ${constraints}\n"
            "Output format: ${format}\n"
        ),
        temperature=0.2,
    ),
    "cot_reasoning.v1": PromptSpec(
        id="cot_reasoning.v1",
        purpose="Structured reasoning for complex crisis scenarios",
        template=(
            "You are ${role}.\n"
            "Analyze the scenario carefully before giving the final recommendation.\n\n"
            "Scenario:\n${query}\n\n"
            "Task:\n${instruction}\n\n"
            "Constraints:\n${constraints}\n\n"
            "Output format:\n${format}\n"
        ),
        temperature=0.3,
    ),
}


def render(prompt_id: str, **vars) -> Tuple[str, PromptSpec]:
    """
    Render a prompt template with variables.

    Args:
        prompt_id: Prompt identifier from PROMPTS registry
        **vars: Variables to substitute in template

    Returns:
        Tuple of (rendered_text, prompt_spec)

    Raises:
        KeyError: If prompt_id not found in registry

    Example:
        >>> text, spec = render("zero_shot.v1",
        ...                     role="helpful assistant",
        ...                     instruction="Summarize this",
        ...                     constraints="Max 50 words",
        ...                     format="Plain text")
    """
    if prompt_id not in PROMPTS:
        raise KeyError(
            f"Prompt '{prompt_id}' not found. "
            f"Available: {', '.join(PROMPTS.keys())}"
        )

    spec = PROMPTS[prompt_id]
    text = Template(spec.template).substitute(**vars)
    return text, spec


def list_prompts() -> List[str]:
    """
    List all available prompt IDs.

    Returns:
        List of prompt identifiers
    """
    return list(PROMPTS.keys())
