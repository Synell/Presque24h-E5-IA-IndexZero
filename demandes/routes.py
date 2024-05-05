from typing import Callable
from class_dict import ClassDict
from dataclasses import dataclass
from .joueurs import Joueur


@dataclass
class Route(ClassDict):
    niveau_bateau: int
    valeur_attaque: int
    valeur_coffres: list[int]
    presence_monstre: bool
    joueurs: list[Joueur]


def routes(envoyer: Callable[[str], None], recevoir: Callable[[], str], joueurs: list[Joueur] = []) -> list[Route]:
    envoyer('ROUTES')

    reponse = recevoir()

    if 'NOK' in reponse:
        print(reponse)
        return []

    ret = []
    routes = reponse.split('|')

    for i, route in enumerate(routes, start = 1):
        if route == '': continue

        values = route.split(';')

        ret.append(
            Route(
                niveau_bateau = int(values.pop(0)),
                valeur_attaque = int(values.pop(0)),
                valeur_coffres = [int(values.pop(0)) for _ in range(3)],
                presence_monstre = values.pop(0).lower() == 'true',
                joueurs = [j for j in joueurs if j.activite == f'PILLER{i}']
            )
        )

    return ret
