# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:07:21 2020

@author: Alexandre
"""

import sqlite3
from sqlite3 import Error
import time

def select_records(db_path):
    rows = []
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM records"
        cur.execute(query)
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return rows

def select_personnes(db_path):
    rows = []
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM personne"
        cur.execute(query)
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return rows

def add_personne(db_path, personne):
    """
    personne = {
        "nom" : "BILLON",
        "prenom" : "Alexandre"
    }
    """
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        today = time.time()
        query = 'INSERT INTO personne (nom, prenom) VALUES ("' + personne["nom"] + '", "' + personne["prenom"] + '")'
        cur.execute(query)
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_record(db_path, record):
    """
    record = {
        "personne1" : "1",
        "personne2" : "2",
        "somme" : "144.56"
    }
    """

    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        today = time.time()
        query = 'INSERT INTO records (personne1, personne2, temps, somme) VALUES (' + str(record["personne1"]) + ',' + str(record["personne2"]) + ',' + str(int(today)) + ',' + str(record["somme"]) + ')'
        cur.execute(query)
        cur.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return rows