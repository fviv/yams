

class Combination:
    def __init__(self, points, pattern):
        self.points = points
        self.used = False
        self.patter = pattern

    def check_if_valid(self, dices) -> bool:
