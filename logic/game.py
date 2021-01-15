from logic.dice import Dice


class Game:
    def __init__(self) -> None:
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.players = []

    def __init__(self, players) -> None:
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.players = players

    def launch_dices(self) -> None:
        for dice in self.dices:
            if not dice.keep:
                dice.throw_dice()
        self.reset_dices()

    def add_player(self, player) -> None:
        self.players.append(player)

    def reset_dices(self) -> None:
        for dice in self.dices:
            dice.keep = False

    def check_if_all_kept(self) -> bool:
        for dice in self.dices:
            if dice.keep == False:
                return False
        return True

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def keep_dice(self, dice) -> None:
        dice.keep = True

    def play_turn(self, player) -> None:
        i = 0
        while i < 3 and not self.check_if_all_kept():
            i += 1
            self.launch_dices()
            player.score_sheet.get_possible_points(self.dices)

    def reset_game(self):
        self = Game(self.players)

