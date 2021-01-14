import random


class Dice:
    def __init__(self) -> None:
        self.random = random
        self.value = 0

    def throw_dice(self) -> int:
        self.value = self.random.randint(1, 6)
        return self.value
