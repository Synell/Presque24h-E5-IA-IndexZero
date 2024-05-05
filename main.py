# Ces fonctions sont utilisés pour communiquer avec le serveur
from commandes import *
from demandes import *

# Ce module permet de se connecter au serveur, ne pas toucher
from connection import connect

# Connection au serveur
envoyer, recevoir, n_equipe = connect()
id_equipe = int(n_equipe) - 1
# ex: envoyer("commande")
# numero_equipe == "1" ou "2" ou "3" ou "4"
e, r = envoyer, recevoir



def decide(self: Joueur, others: list[Joueur], routes: list[Route], tour: int) -> None:
    my_turn = len([j for j in others if j.activite != 'AUCUNE']) + 1
    nb_joueurs = len(others) + 1
    n_actions = 0


    if self.vie <= max(len(list(filter(lambda x: x.valeur_attaque > self.valeur_attaque, others))), 2):
        reparer(e, r)
        return


    if ((self.nombre_coffre and tour == 120) or (self.nombre_coffre >= 3)):
        receler(e, r)
        return


    max_score_moyen_j: list[Joueur] = sorted(
        list(filter(lambda o: o.activite.startswith('PILLER') and self.valeur_attaque >= o.valeur_attaque, others)),
        key = lambda j: j.score / j.nombre_coffre if j.nombre_coffre else 0,
        reverse = True
    )
    if max_score_moyen_j:
        max_score_moyen_j: Joueur = max_score_moyen_j[0]
        max_score_moyen = max_score_moyen_j.score / max_score_moyen_j.nombre_coffre if max_score_moyen_j.nombre_coffre else 0

    else:
        max_score_moyen_j: None = None
        max_score_moyen = 0

    power = sorted([j for j in others if j.activite == 'AUCUNE'], key = lambda j: j.valeur_attaque, reverse = True)
    power = list(filter(lambda j: self.valeur_attaque >= j.valeur_attaque, power))

    if power:
        while self.valeur_attaque <= power[0].valeur_attaque and self.score >= 500 and n_actions < 12 and my_turn != nb_joueurs:
            closest = sorted(routes, key = lambda x: x.valeur_attaque - self.valeur_attaque)
            closest = list(filter(lambda x: x.valeur_attaque > self.valeur_attaque, closest))
            if not closest: break
            if closest[0].valeur_attaque - self.valeur_attaque > 50: break

            recruter(e, r)
            self.valeur_attaque += 5
            self.score -= 500
            n_actions += 1

    sorted_routes = sorted(routes, key=lambda x: (x.valeur_coffres + [0])[len(x.joueurs)], reverse = True)
    sorted_routes = list(filter(lambda x: not x.presence_monstre, sorted_routes))

    if (max_score_moyen_j) and (max_score_moyen > sorted_routes[0].valeur_coffres[len(sorted_routes[0].joueurs)] and self.valeur_attaque >= sorted_routes[0].valeur_attaque):
        trahir(e, r, max_score_moyen_j.num)
        return

    if self.nombre_coffre >= 2 and my_turn != nb_joueurs:
        receler(e, r)
        return


    if sorted_routes:
        while self.valeur_attaque < sorted_routes[0].valeur_attaque and self.score >= 500 and n_actions < 12:
            recruter(e, r)
            self.score -= 500
            n_actions += 1


    for route in sorted_routes:
        if route.valeur_attaque > self.valeur_attaque:
            continue

        if self.valeur_attaque >= route.valeur_attaque:
            piller(e, r, routes.index(route) + 1)
            return


    if self.nombre_coffre:
        receler(e, r)
        return


    reparer(e, r)
    return





while(True) :
    requete = r()
    if (requete.startswith("DEBUT_TOUR")):
        req_split = requete.split('|')
        tour = int(req_split[1])

    else:
        raise Exception ("pas debut de tour ?")

    list_joueurs = joueurs(e, r)
    list_routes = routes(e, r, list_joueurs)

    decide(list_joueurs.pop(id_equipe), list_joueurs, list_routes, tour)
    # res = r()
    # if (res != "OK"):
    #     print('erreur', res)
    #     break

    # e("FIN_TOUR")
    # r()
