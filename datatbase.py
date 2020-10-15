import sqlite3
import pandas as pd
import csv


class Manager:
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


manager = Manager()
manager.insert_into_table()
