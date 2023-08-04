from random import randint
from os import system


class Player:
    choices = ["travel", "stats", "rest", "quit"]

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
    def min_damage(self):
        match self.archetype:
            case "warrior":
                return self.strength
            case "mage":
                return self.intelligence
            case "rogue":
                return self.dexterity
            case _:
                return 0

    @property
    def max_damage(self):
        match self.archetype:
            case "warrior":
                return self.strength * 2
            case "mage":
                return self.intelligence * 2
            case "rogue":
                return self.dexterity * 2
            case _:
                return 0

    @property
    def attack_damage(self):
        return f"{self.min_damage} - {self.max_damage}"

    @property
    def hit_points(self):
        return 100 + 10 * (self.level - 1) + 10 * (self.health - 1)

    def __str__(self) -> str:
        return (
            f"\nName:             {self.name}"
            + f"\nClass:            {self.archetype.capitalize()}"
            + f"\nLevel:            {self.level}"
        )

    def checkstats(self):
        print(self)
        print(
            f"\nStrength:         {self.strength}"
            + f"\nIntelligence:     {self.intelligence}"
            + f"\nDexterity:        {self.dexterity}"
            + f"\n\nAttack damage:    {self.attack_damage}"
            + f"\nHit points:       {self.hit_points}"
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

    def levelup(self):
        self.level += 1
        print(f"You have levelled up! You are now level {self.level}.")
        self.addstats("every stats")

    def attack(self, target):
        print(
            f"{self.name} attacked {target.name}"
            + f" and dealt {randint(self.min_damage,self.max_damage)}"
        )
        # todo


class Enemy(Player):
    def __init__(self, name, archetype):
        self.name = name
        self.archetype = archetype
        self.strength = randint(1, daycount + 1)
        self.intelligence = randint(1, daycount + 1)
        self.dexterity = randint(1, daycount + 1)


player = Player()
location = [
    "Dark woods",
    "Wetlands",
    "Magic ruins",
    "Bandit camp",
    "Peaceful lands",
    "Peaceful lands",
    "Peaceful lands",
    "Peaceful lands",
    "Peaceful lands",
    "Peaceful lands",
    "Peaceful lands",
]
daycount = 1

enemy = Enemy("Bandit", "warrior")
# enemy.checkstats()

while True:
    match player.archetype:
        case "warrior":
            player.strength += 2
            break
        case "mage":
            player.intelligence += 2
            break
        case "rogue":
            player.dexterity += 2
            break
        case _:
            player.archetype = input(
                "\nAre you sure that is a real thing?. Let me ask you again.\n... a warrior, mage or a rogue?\n"
            )
print(f"\nAh.. so {player.archetype} {player.name}!\nYour adventure begins now.\n")

# print(player)
# player.checkstats()
# player.addstats("strength")
# player.checkstats()
# player.addstats("intelligence", 2)
# player.checkstats()
player.attack(enemy)

while True:
    player.choice = input(
        f"\nDay: {daycount}\nWhat would you like to do? Travel, check stats or take a rest?\n"
    )
    if player.choice == player.choices[0]:
        location_current = location[randint(0, len(location))]
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
