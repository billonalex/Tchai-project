# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:40:42 2020

@author: Alexandre

Requêtes API :
    done - Ajouter une personne                                                                 : POST /personne/<nom>/<prenom>                         : INSERT INTO personne (nom,prenom) VALUES ("BILLON", "Alexandre")
    done - Supprimer une personne                                                               : DELETE /personne/<id>                                 : DELETE FROM personne WHERE id=1
    done - Consulter la liste des personnes                                                     : GET /personnes                                        : SELECT * FROM personne (ORDER BY nom,prenom)
    done - Informations d'une personne via son id                                               : GET /personnes/<id>                                   : SELECT * FROM personne WHERE id=1

    done - Effectuer une transaction                                                            : POST /records/<personne1>/<personne2>/<somme>         : INSERT INTO records (personne1,personne2,temps,somme) VALUES (1,2,155615521,1565.54)
    done - Annuler une transaction                                                              : DELETE /records/<id>                                  : DELETE FROM records WHERE id=1
    done - Consulter les transactions dans l'ordre chronologique                                : GET /records                                          : SELECT * FROM records (order by temps ASC)
    done - Consulter les transactions dans l'ordre chronologique pour une personne              : GET /records/<personne>                               : SELECT * FROM records WHERE personne1=1 (order by temps ASC)
    done - Afficher le solde d'une personne                                                     : GET /solde/<personne>                                 : SELECT SUM(somme) AS solde FROM records WHERE personne1=1

    done - Vérifier l'intégrité des données                                                     : GET /check/data/                                      : SELECT * FROM records (order by temps ASC)
    done - Vérifier l'intégrité d'un enregistrement                                             : GET /check/data/<id>                                  : SELECT * FROM records WHERE id=1 (order by temps ASC)

    done - Effectuer une transaction en tenant compte du hash de la plus récente transaction         : POST /records/v3/<personne1>/<personne2>/<somme>      : SELECT id from records WHERE temps = (SELECT MAX(temps) FROM records)
"""

import sqlite3
import json
import os
from flask import *
from flask import send_from_directory
from db import *

db_path = "db/tchai.db"
conn = None
app = Flask(__name__)
names = [e[1] + " " + e[2] for e in select_personnes(db_path)]

# Let's define some routes :

@app.route('/')
def hello():
    return 'Hello <ul>'+''.join(['<li>'+ n for n in names]) +'</ul>\n', 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
    return ""

@app.route('/personnes/<id>', methods=['DELETE'])
def rm_per(id):
    delete_personne(db_path, int(id))

@app.route('/records/', methods=['GET'])
def liste_records():
    return str(select_records(db_path))

@app.route('/records/<personne>', methods=['GET'])
def liste_records_personne1(personne):
    return str(get_record_by_personne1(db_path, int(personne)))

@app.route('/records/<personne1>/<personne2>/<somme>', methods=['POST'])
def new_record(personne1, personne2, somme):
    record = {
        "personne1" : personne1,
        "personne2" : personne2,
        "somme" : somme
    }
    add_record(db_path, record)
    return ""

@app.route('/records/v3/<personne1>/<personne2>/<somme>', methods=['POST'])
def new_record_v3(personne1, personne2, somme):
    record = {
        "personne1" : personne1,
        "personne2" : personne2,
        "somme" : somme
    }
    add_record_v3(db_path, record)
    return ""

@app.route('/records/<id>', methods=['DELETE'])
def del_record(id):
    delete_record(db_path, id)

@app.route('/solde/<personne>', methods=['GET'])
def solde_personne(personne):
    return str(get_solde(db_path, int(personne)))

@app.route('/check/data', methods=['GET'])
def check():
    return str(check_hash(db_path))   

@app.route('/check/data/v3', methods=['GET'])
def check_v3():
    return str(check_hash_v3(db_path))  

@app.route('/check/data/<id>', methods=['GET'])
def check_by_id(id):
    return str(check_hash_by_id(db_path, id))    

# Why won't we run our app ?
app.run(host='127.0.0.1', debug=True)