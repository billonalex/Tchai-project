# Tchaï Project

## Usage

- Run ```python Flask.py``` in a shell
- Then you can access to ```http://127.0.0.1:5000/``` in your favourite browser
- You can use this address to send your API requests

## Requêtes API :

Les requêtes créées sont :

    Ajouter une personne -----------------------------------------------------> POST /personne/<nom>/<prenom> ------------------------> INSERT INTO personne (nom,prenom) VALUES ("BILLON", "Alexandre")
    Supprimer une personne ---------------------------------------------------> DELETE /personne/<id> --------------------------------> DELETE FROM personne WHERE id=1
    Consulter la liste des personnes -----------------------------------------> GET /personnes ---------------------------------------> SELECT * FROM personne (ORDER BY nom,prenom)
    Informations d'une personne via son id -----------------------------------> GET /personnes/<id> ----------------------------------> SELECT * FROM personne WHERE id=1

    Effectuer une transaction ------------------------------------------------> POST /records/<personne1>/<personne2>/<somme> --------> INSERT INTO records (personne1,personne2,temps,somme) VALUES (1,2,155615521,1565.54)
    Annuler une transaction --------------------------------------------------> DELETE /records/<id> ---------------------------------> DELETE FROM records WHERE id=1
    Consulter les transactions dans l'ordre chronologique --------------------> GET /records -----------------------------------------> SELECT * FROM records (order by temps ASC)
    Consulter les transactions dans l'ordre chronologique pour une personne --> GET /records/<personne> ------------------------------> SELECT * FROM records WHERE personne1=1 (order by temps ASC)
    Afficher le solde d'une personne -----------------------------------------> GET /solde/<personne> --------------------------------> SELECT SUM(somme) AS solde FROM records WHERE personne1=1

## Hash

SHA-256 sera utilisé pour le hashage des enregistrements.

On encode le tuple avec ces informations :

    id_personne1
    id_personne2
    temps
    somme

On crée une chaine ```"{id_personne1}|{id_personne2}|{temps}|{somme}"``` qu'on enverrai dans une méthode de hashage SHA-256.
