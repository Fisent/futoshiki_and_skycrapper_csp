from .board import Board


# this constraint means that field x_1,y_1 is lower than x_2,y_2
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

    def __repr__(self):
        field1 = 'field x:' + str(self.x_1) + ', y:' + str(self.y_1)
        field2 = 'field x:' + str(self.x_2) + ', y:' + str(self.y_2)
        return 'Constraint: ' + field1 + ' must be lower than ' + field2


class BoardFutoshiki(Board):
    def __init__(self, matrix, constraints, name='bezimienny'):
        self.N = len(matrix)
        self.matrix = matrix
        self.constraints = constraints
        self.moves_stack = []
        self.name = name

    def __repr__(self):
        out = ''
        for line in self.matrix:
            out += repr(line) + '\n'
        return out

    def check_constraint(self, constraint):
        lower_value = self.matrix[constraint.x_1][constraint.y_1]
        higher_value = self.matrix[constraint.x_2][constraint.y_2]
        return lower_value == 0 or higher_value == 0 or (lower_value < higher_value)
