from logic.player import Player
from logic.game import Game

g = Game()
p = Player("felix")
g.add_player(p)
g.play_turn(p)
