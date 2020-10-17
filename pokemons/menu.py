import sqlite3
from database import ManageData

# pokemon dataset : https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6#file-pokemon-csv


class Menu:

    manageData = ManageData()

    def __init__(self):
        # TODO: garder ou supprimer : self.compte_existant = False
        self.conn = sqlite3.connect('BasesDonnees/ma_base.db')
        self.cursor = self.conn.cursor()
        with open("BasesDonnees/requetes/creationTables.sql") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()

    def ask_account(self):
        print("Bienvenue Sur Mon Jeu MMORPG\n")
        choix_utilisateur = 0
        print(choix_utilisateur < 1 or choix_utilisateur > 2)
        while True:
            try:
                # TODO: renommer choix_utilisateur
                choix_utilisateur = int(
                    input("Connectez vous à votre compte en tapant 1 si vous en avez un, 2 sinon : "))
                break
            except ValueError:
                print("Oups !! Veuillez rentrer soit 1 soit 2 !")
        if choix_utilisateur == 1:
            Menu.manageData.after_connexion()
            self.user_choise()

        if choix_utilisateur == 2:
            self.create_account()
            self.ask_account()

    def user_choise(self):
        self.connexion()
        self.ask_pokemons()

    def connexion(self):
        email = str(input("\nEntrez votre email : "))
        mot_de_passe = str(input("Entrez votre mot de passe : "))
        self.cursor.execute("SELECT pseudo FROM Compte WHERE email = ? AND password = ?",
                            (email, mot_de_passe))
        resultat = self.cursor.fetchone()

        if resultat is None:  # if resultat:  # bool(resultat)
            print("\nDésolé erreur de connection ! Reessayez\n")
            return self.connexion()  # Recursivité
        else:
            pseudo = resultat[0]
            print("\nBonjour " + pseudo)
            return pseudo

    def create_account(self):
        # TODO: while True
        pseudo = str(input("Entrez votre pseudo : "))
        email = str(input("Entrez votre adresse mail : "))
        mot_de_passe = str(input("Entrez un mot de passe : "))  # TODO: getpass
        # TODO: Check mot de passe
        self.cursor.execute("""
            INSERT INTO Compte(pseudo,email,password) VALUES(
            ?,?,?);
        """, (pseudo, email, mot_de_passe))
        self.conn.commit()

    def ask_pokemons(self):
        pseudo = self.connexion()
        oui = str(input("Voulez vous voir vos pokemons (tapez 'oui')?\n"))
        if oui == 'oui':
            Menu.manageData.character_display(pseudo)
        else:
            self.user_choise()

    def exit(self):
        self.conn.close()


menu = Menu()
menu.ask_account()
