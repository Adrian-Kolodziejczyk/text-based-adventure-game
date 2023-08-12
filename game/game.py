from random import randint, choices, choice, random
from os import system
from game.items import Items
from game.events import Events
from game.print_slow import print_slow


class Game:
    running = 1
    day_count = 1
    confirm = 1
    locations = [
        "Dark woods",
        "Wetlands",
        "Magic ruins",
        "Bandit camp",
        "Peaceful lands",
    ]
    location_weights = [40, 40, 5, 5, 10]

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
                    print_slow(
                        "\nAre you sure that is a real thing?."
                        + " Let me ask you again.\n... a warrior, mage or a rogue?\n"
                    )
                    player.archetype = input
        else:
            print_slow(f"\nAh.. so {player.archetype} {player.name}!")
            print_slow("\nYour adventure begins now.\n")

    def magic_ruins(player):
        print(
            "You can feel the magic surrounding you. "
            + "After searching the ruins you discover an old book, "
            + "which contains valuable knowledge.\n"
        )
        player.add_stats("intelligence")

    def rest():
        print(
            "\nYou found a place to safely camp and took a moment of respite. "
            + "You are well rested!"
        )
        Game.day_count += 1

    def travel(player):
        location_current = choices(Game.locations, Game.location_weights)
        location_current = location_current[0]
        print(f"\nYou are now in {location_current}\n")
        match location_current:
            case "Magic ruins":
                Game.magic_ruins(player)
            case "Peaceful lands":
                Items.generate_item(player, "random")
            case "Bandit camp":
                print(
                    "You are trying to go past it without being noticed...\n"
                    + "...and it worked! You have improved your dexterity"
                )
                player.add_stats("dexterity")
            case _:
                print("Nothing happens.")
        Game.day_count += 1

    def quit():
        system("cls")
        Game.running = 0

    """
    def main_loop2(player):
        Game.confirm_archetype(player)
        while Game.running == 1:
            while player.hit_points > 0:
                player.choice = str(
                    input(
                        f"\nDay: {Game.day_count}\nWhat would you like to do? "
                        + "Travel, check stats, check inventory,"
                        + " check equipment, equip an item or take a rest?\n"
                    )
                ).lower()
                for event in Events.events:
                    if player.choice == event:
                        Events.get(event, player, Game)
                    else:
                        pass
    """

    def main_loop(player):
        Game.confirm_archetype(player)
        while player.hit_points > 0:
            player.choice = str(
                input(
                    f"\nDay: {Game.day_count}\nWhat would you like to do? "
                    + "Travel, check stats, check inventory,"
                    + " check equipment, equip an item or take a rest?\n"
                )
            ).lower()
            match player.choice:
                case "travel":
                    location_current = choices(Game.locations, Game.location_weights)
                    location_current = location_current[0]
                    print(f"\nYou are now in {location_current}\n")
                    match location_current:
                        case "Magic ruins":
                            Game.magic_ruins(player)
                        case "Peaceful lands":
                            Items.generate_item(player, "random")
                        case "Bandit camp":
                            print(
                                "You are trying to go past it without being noticed...\n"
                                + "...and it worked! You have improved your dexterity"
                            )
                            player.add_stats("dexterity")
                        case _:
                            print("Nothing happens.")
                    Game.day_count += 1
                case "stats":
                    player.check_stats()
                case "inventory" | "inv":
                    player.check_inventory()
                case "rest":
                    Game.rest()
                case "equip":
                    player.equip_item()
                case "equipment" | "eq":
                    player.check_equipment()
                case "quit":
                    system("cls")
                    break
                case _:
                    print("\nYou cannot do that.")
        else:
            print("You died...")
