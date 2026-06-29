import os

from dotenv import load_dotenv


load_dotenv()


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434").rstrip("/")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:7b")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "120"))
