# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:07:21 2020

@author: Alexandre

hash_sha256("1|2|1605721721|144")
hash_sha256_v3("1|2|1605721721|144", "25ae70e8e67e3f1f48227e70f603623cc72b26bda446ace306f61dad0101fc3d")

"""

from RSA import *

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
            calculated_hash = hash_sha256(str(row[1]) + "|" + str(row[2]) + "|" + str(row[3]) + "|" + str(row[4]))
            
            if(str(row[5]) != str(calculated_hash)):
                false_lines.append(row)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return false_lines

def check_hash_v3(db_path):
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

        for i in range(len(rows)):
            calculated_hash = ""

            if(i == 0):
                calculated_hash = hash_sha256(str(rows[i][1]) + "|" + str(rows[i][2]) + "|" + str(rows[i][3]) + "|" + str(rows[i][4]))
            else:
                calculated_hash = hash_sha256_v3(str(rows[i][1]) + "|" + str(rows[i][2]) + "|" + str(rows[i][3]) + "|" + str(rows[i][4]), str(rows[i-1][5]))
            
            if(str(rows[i][5]) != str(calculated_hash)):
                false_lines.append(rows[i])

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
            calculated_hash = hash_sha256(str(row[1]) + "|" + str(row[2]) + "|" + str(row[3]) + "|" + str(row[4]))
            
            if(str(row[5]) != str(calculated_hash)):
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
    res = []

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        rows = []
        query = "SELECT * FROM records ORDER BY temps ASC"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            #row.append(datetime.fromtimestamp(row[3]))
            #row = row + tuple(str(datetime.fromtimestamp(row[3])))
            res.append(list(row) + [str(datetime.fromtimestamp(row[3]))])
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return res

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

def add_personne_v4(db_path, personne):
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

        rows = []
        id_personne = -1
        select_query = "SELECT id FROM personne WHERE nom LIKE \"" + personne["nom"] + "\" AND prenom LIKE \"" + personne["prenom"] + "\""
        cur.execute(select_query)
        rows = cur.fetchall()
        for row in rows:
            id_personne = row[0]
        if id_personne != -1:
            write_key_in_db(conn, id_personne)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

#Ajout d'une personne avec nom, prénom, adresse mail + mot de passe en v4 avec clé RSA
def add_personne_v4_RSA(db_path, personne):
    """
    personne = {
        "nom" : "BILLON",
        "prenom" : "Alexandre"
        "mail" : "alexandre_billon@etu.u-bourgogne.fr"
        "password" : "alex"
    }
    """
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        today = time.time()
        query = 'INSERT INTO personne (nom, prenom, mail, password) VALUES ("' + personne["nom"] + '", "' + personne["prenom"] + '", "' + personne["mail"] + '", "' + personne["password"] + '")'
        cur.execute(query)
        conn.commit()

        rows = []
        id_personne = -1
        select_query = "SELECT id FROM personne WHERE nom LIKE \"" + personne["nom"] + "\" AND prenom LIKE \"" + personne["prenom"] + "\""
        cur.execute(select_query)
        rows = cur.fetchall()
        for row in rows:
            id_personne = row[0]
        if id_personne != -1:
            write_key_in_db(conn, id_personne)

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
        query = 'DELETE FROM personne WHERE id=' + str(id) + ')'
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
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_record_v3(db_path, record):
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

        #On récupère le hash de la plus récente transaction
        previous_hash = ""
        query_hash = "SELECT hash from records WHERE temps = (SELECT MAX(temps) FROM records)"
        cur.execute(query_hash)
        rows = cur.fetchall()

        if(len(rows) == 0): #On est sur la première transaction
            today = time.time()
            pre_hash = str(record["personne1"]) + "|" + str(record["personne2"]) + "|" + str(int(today)) + "|" + str(record["somme"])
            hash = hash_sha256(pre_hash)

        else: #Il y a déjà une transaction dans la base, on peut utiliser le hash précédent !
            for row in rows:
                previous_hash = row[0]
            today = time.time()
            pre_hash = str(record["personne1"]) + "|" + str(record["personne2"]) + "|" + str(int(today)) + "|" + str(record["somme"])
            hash = hash_sha256_v3(pre_hash, previous_hash) #On crée notre hash en tenant compte du hash précédent

        #On insère l'enregistrement
        query = 'INSERT INTO records (personne1, personne2, temps, somme, hash) VALUES (' + str(record["personne1"]) + ',' + str(record["personne2"]) + ',' + str(int(today)) + ',' + str(record["somme"]) + ',"' + hash + '")'
        cur.execute(query)
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_record_v4(db_path, record):
    """
    record = {
        "personne1" : "1",
        "personne2" : "2",
        "temps" : "15615213541665",
        "somme" : "144.56",
        "signature" : {signature}
    }
    """

    conn = None

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        #On récupère le hash de la plus récente transaction
        previous_hash = ""
        hash=""
        query_hash = "SELECT hash from records WHERE temps = (SELECT MAX(temps) FROM records)"
        cur.execute(query_hash)
        rows = cur.fetchall()

        if(len(rows) == 0): #On est sur la première transaction
            today = time.time()
            pre_hash = str(record["personne1"]) + "|" + str(record["personne2"]) + "|" + str(int(today)) + "|" + str(record["somme"])
            hash = hash_sha256(pre_hash)

        else: #Il y a déjà une transaction dans la base, on peut utiliser le hash précédent !
            for row in rows:
                previous_hash = row[0]
            today = time.time()
            pre_hash = str(record["personne1"]) + "|" + str(record["personne2"]) + "|" + str(int(today)) + "|" + str(record["somme"])
            hash = hash_sha256_v3(pre_hash, previous_hash) #On crée notre hash en tenant compte du hash précédent

        #On insère l'enregistrement
        query = 'INSERT INTO records (personne1, personne2, temps, somme, hash, signature) VALUES (' + str(record["personne1"]) + ',' + str(record["personne2"]) + ',' + str(record["temps"]) + ',' + str(record["somme"]) + ',"' + hash + '", "' + str(record["signature"]) + '")'
        cur.execute(query)
        conn.commit()

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
        conn.commit()

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
        debit = 0
        credit = 0
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        rows = []
        query = "SELECT SUM(SOMME) FROM records WHERE personne1=" + str(id)
        cur.execute(query)
        rows = cur.fetchall()

        if(len(rows) > 0 and type(rows[0][0]) != type(None)):
            for row in rows :
                debit = int(row[0])

        rows = []
        query = "SELECT SUM(SOMME) FROM records WHERE personne2=" + str(id)
        cur.execute(query)
        rows = cur.fetchall()
        if(len(rows) > 0 and type(rows[0][0]) != type(None)):
            for row in rows:
                credit = int(row[0])
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return (credit - debit)
