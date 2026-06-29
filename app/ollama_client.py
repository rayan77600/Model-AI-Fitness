import json

import requests

from app.config import MODEL_NAME, OLLAMA_URL, REQUEST_TIMEOUT


class OllamaClientError(RuntimeError):
    pass


def call_ollama(prompt: str) -> dict:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "format": "json",
    }

    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.Timeout as exc:
        raise OllamaClientError(
            f"Ollama n'a pas repondu avant le timeout de {REQUEST_TIMEOUT} secondes."
        ) from exc
    except requests.ConnectionError as exc:
        raise OllamaClientError(
            f"Impossible de joindre Ollama a l'adresse {OLLAMA_URL}."
        ) from exc
    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "inconnu"
        raise OllamaClientError(
            f"Ollama a retourne une erreur HTTP {status_code}."
        ) from exc
    except requests.RequestException as exc:
        raise OllamaClientError(f"Erreur pendant l'appel a Ollama: {exc}") from exc

    try:
        ollama_payload = response.json()
    except ValueError as exc:
        raise OllamaClientError("La reponse HTTP d'Ollama n'est pas un JSON valide.") from exc

    raw_model_response = ollama_payload.get("response")
    if not isinstance(raw_model_response, str):
        raise OllamaClientError("La reponse Ollama ne contient pas de champ 'response' valide.")

    try:
        parsed_response = json.loads(raw_model_response)
    except json.JSONDecodeError as exc:
        raise OllamaClientError("Le modele n'a pas retourne un JSON valide.") from exc

    if not isinstance(parsed_response, dict):
        raise OllamaClientError("Le JSON retourne par le modele doit etre un objet.")

    return parsed_response
