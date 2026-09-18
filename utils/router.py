"""
Model routing utilities.

Automatically selects appropriate model tier based on prompt technique:
- Reasoning techniques (cot, tot) → reasoning models
- General techniques → general models
"""

import yaml
from pathlib import Path
from typing import Literal, Optional
from .config_loader import (
    get_general_techniques,
    get_strong_techniques,
    get_reasoning_techniques,
)


def pick_model(
    provider: Literal["openai", "google", "groq"],
    technique: str,
    tier: Optional[Literal["general", "strong", "reason"]] = None,
    config_path: str = "config/models.yaml",
) -> str:
    """
    Select appropriate model based on provider and technique.

    Routing logic:
    - configured reasoning techniques → reason tier
    - technique in {"strong", "complex"} → strong tier
    - Otherwise → general tier
    - Explicit tier parameter overrides automatic routing

    Args:
        provider: API provider (openai, google, groq)
        technique: Prompt technique identifier
        tier: Optional explicit tier selection
        config_path: Path to models.yaml config file

    Returns:
        Model identifier string

    Raises:
        FileNotFoundError: If config file not found
        KeyError: If provider or fallback tier is missing
        ValueError: If technique or tier is unknown
    """
    config_file = Path(config_path)

    # If config file doesn't exist, try relative to this file's location
    if not config_file.exists():
        # Try relative to utils directory (project root)
        utils_dir = Path(__file__).resolve().parent
        project_root = utils_dir.parent
        config_file = project_root / config_path

    if not config_file.exists():
        raise FileNotFoundError(
            f"Model config not found. Tried:\n"
            f"  - {config_path}\n"
            f"  - {config_file}\n"
            f"Current working directory: {Path.cwd()}"
        )

    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    if provider not in config:
        raise KeyError(f"Provider '{provider}' not found in {config_path}")
    technique = technique.strip().lower()

    valid_techniques = {
        item.strip().lower()
        for item in (
            get_general_techniques()
            + get_strong_techniques()
            + get_reasoning_techniques()
        )
    }

    if technique not in valid_techniques:
        raise ValueError(
            f"Unknown technique: {technique!r}. "
            f"Allowed: {', '.join(sorted(valid_techniques))}"
        )

    if tier is not None and tier not in {"general", "strong", "reason"}:
        raise ValueError(f"Unknown tier: {tier!r}")
    # Determine tier based on technique if not explicitly provided
    if tier is None:
        # Reasoning techniques require reasoning models
        if should_use_reasoning_model(technique):
            tier = "reason"
        # Strong/complex techniques benefit from stronger models
        elif should_use_strong_model(technique):
            tier = "strong"
        # Default to general tier
        else:
            tier = "general"

    if tier not in config[provider]:
        # Fallback to general if requested tier not available
        tier = "general"

    return config[provider][tier]


def should_use_reasoning_model(technique: str) -> bool:
    """
    Check if technique requires reasoning model.

    Args:
        technique: Prompt technique identifier

    Returns:
        True if reasoning model recommended
    """
    from .config_loader import should_auto_route_reasoning, get_reasoning_techniques

    if not should_auto_route_reasoning():
        return False

    return technique.strip().lower() in {
        item.strip().lower() for item in get_reasoning_techniques()
    }


def should_use_strong_model(technique: str) -> bool:
    """Check if technique requires a strong model."""
    from .config_loader import get_strong_techniques

    return technique.strip().lower() in {
        item.strip().lower() for item in get_strong_techniques()
    }
