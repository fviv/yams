import re


class Combination:

    def __init__(self, name, pattern, points):
        self.name = name
        self.used = False
        self.pattern = pattern
        self.points = points
        self.points_gained_if_chosen = 0

    def check_if_valid(self, results) -> int:

        if self.used == True:
            return
        if self.points == "sum":
            self.points_gained_if_chosen = results.count(
                self.pattern)*int(self.pattern)
        elif self.points == "total":
            regex = re.compile(self.pattern)
            occurence = regex.findall(results)
            if len(occurence) == 0:
                self.points_gained_if_chosen = 0
            else:
                total = 0
                if len(occurence[0]) != 1 and len(occurence[0]) != 5:
                    occurence[0] = occurence[0][0]
                for char in occurence[0]:
                    total += int(char)
                self.points_gained_if_chosen = total
        else:
            regex = re.compile(self.pattern)
            occurence = regex.findall(results)
            if len(occurence) == 0:
                self.points_gained_if_chosen = 0
            else:
                self.points_gained_if_chosen = self.points
