from app.rules import apply_basic_rules
from app.schemas import ClientProfile


def test_lumbar_pain_rules_are_applied() -> None:
    profile = ClientProfile(
        objectif="prise_muscle",
        niveau="debutant",
        frequence=3,
        duree_seance=45,
        materiel=["salle"],
        douleurs=["lombaires"],
    )

    constraints = apply_basic_rules(profile)
    joined_constraints = " ".join(constraints)

    assert "Douleur lombaire" in joined_constraints
    assert "deadlift lourd" in joined_constraints
    assert "full body ou split simple" in joined_constraints


def test_shoulder_pain_rules_are_applied() -> None:
    profile = ClientProfile(
        objectif="force",
        niveau="intermediaire",
        frequence=4,
        duree_seance=60,
        materiel=["salle"],
        douleurs=["epaules"],
    )

    constraints = apply_basic_rules(profile)
    joined_constraints = " ".join(constraints)

    assert "Douleur epaule" in joined_constraints
    assert "landmine press" in joined_constraints
    assert "upper/lower ou push/pull/legs" in joined_constraints
