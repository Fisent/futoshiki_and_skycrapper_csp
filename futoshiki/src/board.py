
# this constraint means that field x_1,y_1 is higher than x_2,y_2
class Constraint:
    def __init__(self, x_1: int, y_1: int, x_2: int, y_2: int):
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2

    def __eq__(self, other):
        x = self.x_1 == other.x_1 and self.x_2 == other.x_2
        y = self.y_1 == other.y_1 and self.y_2 == other.y_2
        return x and y


class Board:
    def __init__(self, matrix, constraints):
        self.matrix = matrix
        self.constraints = constraints

    def __repr__(self):
        out = ''
        for line in self.matrix:
            out += repr(line) + '\n'
        return out
