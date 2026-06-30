from app.schemas import ClientProfile


PAIN_RULES = {
    "genou": [
        "Douleur genou: privilegier squat ou leg press avec amplitude toleree, split squat adapte, step-up bas, hip hinge et cardio doux si non douloureux.",
        "Douleur genou: eviter sauts repetes, course agressive, changements brusques de volume et flexion profonde chargee si douloureuse.",
    ],
    "genoux": [
        "Douleur genou: privilegier squat ou leg press avec amplitude toleree, split squat adapte, step-up bas, hip hinge et cardio doux si non douloureux.",
        "Douleur genou: eviter sauts repetes, course agressive, changements brusques de volume et flexion profonde chargee si douloureuse.",
    ],
    "epaule": [
        "Douleur epaule: privilegier rowing, tirages horizontaux, developpe prise neutre si tolere, landmine press, pompes inclinees et stabilite scapulaire.",
        "Douleur epaule: eviter developpe au-dessus de la tete si douloureux, dips irritants, prises trop larges, amplitudes forcees et mouvements derriere la nuque.",
    ],
    "epaules": [
        "Douleur epaule: privilegier rowing, tirages horizontaux, developpe prise neutre si tolere, landmine press, pompes inclinees et stabilite scapulaire.",
        "Douleur epaule: eviter developpe au-dessus de la tete si douloureux, dips irritants, prises trop larges, amplitudes forcees et mouvements derriere la nuque.",
    ],
    "lombaire": [
        "Douleur lombaire: privilegier hip hinge propre et controle, machines stables, unilateral work, gainage anti-extension, anti-rotation, respiration et bracing.",
        "Douleur lombaire: eviter deadlift lourd, good morning, rowing buste penche, charges mal controlees en flexion lombaire et fatigue excessive avec technique degradee.",
    ],
    "lombaires": [
        "Douleur lombaire: privilegier hip hinge propre et controle, machines stables, unilateral work, gainage anti-extension, anti-rotation, respiration et bracing.",
        "Douleur lombaire: eviter deadlift lourd, good morning, rowing buste penche, charges mal controlees en flexion lombaire et fatigue excessive avec technique degradee.",
    ],
    "bas du dos": [
        "Douleur lombaire: privilegier hip hinge propre et controle, machines stables, unilateral work, gainage anti-extension, anti-rotation, respiration et bracing.",
        "Douleur lombaire: eviter deadlift lourd, good morning, rowing buste penche, charges mal controlees en flexion lombaire et fatigue excessive avec technique degradee.",
    ],
    "coude": [
        "Douleur coude: privilegier prises neutres, charges moderees, volume de poussee/tirage mieux reparti et travail d'avant-bras progressif.",
        "Douleur coude: eviter les prises qui irritent et les gros volumes de poussee ou tirage concentres sur une seule seance.",
    ],
    "coudes": [
        "Douleur coude: privilegier prises neutres, charges moderees, volume de poussee/tirage mieux reparti et travail d'avant-bras progressif.",
        "Douleur coude: eviter les prises qui irritent et les gros volumes de poussee ou tirage concentres sur une seule seance.",
    ],
    "poignet": [
        "Douleur poignet: privilegier prises neutres, charges moderees et amplitudes controlees.",
        "Douleur poignet: eviter barres ou prises irritantes et extension de poignet agressive.",
    ],
    "poignets": [
        "Douleur poignet: privilegier prises neutres, charges moderees et amplitudes controlees.",
        "Douleur poignet: eviter barres ou prises irritantes et extension de poignet agressive.",
    ],
    "hanche": [
        "Douleur hanche: privilegier pont fessier, hip thrust, RDL, travail unilateral controle et mobilite douce si elle aide.",
        "Douleur hanche: eviter amplitudes forcees et mouvements qui pincent l'aine ou la hanche.",
    ],
    "hanches": [
        "Douleur hanche: privilegier pont fessier, hip thrust, RDL, travail unilateral controle et mobilite douce si elle aide.",
        "Douleur hanche: eviter amplitudes forcees et mouvements qui pincent l'aine ou la hanche.",
    ],
    "cheville": [
        "Douleur cheville/pied: privilegier mollets, tibial anterior, proprioception, marche progressive et equilibre.",
        "Douleur cheville/pied: eviter impact excessif et course si la tolerance est basse.",
    ],
    "chevilles": [
        "Douleur cheville/pied: privilegier mollets, tibial anterior, proprioception, marche progressive et equilibre.",
        "Douleur cheville/pied: eviter impact excessif et course si la tolerance est basse.",
    ],
    "pied": [
        "Douleur cheville/pied: privilegier mollets, tibial anterior, proprioception, marche progressive et equilibre.",
        "Douleur cheville/pied: eviter impact excessif et course si la tolerance est basse.",
    ],
    "pieds": [
        "Douleur cheville/pied: privilegier mollets, tibial anterior, proprioception, marche progressive et equilibre.",
        "Douleur cheville/pied: eviter impact excessif et course si la tolerance est basse.",
    ],
    "cou": [
        "Douleur cou: privilegier posture neutre, travail du haut du dos et exercices sans tension cervicale excessive.",
        "Douleur cou: eviter haussements d'epaules charges et mouvements qui compressent ou crispent le cou.",
    ],
}


def apply_basic_rules(profile: ClientProfile) -> list[str]:
    constraints: list[str] = []

    if profile.niveau.lower() == "debutant":
        constraints.append(
            "Limiter le volume, privilegier la technique et eviter les charges maximales."
        )
        constraints.append("Garder 1 a 3 repetitions en reserve sur la plupart des series.")

    douleurs = {douleur.lower() for douleur in profile.douleurs}
    for douleur in douleurs:
        constraints.extend(PAIN_RULES.get(douleur, []))

    if douleurs:
        constraints.append(
            "Si une douleur vive, un gonflement, un blocage, une irradiation, une instabilite ou une perte de force apparait, reduire la contrainte et recommander un professionnel de sante."
        )

    if profile.frequence == 2:
        constraints.append("Recommander une organisation full body.")
    elif profile.frequence == 3:
        constraints.append("Recommander full body ou split simple.")
    elif profile.frequence >= 4:
        constraints.append("Recommander upper/lower ou push/pull/legs.")

    constraints.append("Definir une progression simple et mesurable.")
    constraints.append("Prioriser les exercices utiles, non redondants et compatibles avec le temps disponible.")
    constraints.append("Prevoir des jours de recuperation reels dans la semaine.")

    return constraints
