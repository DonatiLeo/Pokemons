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
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pokemons(
        id_pokemon INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        type1 TEXT NOT NULL,
        type2 TEXT,
        health_point INTEGER NOT NULL,
        attack INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        special_attack INTEGER NOT NULL,
        special_defense INTEGER NOT NULL,
        speed INTEGER NOT NULL,
        generation INTEGER NOT NULL,
        legendary INTEGER NOT NULL,
        PRIMARY KEY(id_pokemon)
        );
        """, )

        for element in table[1:]:
            y = element[0].split(",")
            self.cursor.execute("""INSERT OR REPLACE INTO Pokemons VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?);     
            """, (y[0], y[1], y[2], y[3], int(y[4]), int(y[5]), int(y[6]), int(y[7]), int(y[8]), int(y[9]),
                  int(y[10]), y[11]))
        self.conn.commit()
        csv_file.close()
        return table

    def add_character(self, compte_id, id_pokemon):
        information = compte_id, id_pokemon
        self.cursor.execute("""INSERT INTO Pokemons_possessed(compte_id,id_pokemon) VALUES
        (?,?);""", information)
        self.conn.commit()

    def connexion(self, email, mot_de_passe):
        self.cursor.execute("SELECT id, pseudo FROM Compte WHERE email = ? AND password = ?;",
                            (email, mot_de_passe))
        resultat = self.cursor.fetchone()
        self.conn.commit()
        return resultat

    def insert_into_new_account(self, pseudo, email, mot_de_passe):
        # TODO : Si existe deja alors redemande.
        self.cursor.execute("""
                    INSERT INTO Compte(pseudo,email,password) VALUES(
                    ?,?,?);
                """, (pseudo, email, mot_de_passe))
        self.conn.commit()

    def select_information(self, email, mot_de_passe):
        self.cursor.execute("SELECT id, pseudo FROM Compte WHERE email = ? AND password = ?;",
                            (email, mot_de_passe))
        resultat = self.cursor.fetchone()
        self.conn.commit()
        return resultat

    def after_connexion(self):
        self.cursor.execute("""
        SELECT id_pokemon FROM Pokemons
        ORDER BY random() 
        LIMIT 1;
        """)
        resultat = self.cursor.fetchone()
        return resultat[0]

    def character_display(self, id_pseudo):
        self.cursor.execute("""SELECT name, health_point, attack, defense, special_attack, special_defense, speed
                        FROM Compte
                        INNER JOIN Pokemons_possessed
                        ON Pokemons_possessed.compte_id = Compte.id
                        INNER JOIN Pokemons
                        ON Pokemons.id_pokemon = Pokemons_possessed.id_pokemon
                        WHERE compte_id = ?""", str(id_pseudo))
        print(self.cursor.fetchall())

    def character_choice(self, pokemon_choisi, id_pseudo):
        self.cursor.execute("""
                        SELECT Pokemons.id_pokemon, name, health_point, attack 
                        FROM Pokemons
                        INNER JOIN Pokemons_possessed
                        ON Pokemons_possessed.id_pokemon = Pokemons.id_pokemon
                        WHERE compte_id = ? AND name = ?;
                        """, (id_pseudo, pokemon_choisi))
        return self.cursor.fetchone()

    def character_choice_bot(self):
        self.cursor.execute("""SELECT id_pokemon, name, health_point, attack 
                        FROM Pokemons
                        ORDER BY random() 
                        LIMIT 1;
                        """)
        return self.cursor.fetchone()
