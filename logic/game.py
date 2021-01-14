from logic.dice import Dice


class Game:
    def __init__(self) -> None:
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.players = []

    def launch_dices(self) -> None:
        for dice in self.dices:
            if not dice.keep:
                dice.throw_dice()

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

    def choose_dices(self) -> None:
        i = 0
        while i < len(self.dices):
            print("dice ["+i + "] result : "+self.dices[i].value)
        answer = input("veuillez entrer les numéros des dés à garder " +
                       "séparés par une virgule et sans espace \n" + "ex: \"0, 3, 4\"")
        for index in answer.split(","):
            self.dices[int(index)].keep = True

    def play_turn(self, player) -> None:
        self.reset_dices()
        i = 0
        while i < 3 and not self.check_if_all_kept():
            i += 1
            self.launch_dices()
            self.choose_dices
        

