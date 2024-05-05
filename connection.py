from socket import *
from typing import Callable

def connect() -> tuple[Callable[[str], None], Callable[[], str], str]:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(("127.0.0.1", 1234))

    def envoyer(to_send: str) -> None:
        print("Envoi de message : ", to_send)
        if isinstance(to_send, str):
            to_send = to_send.encode()
        sock.send(to_send+b"\r\n")

    def recevoir(byte_length: int = 1024) -> str:
        print("En attente de message : ", end="")
        recu = sock.recv(byte_length).decode().replace("\r\n", "")
        if recu[-1] == '|': recu = recu[:-1]
        print(recu)
        if recu=="FIN": 
            sock.close() 
            exit()
        return(recu)


    premier_message_serveur = recevoir()
    if premier_message_serveur.startswith("NOM_EQUIPE"):
        print("Connection établi")
        envoyer("IndexZer0")
        numero_equipe = recevoir().split("|")[-1]
        print("Numéro équipe", numero_equipe)

    return(envoyer, recevoir, numero_equipe)
