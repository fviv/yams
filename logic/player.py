from logic.score_sheet import ScoreSheet


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.score_sheet = ScoreSheet()
