from entity.player import Player
from entity.enemy import Enemy
from game.game import Game
from game.items import Items


if __name__ == "__main__":
    player = Player()
    Game.main_loop(player)
