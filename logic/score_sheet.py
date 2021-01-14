from logic.combinations.combinations_manager import CombinationsManager


class ScoreSheet:
    def __init__(self) -> None:
        self.combinations_manager = CombinationsManager()

    def __sort_results(self, dices) -> list:
        results = []
        for dice in dices:
            if len(results) == 0:
                results.append(dice.value)
            else:
                i = 0
                j = len(results)
                while i < j:
                    if dice.value < results[i]:
                        results.insert(i, dice.value)
                        break
                    i += 1
                if i == j:
                    results.append(dice.value)
        return results

    def get_possible_points(self, dices):

        results = ""
        for value in self.__sort_results(dices):
            results += str(value)
        self.combinations_manager.get_possible_points(results)
