from os import system
from random import randint, choice
from game.items import Items


class Player:
    choices = ["travel", "stats", "inventory", "rest", "equip", "equipment", "quit"]
    archetypes = ["warrior", "mage", "rogue"]

    def __init__(self):
        self.name = input("Welcome. What is your name?\n").capitalize()
        system("cls")
        self.archetype = input(
            "Who would you like to become?"
            + " Strong warrior, powerful mage or a stealthy rogue?\n"
        ).lower()
        system("cls")
        self.level = 1
        self.strength = 1
        self.intelligence = 1
        self.dexterity = 1
        self.health = 1
        self.inventory = []
        self.equipment = []

    @property
    def min_damage(self):
        match self.archetype:
            case "warrior":
                if self.equipment:
                    return self.strength * choice(self.equipment).weapon_min_damage
                else:
                    return self.strength
            case "mage":
                if self.equipment:
                    return self.intelligence * choice(self.equipment).weapon_min_damage
                else:
                    return self.intelligence
            case "rogue":
                if self.equipment:
                    return self.dexterity * choice(self.equipment).weapon_min_damage
                else:
                    return self.dexterity
            case _:
                return 0

    @property
    def max_damage(self, weapon_min_damage=1):
        match self.archetype:
            case "warrior":
                if self.equipment:
                    return self.strength * 2 * choice(self.equipment).weapon_max_damage
                else:
                    return self.strength
            case "mage":
                if self.equipment:
                    return (
                        self.intelligence * 2 * choice(self.equipment).weapon_max_damage
                    )
                else:
                    return self.intelligence
            case "rogue":
                if self.equipment:
                    return self.dexterity * 2 * choice(self.equipment).weapon_max_damage
                else:
                    return self.dexterity
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

    def equip_item(self):
        item = input("Which item do you want to equip?\n")
        for a in self.inventory:
            if a.name == item:
                if self.equipment:
                    self.equipment.clear()
                self.equipment.append(a)
                self.inventory.remove(a)
                print(f"You have equipped {a.name}.")

    def check_equipment(self):
        if self.equipment:
            print(self.equipment)
        else:
            print("You dont have anything equipped.")

    def check_inventory(self):
        if self.inventory:
            print(self.inventory)
        else:
            print("Your inventory is empty.")

    def level_up(self):
        self.level += 1
        print(f"You have levelled up! You are now level {self.level}.")
        self.add_stats("every stats")

    def attack(self, target):
        print(
            f"{self.name} attacked {target.name}"
            + f" and dealt {randint(self.min_damage,self.max_damage)} damage."
        )
