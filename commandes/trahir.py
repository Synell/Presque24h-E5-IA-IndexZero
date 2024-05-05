def trahir(envoyer, recevoir, argument1_numero_cible):
    if isinstance(argument1_numero_cible, int):
        argument1_numero_cible = str(argument1_numero_cible) # Transforme l'int en integer
        
    envoyer("TRAHIR"+"|"+argument1_numero_cible)

    reponse = recevoir()

    if reponse == "OK":
        return(True)
    if "NOK" in reponse :
        print(reponse)
        return(False)