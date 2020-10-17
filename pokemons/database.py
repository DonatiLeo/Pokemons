import sqlite3
import pandas as pd
import csv


class ManageData:

    SQL_PATH = '../resources/sql/'
    CSV_PATH = '../resources/csv/'

    def __init__(self):
        self.conn = sqlite3.connect(ManageData.SQL_PATH + 'ma_base.db')
        self.cursor = self.conn.cursor()
        with open(ManageData.SQL_PATH + "requetes/creationTables.sql") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()

    def insert_into_table(self):
        #  chargement des données dans les dataframe de Pandas
        package = pd.read_csv(ManageData.CSV_PATH + "pokemon.csv")
        #  ecriture des données dans la table sqlite
        package.to_sql('Pokemons', self.conn, if_exists='append', index=False)

    @staticmethod
    def opening_csv():
        # Soit je remplace par pandas, soit je garde csv en mettant a jour la méthode insert_into_table.
        csv_file = open("BasesDonnees/pokemons/pokemon.csv", "r")
        table = list(csv.reader(csv_file, delimiter=';'))
        csv_file.close()
        return table

    def add_character(self, pseudo, pokemon):
        self.cursor.execute("""INSERT INTO Pokemons_possessed(id,compte_id,id_pokemon,pokemons_possessed_total) VALUES
        (?,)        
        """)

    def after_connexion(self):
        self.cursor.execute("""
        SELECT RAND(id_pokemon)
        FROM Pokemons
        """)
        pokemon = self.cursor.fetchone()
        return pokemon

    def character_display(self, pseudo):
        self.cursor.execute("""
        """)
        self.cursor.fetchall()


manager = ManageData()
manager.insert_into_table()
