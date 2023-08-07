from os import system
from random import randint


class Player:
    choices = ["travel", "stats", "rest", "quit"]
    archetypes = ["warrior", "mage", "rogue"]

    def __init__(self):
        self.name = input("Welcome. What is your name?\n").capitalize()
        system("cls")
        self.archetype = input(
            "Who would you like to become?"
            + "Strong warrior, powerful mage or a stealthy rogue?\n"
        ).lower()
        system("cls")
        self.level = 1
        self.strength = 1
        self.intelligence = 1
        self.dexterity = 1
        self.health = 1

    @property
    def min_damage(self, weapon_max_damage=1):
        match self.archetype:
            case "warrior":
                return self.strength * weapon_max_damage
            case "mage":
                return self.intelligence * weapon_max_damage
            case "rogue":
                return self.dexterity * weapon_max_damage
            case _:
                return 0

    @property
    def max_damage(self, weapon_min_damage=1):
        match self.archetype:
            case "warrior":
                return self.strength * 2 * weapon_min_damage
            case "mage":
                return self.intelligence * 2 * weapon_min_damage
            case "rogue":
                return self.dexterity * 2 * weapon_min_damage
            case _:
                return 0

    @property
    def attack_damage(self) -> str:
        return f"{self.min_damage} - {self.max_damage}"

    @property
    def hit_points(self) -> int:
        return 100 + 10 * (self.level - 1) + 10 * (self.health - 1)

    def __str__(self) -> str:
        return (
            f"\nName:             {self.name}"
            + f"\nClass:            {self.archetype.capitalize()}"
            + f"\nLevel:            {self.level}"
        )

    def check_stats(self):
        print(
            self,
            f"\n\nStrength:         {self.strength}"
            + f"\nIntelligence:     {self.intelligence}"
            + f"\nDexterity:        {self.dexterity}\n"
            + f"\nAttack damage:    {self.attack_damage}"
            + f"\nHit points:       {self.hit_points}",
        )

    def add_stats(self, stat, times=1):
        match stat:
            case "strength":
                self.strength += 1 * times
            case "intelligence":
                self.intelligence += 1 * times
            case "dexterity":
                self.dexterity += 1 * times
            case "every stat":
                self.strength += 1 * times
                self.intelligence += 1 * times
                self.dexterity += 1 * times
            case _:
                pass
        print(f"You have gained {times} point(s) of {stat}!")

    def level_up(self):
        self.level += 1
        print(f"You have levelled up! You are now level {self.level}.")
        self.add_stats("every stats")

    def attack(self, target):
        print(
            f"{self.name} attacked {target.name}"
            + f" and dealt {randint(self.min_damage,self.max_damage)} damage."
        )
