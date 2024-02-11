from classes.SqlRequest import *
import os

db = 'data/ventes.db'
filename = 'data/create_bdd.txt'


# Je vérifie si la base de données Sqlite exite
if os.path.exists(db):
    # Si oui, je la supprime
    os.remove(db)

# Création de la BDD, des tables et insertion des données
sqlrequest = DatabaseManager(db)
sqlrequest.create_database(filename)

print("----------------------------------------")
print("La base de données a été créée")
print("----------------------------------------")
print("")

# Test du bon fonctionnement des requêtes.
request1 = """
SELECT 
    ID_Reference_produit,
    SUM(Quantite) AS Quantite_totale
FROM Ventes
GROUP BY ID_Reference_produit
ORDER BY Quantite_totale DESC;
"""
print("----------------------------------------")
print("Requête pour obtenir la quantité totale de ventes par produit")
print(sqlrequest.execute_sql(request1))
print("----------------------------------------")
print("")

request2 = """
SELECT *
FROM Produits
ORDER BY Nom ASC 
"""
print("----------------------------------------")
print("Requête pour obtenir la liste de tous les produits")
print(sqlrequest.execute_sql(request2))
print("----------------------------------------")
print("")

request3 = """
SELECT v.ID_Reference_produit, p.Nom, v.Quantite, v.Date, m.Ville
FROM Ventes v
RIGHT JOIN Magasins m ON m.ID_Magasin = v.ID_Magasin
RIGHT JOIN Produits p ON p.ID_Reference_produit = v.ID_Reference_produit
WHERE m.Ville = 'Paris'
"""
print("----------------------------------------")
print("Requête pour obtenir toutes les ventes dans les magasins situés à Paris")
print(sqlrequest.execute_sql(request3))
print("----------------------------------------")