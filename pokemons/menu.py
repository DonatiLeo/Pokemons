import sqlite3
from random import randint
from database import ManageData
from game import Game


# pokemon dataset : https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6#file-pokemon-csv


class Menu:
    manage_data = ManageData()
    game = Game()

    def __init__(self):
        # TODO: garder ou supprimer : self.compte_existant = False
        pass

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
            id_pseudo = self.connexion()
            self.menu_after_connexion(id_pseudo)

        elif choix_utilisateur == 2:
            id_pseudo = self.create_account()
            id_pokemon = Menu.manage_data.after_connexion()
            Menu.manage_data.add_character(id_pseudo, id_pokemon)
            self.ask_account()
            return id_pseudo

        elif choix_utilisateur == 3:
            self.exit()

    def connexion(self):
        email = str(input("\nEntrez votre email : "))
        mot_de_passe = str(input("Entrez votre mot de passe : "))
        resultat = Menu.manage_data.connexion(email, mot_de_passe)
        if resultat is None:  # if resultat:  # bool(resultat)
            print("\nDésolé erreur de connection ! Reessayez\n")
            return self.connexion()  # Recursivité
        else:
            pseudo = resultat[1]
            id_pseudo = resultat[0]
            print("\nBonjour " + pseudo + "\nvous avez le numéro ", id_pseudo)
            return id_pseudo

    @staticmethod
    def create_account():
        # TODO: while True
        pseudo = str(input("\nEntrez votre pseudo : "))
        email = str(input("Entrez votre adresse mail : "))
        mot_de_passe = str(input("Entrez un mot de passe : "))  # TODO: getpass
        # TODO: Check mot de passe
        Menu.manage_data.insert_into_new_account(pseudo, email, mot_de_passe)
        resultat = Menu.manage_data.select_information(email, mot_de_passe)
        id_pseudo = resultat[0]
        return id_pseudo

    def menu_after_connexion(self, id_pseudo):
        self.ask_pokemons(id_pseudo)
        self.ask_versus(id_pseudo)
        reponse = int(input("\nVoulez vous revenir au menu principal ? si oui tapez 1 "
                            "\nSi vous voulez vous déconnecter tapez 2 "
                            "\nSi vous voulez quitter le jeu tappez 3 : "))
        if reponse == 3:
            self.exit()
        elif reponse == 2:
            self.ask_account()
        elif reponse == 1:
            self.menu_after_connexion(id_pseudo)
        return id_pseudo

    def ask_pokemons(self, id_pseudo):
        reponse = str(input("\nVoulez vous voir vos pokemons (tapez 'oui')?\nSinon tapez 'non' : "))
        if reponse == "oui":
            Menu.manage_data.character_display(id_pseudo)
        elif reponse == "n":
            self.menu_after_connexion(id_pseudo)

    def ask_versus(self, id_pseudo):
        reponse = str(input("\nVoulez-vous lancer un duel ? Si oui tapez 'oui'\nSinon tapez 'non' :  "))
        if reponse == "oui":
            pokemon_player = Menu.game.character_choice(id_pseudo)
            pokemon_bot = Menu.game.character_choice_bot()
            Menu.game.duel_vs_bot(pokemon_player, pokemon_bot, id_pseudo)
        elif reponse == "n":
            self.menu_after_connexion(id_pseudo)

    @staticmethod
    def exit():
        print("\nAurevoir à bientôt !")
