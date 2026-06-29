from pydantic import BaseModel, Field, field_validator


class ClientProfile(BaseModel):
    objectif: str
    niveau: str
    frequence: int = Field(..., ge=1, le=7)
    duree_seance: int = Field(..., ge=15, le=180)
    materiel: list[str]
    douleurs: list[str] = Field(default_factory=list)

    @field_validator("objectif", "niveau")
    @classmethod
    def must_not_be_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Ce champ ne peut pas etre vide.")
        return value.strip()


class Exercise(BaseModel):
    nom: str
    series: int
    repetitions: str
    repos: str


class Session(BaseModel):
    seance: int
    titre: str
    exercices: list[Exercise]


class ProgramResponse(BaseModel):
    programme: list[Session]
