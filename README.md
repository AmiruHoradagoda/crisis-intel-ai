# Crisis Intel AI

A notebook-based learning project for processing crisis reports. It explores message classification, flood news extraction, rescue prioritization, response stability, and token budgeting. The notebooks use shared utilities for prompts, model routing, configuration, JSON handling, and LLM calls.

This is a prototype for experiments with sample data. Review model outputs before using them for real decisions.

## Setup

Use Python 3.12 or later. From the repository root, install the project dependencies with [uv](https://docs.astral.sh/uv/):

```powershell
uv sync
```

The dependencies are declared in `pyproject.toml` and pinned in `uv.lock`. `requirements.txt` is also present for a pip-based setup. `uv sync` performs an exact sync of `.venv`; use `uv sync --inexact` if you want to keep other packages already installed there.

The notebooks currently select Groq models. Create a `.env` file in the repository root with your key:

```dotenv
GROQ_API_KEY=your_key_here
```

The shared `LLMClient` also supports `OPENAI_API_KEY` and `GEMINI_API_KEY` if you adapt a notebook to select another provider. `.env` is ignored by Git. API calls require network access and may incur provider charges.

## Run the notebooks

Launch Jupyter with **`notebooks/` as the working directory**. The notebooks use paths such as `../data/...` and `../output/...`.

```powershell
cd notebooks
..\.venv\Scripts\jupyter.exe lab
```

On macOS or Linux, use `../.venv/bin/jupyter lab` in the second line. In Jupyter, select the Python kernel from this project's `.venv`, then run a notebook from top to bottom. If you launch Jupyter from another directory, relative data and output paths may fail.

| Notebook | What it does | Main output |
| --- | --- | --- |
| [`classifier.ipynb`](notebooks/classifier.ipynb) | Classifies sample messages by district, intent, and priority | `output/classified_messages.xlsx` |
| [`news_extraction.ipynb`](notebooks/news_extraction.ipynb) | Extracts structured flood events from news lines and validates them with Pydantic | `output/flood_report.xlsx` |
| [`rescue_planning.ipynb`](notebooks/rescue_planning.ipynb) | Scores incidents and asks the model to compare rescue strategies | `output/logistics_commander.md` |
| [`stability_test.ipynb`](notebooks/stability_test.ipynb) | Compares responses to the same scenarios at different temperatures | `output/stability_experiment.md` |
| [`budget_keeper.ipynb`](notebooks/budget_keeper.ipynb) | Counts message tokens and summarizes messages above a configured limit | `output/budget_keeper.md` |

The notebooks may overwrite their output files when run. Their examples are configured for Groq; change the provider and model selection in a notebook to use another supported service.

## Project layout

```text
config/       Model IDs, task defaults, routing rules, district list
data/         Sample messages, news feed, incidents, scenarios
notebooks/    Interactive experiments
output/       Reports and spreadsheets produced by notebooks
utils/        Shared Python helpers
```

Key utilities:

- `utils/config_loader.py` loads `config/config.yaml`; use `get_config().get("classification.districts")` for nested settings.
- `utils/router.py` selects a model from `config/models.yaml` based on provider and technique.
- `utils/prompts.py` stores and renders prompt templates.
- `utils/llm_client.py` wraps OpenAI, Google Gemini, and Groq calls with retries and usage reporting.
- `utils/token_utils.py` estimates prompt tokens. Estimates for non-OpenAI providers are approximate.
- `utils/json_utils.py` contains JSON extraction, repair, and validation helpers.

The [learning log](LEARNING_LOG.md) records experiments and debugging notes.
