# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:07:21 2020

@author: Alexandre

hash_sha256("1|2|1605721721|144")

"""

import sqlite3
from sqlite3 import Error
import time
import hashlib

def hash_sha256(text):
    h = hashlib.sha256()
    h.update(text.encode('ascii'))
    return h.hexdigest()

def hash_sha256_v3(text,previous_hash):
    text = text + "|" + previous_hash
    h = hashlib.sha256()
    h.update(text.encode('ascii'))
    return h.hexdigest()

def check_hash(db_path):
    rows = []
    conn = None
    false_lines = []

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM records"
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            calculated_hash = hash_sha256(str(row[0]) + "|" + str(row[1]) + "|" + str(row[2]) + "|" + str(row[3]))
            
            if(str(row[4]) != str(calculated_hash)):
                false_lines.append(row)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return false_lines
    
def check_hash_by_id(db_path, id):
    rows = []
    conn = None
    false_lines = []

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM records WHERE id=" + str(id)
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            calculated_hash = hash_sha256(str(row[0]) + "|" + str(row[1]) + "|" + str(row[2]) + "|" + str(row[3]))
            
            if(str(row[4]) != str(calculated_hash)):
                false_lines.append(row)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return false_lines

def select_records(db_path):
    rows = []
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM records ORDER BY temps ASC"
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

def get_personne(db_path,id):
    rows = []
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM personne WHERE id=" + str(id)
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

def delete_personne(db_path, id):
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        query = 'DELETE FROM personne WHERE id=' + id + ')'
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
        pre_hash = str(record["personne1"]) + "|" + str(record["personne2"]) + "|" + str(int(today)) + "|" + str(record["somme"])
        hash = hash_sha256(pre_hash)
        query = 'INSERT INTO records (personne1, personne2, temps, somme, hash) VALUES (' + str(record["personne1"]) + ',' + str(record["personne2"]) + ',' + str(int(today)) + ',' + str(record["somme"]) + ',"' + hash + '")'
        cur.execute(query)
        cur.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def delete_record(db_path, id):

    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        query = 'DELETE FROM records WHERE id=' + str(id)
        cur.execute(query)
        cur.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def get_record_by_personne1(db_path,id):
    rows = []
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM records WHERE personne1=" + str(id)
        cur.execute(query)
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return rows

def get_solde(db_path,id):
    rows = []
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT SUM(SOMME) FROM records WHERE personne1=" + str(id)
        cur.execute(query)
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return rows