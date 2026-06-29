from app.schemas import ClientProfile, ProgramResponse


def validate_program(program: dict, profile: ClientProfile) -> dict:
    if not isinstance(program, dict):
        raise ValueError("La reponse du modele doit etre un objet JSON.")

    if "programme" not in program:
        raise ValueError("La reponse du modele doit contenir la cle 'programme'.")

    sessions = program["programme"]
    if not isinstance(sessions, list):
        raise ValueError("La cle 'programme' doit contenir une liste de seances.")

    if len(sessions) != profile.frequence:
        raise ValueError(
            "Le nombre de seances ne correspond pas a la frequence demandee."
        )

    for session_index, session in enumerate(sessions, start=1):
        if not isinstance(session, dict):
            raise ValueError(f"La seance {session_index} doit etre un objet JSON.")

        exercices = session.get("exercices")
        if not isinstance(exercices, list):
            raise ValueError(
                f"La seance {session_index} doit contenir une liste d'exercices."
            )

        for exercise_index, exercise in enumerate(exercices, start=1):
            if not isinstance(exercise, dict):
                raise ValueError(
                    f"L'exercice {exercise_index} de la seance {session_index} doit etre un objet JSON."
                )

            missing_fields = {
                field
                for field in ("nom", "series", "repetitions", "repos")
                if field not in exercise
            }
            if missing_fields:
                fields = ", ".join(sorted(missing_fields))
                raise ValueError(
                    f"L'exercice {exercise_index} de la seance {session_index} ne contient pas: {fields}."
                )

    ProgramResponse.model_validate(program)
    return program
