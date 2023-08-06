from random import randint
from os import system


class Game:
    day_count = 1
    confirm = 1
    locations = [
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
    ]

    def confirm_archetype(player):
        while Game.confirm == 1:
            match player.archetype:
                case "warrior":
                    player.strength += 2
                    Game.confirm = 0
                case "mage":
                    player.intelligence += 2
                    Game.confirm = 0
                case "rogue":
                    player.dexterity += 2
                    Game.confirm = 0
                case _:
                    player.archetype = input(
                        "\nAre you sure that is a real thing?."
                        + " Let me ask you again.\n... a warrior, mage or a rogue?\n"
                    )
        else:
            print(
                f"\nAh.. so {player.archetype} {player.name}!"
                + "\nYour adventure begins now.\n"
            )

    def main_loop(player):
        Game.confirm_archetype(player)
        while player.hit_points > 0:
            player.choice = input(
                f"\nDay: {Game.day_count}\nWhat would you like to do? "
                + "Travel, check stats or take a rest?\n"
            )
            if player.choice == player.choices[0]:
                location_current = Game.locations[randint(0, len(Game.locations))]
                print(f"\nYou are now in {location_current}\n")
                if location_current == Game.locations[2]:
                    print(
                        "You can feel the magic surrounding you. "
                        + "After searching the ruins you discover an old book, "
                        + "which contains valuable knowledge.\n"
                    )
                    player.add_stats("intelligence")
                else:
                    print(
                        "You are trying to go past it without being noticed...\n"
                        + "...and it worked! You have improved your dexterity"
                    )
                    player.add_stats("dexterity")
                Game.day_count += 1
            elif player.choice == player.choices[1]:
                player.check_stats()
            elif player.choice == player.choices[2]:
                print(
                    "\nYou found a place to safely camp and took a moment of respite. "
                    + "You are well rested!"
                )
                Game.day_count += 1
            elif player.choice == player.choices[3]:
                system("cls")
                break
            else:
                print("\nYou cannot do that.")
        else:
            print("You died...")
