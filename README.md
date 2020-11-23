# Tchaï Project

## Usage

- Run ```python Tchai.py``` in a shell
- Then you can access to ```http://127.0.0.1:5000/``` in your favourite browser
- You can use this address to send your API requests

## Requêtes API :

Les requêtes créées sont :

### Ajouter une personne

    POST /personne/<nom>/<prenom>
    INSERT INTO personne (nom,prenom) VALUES ("BILLON", "Alexandre")

### Supprimer une personne

    DELETE /personne/<id>
    DELETE FROM personne WHERE id=1

### Consulter la liste des personnes

    GET /personnes
    SELECT * FROM personne (ORDER BY nom,prenom)

### Informations d'une personne via son id

    GET /personnes/<id>
    SELECT * FROM personne WHERE id=1

### Effectuer une transaction

    POST /records/<personne1>/<personne2>/<somme>
    INSERT INTO records (personne1,personne2,temps,somme) VALUES (1,2,155615521,1565.54)

### Annuler une transaction

    DELETE /records/<id>
    DELETE FROM records WHERE id=1

### Consulter les transactions dans l'ordre chronologique

    GET /records
    SELECT * FROM records (order by temps ASC)

### Consulter les transactions dans l'ordre chronologique pour une personne

    GET /records/<personne>
    SELECT * FROM records WHERE personne1=1 (order by temps ASC)

### Afficher le solde d'une personne

    GET /solde/<personne>
    SELECT SUM(somme) AS solde FROM records WHERE personne1=1

### Vérifier l'intégrité des enregistrements

    GET /check/data/
    SELECT * FROM records (order by temps ASC)

### Vérifier l'intégrité d'un enregistrement

    GET /check/data/<id>
    SELECT * FROM records WHERE id=1 (order by temps ASC)

### Effectuer une transaction en tenant compte du hash de la plus récente transaction

    POST /records/v3/<personne1>/<personne2>/<somme>
    SELECT id from records WHERE temps = (SELECT MAX(temps) FROM records)

D'autres requêtes pourront être imaginées par la suite.

## Database

La base de données est actuellement composée de 2 tables : ```personne``` et ```record```

### Table personne :

```sql
CREATE TABLE "personne" (
	"id"        INTEGER NOT NULL UNIQUE,
	"nom"       TEXT NOT NULL,
	"prenom"    TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
```
- Par la suite, nous pouvons, si nous le souhaitons, ajouter des données supplémentaires à la table personne.

### Table records :

```sql
CREATE TABLE "records" (
	"id"        INTEGER NOT NULL UNIQUE,
	"personne1" INTEGER NOT NULL,
	"personne2" INTEGER NOT NULL,
	"temps"     INTEGER NOT NULL,
	"somme"     NUMERIC NOT NULL,
	"hash"      TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("personne1") REFERENCES "personne"("id"),
	FOREIGN KEY("personne2") REFERENCES "personne"("id")
)
```

Le temps est pour l'instant stocké comme étant le nombre de secondes écoulées depuis le 1er janvier 1970. Ce formalisme a plusieurs avantages :
- Il facilite la comparaison de date, puisque ca reviens a faire une differente entre 2 nombres
- Il est géré par la plupars des langage et SGBD
- Il est universel, la notion de fuseaux horaires disparait.

Cependant il est peu compréhensible par l'homme. C'est pourquoi il sera reconverti en date classique lors de l'affichage.

## Tests et attaques

Les tests et attaques sont développés dans le script ```tests/attack.py```



## Hash

SHA-256 sera utilisé pour le hashage des enregistrements.

On encode le tuple avec ces informations :

    id_personne1
    id_personne2
    temps
    somme

On crée une chaine ```"{id_personne1}|{id_personne2}|{temps}|{somme}"``` qu'on enverra dans une méthode de hashage SHA-256.

## Auteurs

    Alexandre BILLON
    Noémie Chevalier