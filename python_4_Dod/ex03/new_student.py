import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Génère un identifiant aléatoire de 15 lettres minuscules."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Représente un étudiant avec login et identifiant générés
    automatiquement."""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Valide les données et initialise login et id."""

        if not isinstance(self.name, str) or not isinstance(self.surname, str):
            raise TypeError("name and surname must be strings")

        if not self.name or not self.surname:
            raise ValueError("name and surname cannot be empty")

        self.login = self.name[0].upper() + self.surname
