from database import ManageData
from random import randint
from pokemon import Pokemon


class Game:
    SQL_PATH = '../resources/sql/'
    manage_data = ManageData()

    def __init__(self):
        self.joueur_actuel = randint(1, 2)
        self.health_player = 0
        self.health_bot = 0

    @staticmethod
    def character_choice(id_pseudo):
        pokemon_choisi = str(input("Choisissez le pokemon avec lequel vous voulez vous battre : "))
        resultat = Game.manage_data.character_choice(pokemon_choisi, id_pseudo)
        return resultat

    @staticmethod
    def character_choice_bot():
        pokemon_bot = Game.manage_data.character_choice_bot()
        return pokemon_bot

    @staticmethod
    def display(pokemon_player, pokemon_bot):
        print("\nVous vous battez !!")
        print("\nPokémon du bot : " + pokemon_bot[1] + ", Vie :", pokemon_bot[2], ", Attaque :", pokemon_bot[3])
        print("Votre pokémon : " + pokemon_player[1] + ",  Vie :", pokemon_player[2], ",  Attaque :", pokemon_player[3])

    def player(self, pokemon_player, pokemon_bot):
        pokemon = Pokemon(pokemon_player[1], pokemon_bot[1], pokemon_bot[2] - self.health_bot, pokemon_player[3])
        self.health_bot = pokemon.fight_attack()
        return pokemon

    def bot(self, pokemon_player, pokemon_bot):
        pokemon = Pokemon(pokemon_bot[1], pokemon_player[1], pokemon_player[2] - self.health_player, pokemon_bot[3])
        self.health_player = pokemon.fight_attack()
        return pokemon

    def duel_vs_bot(self, pokemon_player, pokemon_bot, id_pseudo):
        Game.display(pokemon_player, pokemon_bot)
        pokemon = Pokemon(None, None, None, None)
        while not pokemon.is_dead():
            if self.joueur_actuel % 2 == 0:
                pokemon_player = self.player(pokemon_player, pokemon_bot)
                if pokemon_player.is_dead():
                    print("\nVous avez gagné !")
                    print(pokemon_bot[1], "est mort !")
                    Game.random_luck(id_pseudo, pokemon_bot)
                    return
                self.joueur_actuel += 1
            else:
                pokemon_bot = self.bot(pokemon_player, pokemon_bot)
                if pokemon_bot.is_dead():
                    print("\nVous avez perdu !")
                    print(pokemon_player[1], "est mort !")
                    return
                self.joueur_actuel += 1

    @staticmethod
    def random_luck(id_pseudo, pokemon_bot):
        luck = randint(1, 20)
        if luck <= 3:
            Game.manage_data.add_character(id_pseudo, pokemon_bot[0])
            print("Vous avez capturé : " + pokemon_bot[1])
        else:
            print("Vous n'avez capturé aucun pokémon !")
