
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

