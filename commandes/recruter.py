def recruter(envoyer, recevoir):

    envoyer("RECRUTER")

    reponse = recevoir()

    if reponse == "OK":
        return(True)
    if "NOK" in reponse :
        print(reponse)
        return(False)
    