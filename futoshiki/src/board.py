
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


class Board:
    def __init__(self, matrix, constraints):
        self.N = len(matrix)
        self.matrix = matrix
        self.constraints = constraints
        self.moves_stack = []

    def __repr__(self):
        out = ''
        for line in self.matrix:
            out += repr(line) + '\n'
        return out

    def is_value_in_row_(self, x, value):
        row = self.matrix[x]
        for i in row:
            if i == value:
                return True
        return False

    def is_value_in_col_(self, y, value):
        col = []
        for row in self.matrix:
            col.append(row[y])
        for i in col:
            if i == value:
                return True
        return False

    def check_constraint(self, constraint):
        lower_value = self.matrix[constraint.x_1][constraint.y_1]
        higher_value = self.matrix[constraint.x_2][constraint.y_2]
        return lower_value == 0 or higher_value == 0 or (lower_value < higher_value)

    def move_sanity_checks(self, x, y, value):
        return 0 <= x < self.N and 0 <= y < self.N and 0 < value <= self.N

    def move_rows_cols_check(self, x, y, value):
        return not self.is_value_in_row_(x=x, value=value) and not self.is_value_in_col_(y=y, value=value)

    def move_constraints_check(self, x, y, value):
        old_value = self.matrix[x][y]
        self.matrix[x][y] = value
        result = True
        for con in self.constraints:
            result = result and self.check_constraint(con)
        self.matrix[x][y] = old_value
        return result

    def is_move_valid(self, x, y, value):
        sanity = self.move_sanity_checks(x, y, value)
        rows_cols = self.move_rows_cols_check(x, y, value)
        constraints = self.move_constraints_check(x, y, value)
        return sanity and rows_cols and constraints or self.matrix[x][y] is value

    def win_check(self):
        won = True
        for row in self.matrix:
            for value in row:
                if value is 0:
                    won = False
        return won

    def make_move(self, x, y, value):
        valid = self.is_move_valid(x, y, value)
        if valid:
            self.moves_stack.append((x, y, self.matrix[x][y]))
            self.matrix[x][y] = value
        return valid

    def undo_move(self):
        print('undo move')
        x, y, value = self.moves_stack.pop()
        self.matrix[x][y] = value
