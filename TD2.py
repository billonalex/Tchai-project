# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 2020

@author: noemi
"""

from flask import *

app = Flask(__name__)
names = ['Zorro']

def save() :
    fichier = open("LNom.txt", "w")
    for n in names :
        fichier.write(n + "\n")
    fichier.close()

@app.route('/')
def hello():    
    return 'Hello <ul>'+''.join(
            ['<li>'+ n for n in names]
            ) +'</ul>\n', 200
    

@app.route('/user/<uname>', methods=['PUT'])
def add (uname):
    names.append(uname)
    save()
    return 'User '+ uname +' added.\n', 201
    
@app.route('/user/<uname>', methods=['DELETE'])
def rem (uname):
    if uname not in names:
        return 'User '+ uname +' does not exists.\n', 404
    names.remove(uname)
    save()
    return 'User '+ uname +' removed.\n', 200
    
app.run(host='0.0.0.0', debug=True)