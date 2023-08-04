from random import randint
from os import system


class Player:
    choices = ["travel", "stats", "rest", "quit"]
    choice = 0

    def __init__(self):
        self.name = input("Welcome. What is your name?\n").capitalize()
        system("cls")
        self.archetype = input(
            "Who would you like to become? Strong warrior, powerful mage or a stealthy rogue?\n"
        ).lower()
        system("cls")
        self.strength = 1
        self.intelligence = 1
        self.dexterity = 1

    @property
    def attack_damage(self):
        if self.archetype == "warrior":
            return self.strength * 2
        elif self.archetype == "mage":
            return self.intelligence * 2
        elif self.archetype == "rogue":
            return self.dexterity * 2

    def __str__(self) -> str:
        return f"Name: {self.name}  Class: {self.archetype.capitalize()}"

    def checkstats(self):
        print(
            f"\nStrength: {self.strength}\nIntelligence: {self.intelligence}\nDexterity: {self.dexterity}\nAttack: {self.attack_damage}"
        )

    def addstats(self, stat, times=1):
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

    def attack(self, target):
        print(f"{target.name} watch out! You have been attacked by {self.name}!")


class Enemy(Player):
    def __init__(self, name, archetype):
        self.name = name
        self.archetype = archetype
        self.strength = randint(1, daycount + 1)
        self.intelligence = randint(1, daycount + 1)
        self.dexterity = randint(1, daycount + 1)


player = Player()
# print(player)
player.checkstats()
player.addstats("strength")
player.checkstats()
player.addstats("intelligence", 2)
player.checkstats()

location = ["Dark woods", "Wetlands", "Magic ruins", "Bandit camp"]
daycount = 1

enemy = Enemy("Bandit", "warrior")
enemy.attack(player)
# enemy.checkstats()

while True:
    match player.archetype:
        case "warrior":
            player.strength += 3
            break
        case "mage":
            player.intelligence += 3
            break
        case "rogue":
            player.dexterity += 3
            break
        case _:
            player.archetype = input(
                "\nAre you sure that is a real thing?. Let me ask you again.\n... a warrior, mage or a rogue?\n"
            )
print(f"\nAh.. so {player.archetype} {player.name}!\nYour adventure begins now.\n")

while True:
    player.choice = input(
        f"\nDay: {daycount}\nWhat would you like to do? Travel, check stats or take a rest?\n"
    )
    if player.choice == player.choices[0]:
        location_current = location[randint(0, 3)]
        print(f"\nYou are now in {location_current}\n")
        if location_current == location[2]:
            print(
                "You can feel the magic surrounding you. After searching the ruins you discover an old book, which contains valuable knowledge.\n"
            )
            player.addstats("intelligence")
        else:
            print(
                "You are trying to go past it without being noticed...\n...and it worked! You have improved your dexterity"
            )
            player.addstats("dexterity")
        daycount += 1
    elif player.choice == player.choices[1]:
        player.checkstats()
    elif player.choice == player.choices[2]:
        print(
            "\nYou found a place to safely camp and took a moment of respite. You are well rested!"
        )
        daycount += 1
    elif player.choice == player.choices[3]:
        system("cls")
        break
    else:
        print("\nYou cannot do that.")
