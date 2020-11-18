# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:40:42 2020

@author: Alexandre
"""

"""
Requêtes API :
    - Ajouter une personne                                                      : POST /personne/<nom>/<prenom>                         : INSERT INTO personne (nom,prenom) VALUES ("BILLON", "Alexandre")
    - Supprimer une personne                                                    : DELETE /personne/<id>                                 : DELETE FROM personne WHERE id=1
    - Consulter la liste des personnes                                          : GET /personnes                                        : SELECT * FROM personne (ORDER BY nom,prenom)
    - Informations d'une personne via son id                                    : GET /personnes/<id>                                   : SELECT * FROM personne WHERE id=1

    - Effectuer une transaction                                                 : POST /records/<personne1>/<personne2>/<somme>         : INSERT INTO records (personne1,personne2,temps,somme) VALUES (1,2,155615521,1565.54)
    - Annuler une transaction                                                   : DELETE /records/<id>                                  : DELETE FROM records WHERE id=1
    - Consulter les transactions dans l'ordre chronologique                     : GET /records                                          : SELECT * FROM records (order by temps ASC)
    - Consulter les transactions dans l'ordre chronologique pour une personne   : GET /records/<personne>                               : SELECT * FROM records WHERE personne1=1 (order by temps ASC)
    - Afficher le solde d'une personne                                          : GET /solde/<personne>                                 : SELECT SUM(somme) AS solde FROM records WHERE personne1=1

"""

import sqlite3
import json
from flask import *
from db import *

db_path = "db/tchai.db"

conn = None

app = Flask(__name__)

records = select_records(db_path)
print(records)
personne = select_personnes(db_path)
print(personne)

names = [e[1] for e in personne]

@app.route('/personnes', methods=['GET'])
def liste_personne():
    return str(select_personnes(db_path))

@app.route('/personnes/<id>', methods=['GET'])
def get_personne_by_id(id):
    return str(get_personne(db_path,int(id)))

@app.route('/personnes/<nom>/<prenom>', methods=['POST'])
def new_personne(nom, prenom):
    p = {
        "nom": nom,
        "prenom": prenom
    }
    add_personne(db_path, p)

#@app.route('/personnes/<id>', methods=['DELETE'])
#delete_personne(db_path, int(id))


@app.route('/')
def hello():
    return 'Hello <ul>'+''.join(['<li>'+ n for n in names]) +'</ul>\n', 200
    
@app.route('/user/<uname>', methods=['PUT'])
def add (uname):
    names.append(uname)
    return 'User '+ uname +' added.\n', 201
    
@app.route('/user/<uname>', methods=['DELETE'])
def rem (uname):
    if uname not in names:
        return 'User '+ uname +' does not exists.\n', 404
    
    names.remove(uname)
    return 'User '+ uname +' removed.\n', 200
    
app.run(host='127.0.0.1', debug=True)

