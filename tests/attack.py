# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:01:51 2020

@author: Alexandre

Insertion des requêtes tests et d'attaque de la DB
"""

import requests
import json

#Utiliser ces variables !
address = "http://127.0.0.1:5000"

#print(requests.post('http://127.0.0.1:5000/personnes/NOM/Prenom').text)
#print(requests.delete('http://127.0.0.1:5000/personnes/4').text)
#print(requests.get('http://127.0.0.1:5000/personnes').text)
#print(requests.get('http://127.0.0.1:5000/personnes/1').text)

#print(requests.post('http://127.0.0.1:5000/records/2/1/50').text)
#print(requests.post('http://127.0.0.1:5000/records/v3/3/1/150').text)
print(requests.post('http://127.0.0.1:5000/personnes/v4/NOM4/Prenom4/np@gmail.com/passw').text)