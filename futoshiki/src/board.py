
class Board:

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

    def move_sanity_check(self, x, y, value):
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
        sanity = self.move_sanity_check(x, y, value)
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
        # print('\t\t\tmove x:' + str(x) + ' y:' + str(y) + ' value:' + str(value) + ' is valid:' + str(valid))
        if valid:
            self.moves_stack.append((x, y, self.matrix[x][y]))
            self.matrix[x][y] = value
        if x is -1 and y is -1:
            self.moves_stack.append((x, y, self.matrix[x][y]))
        return valid

    def undo_move(self):
        # print('undo move')
        if len(self.moves_stack) is not 0:
            x, y, value = self.moves_stack.pop()
            self.matrix[x][y] = value
