# Regles de programmation fitness

Ce document resume les fichiers transmis comme base metier exploitable par l'API.
Il ne s'agit pas encore de RAG: ces regles servent a cadrer le prompt et les validations futures.

## Checklist client

- Identifier le profil de depart: age, sexe, taille, poids, niveau, frequence, materiel, temps disponible, sommeil et stress.
- Clarifier un objectif prioritaire unique: prise de masse, seche, recomposition corporelle, force ou performance sportive.
- Reperer les contraintes: douleurs actuelles, blessures recentes, mouvements interdits, exercices toleres et signaux d'alerte.
- Construire le programme en definissant d'abord la frequence, puis le split, puis les exercices.
- Garder une progression simple et mesurable.
- Prioriser la technique avant la charge.
- Garder 1 a 3 repetitions en reserve sur la plupart des series.
- Eviter les exercices inutiles ou redondants.
- Prevoir des jours de recuperation reels.

## Signaux d'alerte douleur

Si un mouvement provoque une douleur articulaire vive, il faut modifier l'exercice, l'amplitude, la charge, la vitesse ou remplacer le mouvement.
Si la douleur augmente pendant la seance ou dans les jours suivants, il faut reduire la contrainte.
En cas de gonflement, blocage, instabilite, irradiation ou perte de force, le programme doit orienter vers un professionnel de sante.

## Adaptations par zone

- Genoux: privilegier amplitude toleree, leg press, split squat adapte, step-up bas, hip hinge et cardio doux. Eviter sauts repetes, course agressive, changement brutal de volume et flexion profonde chargee si douloureuse.
- Epaules: privilegier rowing, tirages horizontaux, prise neutre, landmine press, pompes inclinees et stabilite scapulaire. Eviter overhead press douloureux, dips irritants, prises trop larges et mouvements derriere la nuque.
- Bas du dos: privilegier hip hinge propre, machines stables, unilateral work, gainage anti-extension, anti-rotation, respiration et bracing. Eviter deadlift lourd, good morning, rowing buste penche et fatigue excessive avec technique degradee.
- Coudes et poignets: privilegier prises neutres, charges moderees, volume mieux reparti et travail progressif. Eviter prises irritantes et extension de poignet agressive.
- Hanches: privilegier pont fessier, hip thrust, RDL, travail unilateral controle et mobilite douce. Eviter amplitudes forcees et mouvements qui pincent.
- Chevilles et pieds: privilegier mollets, tibial anterior, proprioception, marche progressive et equilibre. Eviter impact excessif et course si la tolerance est basse.
- Cou: privilegier posture neutre et travail du haut du dos. Eviter haussements d'epaules charges et mouvements qui crispent le cou.

## Sortie attendue

La sortie API reste volontairement simple pour le site web:

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

Les blocs nutrition, recuperation, suivi et ajustement pourront devenir des schemas dedies plus tard.
