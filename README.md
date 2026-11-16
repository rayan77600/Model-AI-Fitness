# Fitness Program Generation API

A Python/FastAPI service that turns a fitness profile into a structured workout-program request for an Ollama-hosted language model. It demonstrates API design, prompt construction, business rules and response validation.

## Architecture

```text
Client -> Pydantic validation -> rule-based prompt constraints
       -> Ollama /api/generate -> JSON/schema validation -> API response
```

**Stack:** Python, FastAPI, Pydantic, Requests, python-dotenv, Ollama and pytest. A Dockerfile is included. The default model is `qwen2.5:7b`.

## Implemented behavior

- `GET /health` returns `{"status":"ok"}`.
- `POST /generate-program` accepts goals, experience level, frequency, duration, equipment and reported pain.
- Input validation constrains frequency to 1–7 sessions and duration to 15–180 minutes.
- Rule-based constraints are included in the model prompt.
- Output validation checks JSON shape, required exercise fields, Pydantic schema and session count.
- Upstream errors map to HTTP 503; invalid program output maps to HTTP 422.

API field names are French; [`app/schemas.py`](app/schemas.py) defines the contract. Structural validation does not establish exercise suitability or model recommendation quality.

## Verified local setup

Dependency installation and existing tests were verified with Python 3.10.11. From the repository root:

```sh
python -m venv .venv
```

Activate the environment using your shell, then:

```sh
python -m pip install -r requirements.txt
python -m pytest -q
```

The ASGI application is `app.main:app`. The health route was verified in-process using FastAPI's test client. Live Uvicorn startup, Docker builds and real model generation were not exercised during review.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `OLLAMA_URL` | `http://ollama:11434` | Reachable Ollama server address |
| `MODEL_NAME` | `qwen2.5:7b` | Model available on that server |
| `REQUEST_TIMEOUT` | `120` | Request timeout in seconds |

The health endpoint does not check Ollama availability. Dependencies are unpinned and may resolve differently in future installations.

## Tests and evaluation

The existing suite contains one health test and two rule tests for lumbar and shoulder constraints. All three passed during review. No training scripts, fine-tuning pipeline, dataset, benchmark metrics or model-quality evaluation were found. This is an LLM integration project.

## Source map

- [`app/main.py`](app/main.py): endpoints and error handling.
- [`app/rules.py`](app/rules.py) and [`app/prompts.py`](app/prompts.py): constraints and prompt construction.
- [`app/ollama_client.py`](app/ollama_client.py): upstream HTTP calls and JSON decoding.
- [`app/validator.py`](app/validator.py): output validation.
- [`tests`](tests): automated tests.
