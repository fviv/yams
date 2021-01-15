from typing import List
from logic.combinations.combination import Combination


class CombinationsManager:
    def __init__(self):
        self.combinations_constructors = [["ones", "1", "sum"], [
            "twos", "2", "sum"], ["threes", "3", "sum"], ["fours", "4", "sum"], ["fives", "5", "sum"], [
                "sixes", "6", "sum"], ["brelan", "((.)\\2{2})", "total"], ["carré", "((.)\\2{3})", "total"], [
                    "full house", "((.)\\2{2}(.)\\3{1}|(.)\\4{1}(.)\\5{2})", "25"], ["petite suite", "(1234|2345|3456)", "30"], [
                        "grande suite", "(12345|23456)", "40"], ["yams", "(.)\\1{4}", "50"],  ["chance", ".+", "total"]]
        self.combinations = self.__get_combinations()

    def __get_combinations(self) -> list:
        combinations = []
        for combination in self.combinations_constructors:
            combinations.append(Combination(
                combination[0], combination[1], combination[2]))
        return combinations

    def get_possible_points(self, results):
        for combination in self.combinations:
            combination.check_if_valid(results)
