from entity.player import Player
from random import randint
from game.game import Game


class Enemy(Player):
    names = [
        "Thief",
        "Zombie",
        "Phantom",
        "Dragon",
        "Harpy",
        "Goblin",
        "Slime",
        "Rat",
        "Wisp",
        "Scout",
    ]

    def __init__(self):
        self.name = Enemy.names[(randint(0, (len(Enemy.names) - 1)))]
        self.archetype = Enemy.archetypes[randint(0, (len(Enemy.archetypes) - 1))]
        self.strength = randint(1, Game.day_count + 1)
        self.intelligence = randint(1, Game.day_count + 1)
        self.dexterity = randint(1, Game.day_count + 1)
        self.level = 1
        self.health = 1
