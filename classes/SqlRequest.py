import sqlite3
import json

class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def execute_sql(self, query):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    def save_sql(self, query, parameters):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute(query, parameters)
        conn.commit()
        conn.close()

    def create_database(self, filename):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        with open(filename) as f:
            file_data = f.read()
            c.executescript(file_data)
        conn.commit()
        conn.close()

class VenteDatabase(DatabaseManager):
    def test_sql(self, query):
        """
        Pour tester les requêtes SQL
        """       
        return self.execute_sql(query, ())    
    
