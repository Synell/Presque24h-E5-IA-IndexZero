def reparer (envoyer,recevoir):

    envoyer("REPARER")

    reponse = recevoir()

    if reponse == "OK":
        return(True)
    if "NOK" in reponse :
        print(reponse)
        return(False)