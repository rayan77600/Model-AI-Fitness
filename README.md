# coach-ai-api

`coach-ai-api` est une API FastAPI qui sert de couche metier entre un site web et Ollama.
Le site envoie un profil sportif a l'API, l'API construit un prompt controle, appelle Ollama avec un modele Qwen, valide la reponse et retourne un JSON exploitable par le site.

Architecture:

```text
Site web -> API FastAPI -> Ollama API -> Qwen -> JSON -> Site web
```

Cette base ne contient pas de RAG et pas de fine-tuning LoRA. Elle est volontairement simple pour rester extensible.
Les premieres regles metier de programmation sportive sont integrees dans `app/rules.py` et resumees dans `docs/fitness-programming-rules.md`.

## Installation locale

```bash
cd coach-ai-api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copier ensuite les variables d'environnement:

```bash
copy .env.example .env
```

## Lancer l'API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

L'API sera disponible sur `http://localhost:8000`.

## Tester la route de sante

```bash
curl http://localhost:8000/health
```

Reponse attendue:

```json
{
  "status": "ok"
}
```

## Configurer Ollama

Les variables disponibles sont:

```env
OLLAMA_URL=http://ollama:11434
MODEL_NAME=qwen2.5:7b
REQUEST_TIMEOUT=120
```

En local, si Ollama tourne directement sur la machine, `OLLAMA_URL` peut etre:

```env
OLLAMA_URL=http://localhost:11434
```

Le modele doit etre disponible dans Ollama:

```bash
ollama pull qwen2.5:7b
```

Si Ollama n'est pas disponible, `/generate-program` retourne une erreur claire avec le statut HTTP 503.

## Tester /generate-program

```bash
curl -X POST http://localhost:8000/generate-program \
  -H "Content-Type: application/json" \
  -d '{
    "objectif": "prise_muscle",
    "niveau": "debutant",
    "frequence": 3,
    "duree_seance": 45,
    "materiel": ["salle"],
    "douleurs": ["lombaires"]
  }'
```

Reponse attendue:

```json
{
  "programme": [
    {
      "seance": 1,
      "titre": "Full body",
      "exercices": [
        {
          "nom": "Presse a cuisses",
          "series": 3,
          "repetitions": "10-12",
          "repos": "90 sec"
        }
      ]
    }
  ]
}
```

## Pourquoi FastAPI au-dessus d'Ollama

Le site web ne doit pas appeler Ollama directement. FastAPI joue le role d'API metier intermediaire:

- validation des donnees d'entree avec Pydantic;
- construction d'un prompt controle;
- ajout progressif de regles metier;
- gestion des erreurs Ollama;
- validation du JSON retourne par le modele;
- contrat stable pour le site web.

Cette separation permettra d'ajouter plus tard du RAG, de nouvelles regles, de l'observabilite ou une authentification sans exposer Ollama au client.
