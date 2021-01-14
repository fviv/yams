import re


class Combination:

    def __init__(self, name, pattern, points):
        self.name = name
        self.used = False
        self.pattern = pattern
        self.points = points

    def check_if_valid(self, results) -> int:

        if self.used == True:
            return 0
        if self.points == "sum":
            return results.count(self.pattern)*int(self.pattern)
        elif self.points == "total":
            regex = re.compile(self.pattern)
            occurence = regex.findall(results)
            if len(occurence) == 0:
                return 0
            else:
                total = 0
                if len(occurence[0]) != 1 and len(occurence[0]) != 5:
                    occurence[0] = occurence[0][0]
                for char in occurence[0]:
                    total += int(char)
                return total
        else:
            regex = re.compile(self.pattern)
            occurence = regex.findall(results)
            if len(occurence) == 0:
                return 0
            else:
                return self.points
