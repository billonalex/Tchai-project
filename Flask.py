# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:40:42 2020

@author: Alexandre
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


