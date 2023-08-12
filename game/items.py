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
                self.equippable = 1
                self.weapon_min_damage = 1
                self.weapon_max_damage = randint(1, 9)  # test values
            case "utility":
                self.name = choice(Items.utility_names)
                self.equippable = 0
                match self.name:
                    case "Health potion":
                        self.healing = 25
                    case _:
                        self.levelup = 1
            case "random":
                self.name = choice(Items.all_names)
                if self.name in Items.weapon_names:
                    self.equippable = 1
                    self.weapon_min_damage = 1
                    self.weapon_max_damage = randint(1, 9)  # test values
                elif self.name in Items.utility_names:
                    self.equipable = 0
                    match self.name:
                        case "Health potion":
                            self.healing = 25
                        case _:
                            self.levelup = 1
                    pass

            case _:
                pass

    def __repr__(self) -> str:
        return f"{self.name}"

    def generate_item(player, type):
        player.inventory.append(Items(type))
        print(f"You have gained a new {type} item!")

    def use_item():
        pass
