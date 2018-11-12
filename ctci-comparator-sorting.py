#https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return self.name + " " + str(self.score)
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score:
            if a.name < b.name:
                return -1
            return 0
        return 1