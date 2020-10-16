import sqlite3
import pandas as pd
import csv


class ManageData:
    opencsv = open("BasesDonnees/pokemons/pokemon.csv", "r")
    table = list(csv.reader(opencsv, delimiter=';'))

    def __init__(self):
        self.conn = sqlite3.connect('BasesDonnees/ma_base.db')
        self.cursor = self.conn.cursor()
        with open("BasesDonnees/requetes/creationTables.sql") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()

    def insert_into_table(self):
        """

        :return:
        """
        #  chargement des données dans les dataframe de Pandas
        package = pd.read_csv("BasesDonnees/pokemons/pokemon.csv")
        #  ecriture des données dans la table sqlite
        package.to_sql('Pokemons', self.conn, if_exists='append', index=False)

    def add_character(self, pseudo):
        self.cursor.execute("""INSERT INTO 
        
        """)

    def character_display(self, pseudo):
        self.cursor.execute("""SELECT name
        FROM Pokemons
        INNER JOIN Compte
        """)
        self.cursor.fetchall()


manager = ManageData()
manager.insert_into_table()
