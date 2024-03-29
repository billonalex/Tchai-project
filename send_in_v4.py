"""

Script :
    - Liste des personnes

"""

#from db import *
import requests
import json
import hashlib
import time
from datetime import datetime
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

url_api = "http://127.0.0.1:5000/"

def hash_sha256(text):
    h = hashlib.sha256()
    h.update(text.encode('ascii'))
    return h.hexdigest()

def encrypt(message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.encrypt(str.encode(message))


def send(id_personne1, id_personne2, somme, private_key):
    record = {
        "personne1": id_personne1,
        "personne2": id_personne2,
        "temps": int(time.time()),
        "somme": somme
    }

    signature = sign_transaction(record, private_key)

    record["signature"] = signature
    #print(record)

    url = url_api + "records/v4/" + str(record["personne1"]) + "/" + str(record["personne2"]) + "/" + str(record["temps"]) + "/" + str(record["somme"]) + "/" + str(record["signature"])

    requests.post(url)

    return 1

def sign_transaction(record,private_key):
    pre_hash = str(record["personne1"]) + "|" + str(record["personne2"]) + "|" + str(int(record["temps"])) + "|" + str(record["somme"])
    hash = hash_sha256(pre_hash)
    signature = encrypt(hash, private_key)

    return signature

#Selectionne le destinataire de l'argent et le montant
def select_dest(id_exp):
    listeD = eval(requests.get(url_api + "personnes/").text)
    listeKeyD = ""
    print("\nA qui envoyer de l'argent ? ")
    for p in listeD:
        if (int(p[0]) != int(id_exp)):
            print(p[0],":", p[1],p[2])
            listeKeyD = listeKeyD + " " + str(p[0]) + " "
    print("r : Retour")
    inp = input("")
    #Retour
    if (inp.lower() == "r"):
        select_action(id_exp)
    #Selection compte a créditer
    elif (inp.lower() in listeKeyD):
        id_dest = int(inp.lower())
        #Choix du montant
        inp = input("Quel est le montant ? ")
        som = int(inp.lower())
        #Lecture clé privée
        filin = open("./private_key/" + id_exp + ".pem", "rb")
        priv_k = RSA.importKey(filin.read())
        filin.close()
        #Envoi enregistrement
        send(id_exp, id_dest, som, priv_k)
        print("\nArgent envoyé !\n")
        select_action(id_exp)


#Choix action utilisateur
def select_action(id_user):
    print("Que voulez-vous faire ?\n1 : Afficher mon solde\n2 : Afficher mes informations\n3 : Regarder mes transactions\n4 : Envoyer de l'argent\n5 : Supprimer mon compte\nd : Se déconnecter\nq : Quitter")
    inp = input("")
    #Se déconnecter
    if (inp.lower() == "d"):
        print("Déconnexion...")
    #Quitter
    elif (inp.lower() == "q"):
        exit()
    #Affichage solde
    elif (int(inp.lower()) == 1):
        solde = eval(requests.get(url_api + "solde/" + id_user).text)
        print("\nSolde :", solde,"\nEnter pour continuer")
        inp = input("")
        select_action(id_user)
    #Affichage informations
    elif (int(inp.lower()) == 2):
        info = eval(requests.get(url_api + "personnes/" + id_user).text)
        print("\n",info,"\nEnter pour continuer")
        inp = input("")
        select_action(id_user)
    #Regarder transactions
    elif (int(inp.lower()) == 3):
        record = eval(requests.get(url_api + "records/" + id_user).text)
        print("\n",record,"\nEnter pour continuer")
        inp = input("")
        select_action(id_user)
    #Envoyer argent
    elif (int(inp.lower()) == 4):
        select_dest(id_user)
    #Supprimer compte
    elif (int(inp.lower()) == 5):
        requests.delete(url_api + "personnes/" + str(id_user))
        print("\nCompte supprimé")
        menu()


#Selectionne l'utilisateur
def connection_user():
    u = -1
    listeP = eval(requests.get(url_api + "personnes/").text)
    #listeP = select_personnes(db_path)
    listeKey = ""
    print("\nBonjour, qui êtes vous ? ")
    for p in listeP:
        print(p[0],":", p[1],p[2])
        listeKey = listeKey + " " + str(p[0]) + " "
    print("q : Quitter")
    inp = input("")
    #Quitter
    if (inp.lower() == "q"):
        exit()
    #Selection compte a connecter
    elif (inp.lower() in listeKey):
        u = int(inp.lower())
        cpt = 0
        ind_user = 0
        for p in listeP:
            if (p[0] == int(inp.lower())):
                ind_user = cpt
            cpt+=1
        
        #AJOUTER VERIFICATION PASSWORD

        print("\nBonjour", listeP[ind_user][2], listeP[ind_user][1])
        select_action(inp.lower())


def creation_user():
    inp = input("Entrer votre nom : ")
    nom = inp.lower()
    inp = input("Entrer votre prénom : ")
    prenom = inp.lower()
    inp = input("Entrer votre adresse mail : ")
    adresseM = inp.lower()
    inp = input("Entrer votre mot de passe : ")
    mdp = inp.lower()
    headers = {'content-type': 'application/json'}
    res = requests.post(url_api + "personnes/v4/" + nom + "/" + prenom + "/" + adresseM + "/" + mdp, headers)
    #add_personne_v4_RSA(db_path, p)
    print("Création terminée\n")
    menu()

#Choix premier
def menu():
    print("\nBienvenu sur Tchai, que voulez-vous faire ?\n1: Se connecter\n2 : Créer un compte\nq : Quitter")
    inp = input("")
    #Quitter
    if (inp.lower() == "q"):
        exit()
    #Se connecter
    elif (int(inp.lower()) == 1):
        connection_user()
    #Crer un compte
    elif (int(inp.lower()) == 2):
        creation_user()


while(True):
    menu()