from entity.entity import Player
from game.game import Game


if __name__ == "__main__":
    player = Player()
    Game.main_loop(player)
