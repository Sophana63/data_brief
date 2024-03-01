import pandas as pd
import os
from tqdm import tqdm
from classes.SqlRequest import DatabaseManager

df_ventes = pd.read_csv("data2/ventes.csv")
df_produits = pd.read_csv("data2/produits.csv")
df_magasins = pd.read_csv("data2/magasins.csv")

db = './data2/ventes2.db'
filename = './data2/create_bdd.txt'

# Je vérifie si la base de données Sqlite exite
if os.path.exists(db):
    # Si oui, je la supprime
    os.remove(db)

# Création de la BDD et des tables
sqlrequest = DatabaseManager(db)
sqlrequest.create_database(filename)

print("")
print("----------------------------------------")
print("La base de données a été créée")
print("----------------------------------------")
print("")
print("Liste des 5 premières ventes")
print(df_ventes.head())
print("----------------------------------------")
print("")
print("Liste des 5 premièrs magasins")
print(df_magasins.head())
print("----------------------------------------")
print("")
print("Liste des 5 premièrs produits")
print(df_produits.head())
print("----------------------------------------")
print("")


# Insertion des données dans la table Ventes
successful_inserts = 0
total_rows = len(df_ventes)

for index, row in tqdm(df_ventes.iterrows(), total=total_rows, desc="Insertion des ventes"):
    query = "INSERT INTO Ventes (Date, ID_Reference_produit, Quantite, ID_Magasin) VALUES (?, ?, ?, ?)"
    parameters = (row['Date'], row['ID Référence produit'], row['Quantité'], row['ID Magasin'])    
    try:
        sqlrequest.save_sql(query, parameters)
        successful_inserts += 1
    except Exception as e:
        print("Erreur lors de l'insertion pour la ligne", index, ":", e)

if successful_inserts == total_rows:
    print("Toutes les lignes de la table Ventes ont été ajoutées avec succès.")
    print(" ")

# Insertion des données dans la table Produis
successful_inserts = 0
total_rows = len(df_produits)

for index, row in tqdm(df_produits.iterrows(), total=total_rows, desc="Insertion des produits"):
    query = "INSERT INTO Produits (Nom, ID_Reference_produit, Prix, Stock) VALUES (?, ?, ?, ?)"
    parameters = (row['Nom'], row['ID Référence produit'], row['Prix'], row['Stock'])    
    try:
        sqlrequest.save_sql(query, parameters)
        successful_inserts += 1
    except Exception as e:
        print("Erreur lors de l'insertion pour la ligne", index, ":", e)

if successful_inserts == total_rows:
    print("Toutes les lignes de la table Produits ont été ajoutées avec succès.")
    print(" ")

# Insertion des données dans la table Magasins
successful_inserts = 0
total_rows = len(df_magasins)

for index, row in tqdm(df_magasins.iterrows(), total=total_rows, desc="Insertion des magasins"):
    query = "INSERT INTO Magasins (ID_magasin, Ville, Nombre_de_salarie) VALUES (?, ?, ?)"
    parameters = (row['ID Magasin'], row['Ville'], row['Nombre de salariés'])    
    try:
        sqlrequest.save_sql(query, parameters)
        successful_inserts += 1
    except Exception as e:
        print("Erreur lors de l'insertion pour la ligne", index, ":", e)

if successful_inserts == total_rows:
    print("Toutes les lignes de la table Produits ont été ajoutées avec succès.")
    print(" ")


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
LEFT JOIN Magasins m ON m.ID_Magasin = v.ID_Magasin
LEFT JOIN Produits p ON p.ID_Reference_produit = v.ID_Reference_produit
WHERE m.Ville = 'Paris'
"""
print("----------------------------------------")
print("Requête pour obtenir toutes les ventes dans les magasins situés à Paris")
print(sqlrequest.execute_sql(request3))
print("----------------------------------------")