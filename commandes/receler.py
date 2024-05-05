def receler(envoyer, recevoir):
    
    envoyer("RECELER")

    reponse = recevoir()

    if reponse == "OK":
        return(True)
    if "NOK" in reponse :
        print(reponse)
        return(False)
    