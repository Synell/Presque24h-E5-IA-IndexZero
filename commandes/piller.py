
def piller(envoyer, recevoir, argument1_route_commercial):
    if isinstance(argument1_route_commercial, int):
        argument1_route_commercial = str(argument1_route_commercial) # Transforme l'int en integer
        
    envoyer("PILLER"+"|"+argument1_route_commercial)

    reponse = recevoir()

    if reponse == "OK":
        return(True)
    if "NOK" in reponse :
        print(reponse)
        return(False)
    