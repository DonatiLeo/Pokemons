import sqlite3


class Game:

    def __init__(self):
        self.conn = sqlite3.connect('BasesDonnees/ma_base.db')
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def character_choice(self):
        pokemon_choisi = str(input(""))
        self.cursor.execute("""
                SELECT
                """)
        resultat = self.cursor.fetchone()

    def duel(self):
        pass
