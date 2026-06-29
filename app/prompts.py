import json

from app.schemas import ClientProfile


def build_program_prompt(
    profile: ClientProfile,
    constraints: list[str] | None = None,
) -> str:
    constraints = constraints or []
    profile_json = profile.model_dump()

    return f"""
Tu es un coach sportif expert.

Genere un programme sportif personnalise pour le profil client suivant:
{json.dumps(profile_json, ensure_ascii=False, indent=2)}

Contraintes metier a respecter:
{json.dumps(constraints, ensure_ascii=False, indent=2)}

Regles de generation:
- Respecter exactement {profile.frequence} seance(s).
- Adapter le programme a l'objectif, au niveau, au materiel disponible et a la duree de seance.
- Tenir compte des douleurs ou blessures indiquees.
- Ne pas proposer d'exercices incompatibles avec les douleurs mentionnees.
- Repondre uniquement avec un objet JSON valide.
- Ne pas ajouter de texte avant ou apres le JSON.

Format JSON attendu:
{{
  "programme": [
    {{
      "seance": 1,
      "titre": "Full body",
      "exercices": [
        {{
          "nom": "Presse a cuisses",
          "series": 3,
          "repetitions": "10-12",
          "repos": "90 sec"
        }}
      ]
    }}
  ]
}}
""".strip()
