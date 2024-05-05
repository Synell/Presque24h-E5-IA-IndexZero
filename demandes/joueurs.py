from typing import Callable
from dataclasses import dataclass
from class_dict import ClassDict


@dataclass
class Joueur(ClassDict):
    num: int
    score: int
    valeur_attaque : int
    vie : int
    activite : str
    nombre_coffre: int
    valeur_butins: int


def joueurs(envoyer: Callable[[str], None], recevoir: Callable[[], str]) -> list[Joueur]:
    envoyer("JOUEURS")
    reponse = recevoir()

    if reponse.startswith("NOK"):
        print(reponse)
        return []

    resultat= []

    if reponse.startswith("NOK"):
        return resultat

    else:
        joueur_en_cours = reponse.split("|")
        for i, joueur in enumerate(joueur_en_cours, start = 1):
            valeurs = joueur.split(";")

            resultat.append(
                Joueur(
                    i,
                    int(valeurs[0]),
                    int(valeurs[1]),
                    int(valeurs[2]),
                    valeurs[3],
                    int(valeurs[4]),
                    int(valeurs[5])
                )
            )

    return resultat

