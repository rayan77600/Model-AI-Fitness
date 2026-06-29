from app.schemas import ClientProfile


def apply_basic_rules(profile: ClientProfile) -> list[str]:
    constraints: list[str] = []

    if profile.niveau.lower() == "debutant":
        constraints.append(
            "Limiter le volume, privilegier la technique et eviter les charges maximales."
        )

    douleurs = {douleur.lower() for douleur in profile.douleurs}
    if "lombaires" in douleurs or "lombaire" in douleurs:
        constraints.append(
            "Douleur lombaire: eviter deadlift lourd, good morning et rowing buste penche."
        )

    if profile.frequence == 2:
        constraints.append("Recommander une organisation full body.")
    elif profile.frequence == 3:
        constraints.append("Recommander full body ou split simple.")
    elif profile.frequence >= 4:
        constraints.append("Recommander upper/lower ou push/pull/legs.")

    return constraints
