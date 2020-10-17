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
        package.to_sql('Pokemons', self.conn, if_exists='replace', index=False)
        # ajout de l'id primaire
        with open(ManageData.SQL_PATH + "requetes/add_primary_key_to_pokemon.sql") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()

    def opening_csv(self):
        # Soit je remplace par pandas, soit je garde csv en mettant a jour la méthode insert_into_table.
        csv_file = open(ManageData.CSV_PATH + "pokemon.csv", "r")
        table = list(csv.reader(csv_file, delimiter=';'))
        for element in table:
            y = element[0].split(",")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Pokemons(
        ? INTEGER NOT NULL UNIQUE,
        ? TEXT NOT NULL,
        ? TEXT NOT NULL,
        ? TEXT,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        ? INTEGER NOT NULL,
        PRIMARY KEY(?));
        """, (y[0][0], y[0][1], y[0][2], y[0][3], y[0][4], y[0][5], y[0][6], y[0][7], y[0][8], y[0][9], y[0][10], y[0][11], y[0][0]))

        for i in range(len(y)):  # TODO : faire une liste pour remplir la table.
            pass

        csv_file.close()
        return table

    def add_character(self, compte_id, id_pokemon):
        information = compte_id, id_pokemon
        self.cursor.execute("""INSERT INTO Pokemons_possessed(compte_id,id_pokemon,pokemons_possessed_total) VALUES
        (?,?,1)""", information)

    def after_connexion(self):
        self.cursor.execute("""
        SELECT id_pokemon FROM Pokemons
        ORDER BY random() 
        LIMIT 1
        """)
        pokemon = self.cursor.fetchone()
        return pokemon[0]

    def character_display(self, id_pseudo):
        self.cursor.execute("""SELECT name, health_point, attack, defense, special_attack, special_defense, speed
        FROM Compte
        INNER JOIN Pokemons_possessed
        ON Pokemons_possessed.compte_id = Compte.id
        INNER JOIN Pokemons
        ON Pokemons.id_pokemon = Pokemons_possessed.id_pokemon
        WHERE compte_id = ?""", id_pseudo)
        self.cursor.fetchall()
