# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:40:42 2020

@author: Alexandre

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

names = [e[1] + " " + e[2] for e in select_personnes(db_path)]

@app.route('/')
def hello():
    return 'Hello <ul>'+''.join(['<li>'+ n for n in names]) +'</ul>\n', 200

@app.route('/personnes/', methods=['GET'])
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

@app.route('/personnes/<id>', methods=['DELETE'])
def rm_per(id):
    delete_personne(db_path, int(id))
    
app.run(host='127.0.0.1', debug=True)
