from fastapi import FastAPI, HTTPException

from app.ollama_client import OllamaClientError, call_ollama
from app.prompts import build_program_prompt
from app.rules import apply_basic_rules
from app.schemas import ClientProfile, ProgramResponse
from app.validator import validate_program


app = FastAPI(
    title="coach-ai-api",
    description="API metier pour generer des programmes sportifs via Ollama.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/generate-program", response_model=ProgramResponse)
def generate_program(profile: ClientProfile) -> dict:
    constraints = apply_basic_rules(profile)
    prompt = build_program_prompt(profile, constraints)

    try:
        raw_program = call_ollama(prompt)
        return validate_program(raw_program, profile)
    except OllamaClientError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
