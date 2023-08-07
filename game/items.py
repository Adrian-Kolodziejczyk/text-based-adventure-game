from random import randint


class Items:
    items = []
    weapon_names = ["Sword", "Staff", "Dagger", "Bow"]
    utility_names = ["Health potion", "Level-up potion"]
    all_names = weapon_names + utility_names

    def __init__(self, type):
        match type:
            case "weapon":
                self.name = Items.weapon_names[randint(0, len(Items.weapon_names) - 1)]
            case "utility":
                self.name = Items.utility_names[
                    randint(0, len(Items.utility_names) - 1)
                ]
            case "random":
                self.name = Items.all_names[randint(0, len(Items.all_names) - 1)]
            case _:
                pass
        Items.items.append(self)

    def __repr__(self) -> str:
        return f"{self.name}"


# item1 = Items("weapon")
# item2 = Items("utility")
# item3 = Items("random")
# print(Items.items)
