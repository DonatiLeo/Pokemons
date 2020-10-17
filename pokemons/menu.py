import sqlite3
from database import ManageData


# pokemon dataset : https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6#file-pokemon-csv


class Menu:
    manage_data = ManageData()

    def __init__(self):
        # TODO: garder ou supprimer : self.compte_existant = False
        self.conn = sqlite3.connect('../resources/sql/ma_base.db')
        self.cursor = self.conn.cursor()
        with open("../resources/sql/requetes/creationTables.sql") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()

    def ask_account(self):
        print("\nBienvenue Sur Mon Jeu Pokémon\n")
        while True:
            try:
                # TODO: renommer choix_utilisateur
                choix_utilisateur = int(
                    input("Connectez vous à votre compte en tapant 1 si vous en avez un, 2 sinon ou si vous voulez "
                          "quitter le jeu tapez 3 : "))
                break
            except ValueError:
                print("Oups !! Veuillez rentrer soit 1 soit 2 !")

        if choix_utilisateur == 1:
            self.connexion()
            self.ask_pokemons()

        elif choix_utilisateur == 2:
            id_joueur = ''
            self.create_account()
            Menu.manage_data.after_connexion()
            Menu.manage_data.add_character(id_joueur, Menu.manage_data.after_connexion())
            self.ask_account()

        elif choix_utilisateur == 3:
            self.exit()

    def connexion(self):
        email = str(input("\nEntrez votre email : "))
        mot_de_passe = str(input("Entrez votre mot de passe : "))
        self.cursor.execute("SELECT id, pseudo FROM Compte WHERE email = ? AND password = ?",
                            (email, mot_de_passe))
        resultat = self.cursor.fetchone()

        if resultat is None:  # if resultat:  # bool(resultat)
            print("\nDésolé erreur de connection ! Reessayez\n")
            return self.connexion()  # Recursivité
        else:
            pseudo = resultat[1]
            id_pseudo = resultat[0]
            print("\nBonjour " + pseudo + "\nvous avez le numéro ", id_pseudo)
            return id_pseudo

    def create_account(self):
        # TODO: while True
        pseudo = str(input("\nEntrez votre pseudo : "))
        email = str(input("Entrez votre adresse mail : "))
        mot_de_passe = str(input("Entrez un mot de passe : "))  # TODO: getpass
        # TODO: Check mot de passe
        self.cursor.execute("""
            INSERT INTO Compte(pseudo,email,password) VALUES(
            ?,?,?);
        """, (pseudo, email, mot_de_passe))
        self.conn.commit()

    def ask_pokemons(self):
        id_pseudo = self.connexion()
        oui = str(input("Voulez vous voir vos pokemons (tapez 'oui')?\n"))
        if oui == 'oui':
            Menu.manage_data.character_display(id_pseudo)
        else:
            self.ask_account()

    def exit(self):
        print("Aurevoir à bientôt !")
        self.conn.close()
