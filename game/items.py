from random import randint, choice

# from game.game import Game


class Items:
    items = []
    weapon_names = ["Sword", "Staff", "Dagger", "Bow"]
    utility_names = ["Health potion", "Level-up potion"]
    all_names = weapon_names + utility_names

    def __init__(self, type):
        match type:
            case "weapon":
                self.name = choice(Items.weapon_names)
                self.weapon_min_damage = 1
                self.weapon_max_damage = randint(1, 9)  # test values
            case "utility":
                self.name = Items.utility_names[
                    randint(0, len(Items.utility_names) - 1)
                ]
            case "random":
                self.name = choice(Items.all_names)
                if self.name in Items.weapon_names:
                    self.weapon_min_damage = 1
                    self.weapon_max_damage = randint(1, 9)  # test values
            case _:
                pass

    def __repr__(self) -> str:
        return f"{self.name}"

    def generate_item(player, type):
        player.inventory.append(Items(type))
        print(f"You have gained a new {type} item!")
