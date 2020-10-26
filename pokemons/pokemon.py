from random import randint


class Pokemon:

    def __init__(self, pokemon_joueur, pokemon_autre_joueur, health, attack):
        self.pokemon_joueur = pokemon_joueur
        self.pokemon_autre_joueur = pokemon_autre_joueur
        self.health = health
        self.attack = attack

    def fight_attack(self):
        attack_random = randint(1, self.attack)
        print("\n", self.pokemon_joueur, "attaque ! et inflige", attack_random, "dégats")
        self.remove_health(attack_random)
        return attack_random

    def remove_health(self, attack):
        self.health -= attack
        self.health = max(self.health, 0)
        print("il reste", self.health, "points de vie a", self.pokemon_autre_joueur)
        self.is_dead()

    def is_dead(self):
        if self.health == 0:
            return True
        return False
