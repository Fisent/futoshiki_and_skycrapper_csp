from copy import deepcopy


class Solution:

    def create_domains_matrix(self):
        domains_matrix = []
        for row in self.board.matrix:
            r = []
            for cell in row:
                r.append(list(range(1, self.board.N + 1)))
            domains_matrix.append(r)
        return domains_matrix

    def initially_remove_impossible_values_from_domains(self):
        for i in range(len(self.board.matrix)):
            for j in range(len(self.board.matrix[0])):
                board_value = self.board.matrix[i][j]
                if board_value is not 0:
                    self.domains_matrix[i][j] = [board_value]

    def __init__(self, board):
        self.board = board
        self.domains_matrix = self.create_domains_matrix()
        self.initially_remove_impossible_values_from_domains()
        self.results = []

    def remove_value_from_domain(self, x, y, value):
        self.domains_matrix[x][y].remove(value)

    def increment_indexes(self,x, y):
        if y + 1 >= self.board.N:
            if x + 1 >= self.board.N:
                return -1, -1
            x += 1
            y = 0
        else:
            y += 1
        return x, y

    def solve_step(self, x, y):
        print('Step for x: ' + str(x) + ', y: ' + str(y))
        print('Board state: ' + str(self.board.matrix))
        inc_x, inc_y = self.increment_indexes(x, y)

        for value in self.domains_matrix[x][y]:
            print('    value: ' + str(value))
            move_made = self.board.make_move(x, y, value)

            if inc_x is not -1 and inc_y is not -1 and move_made:
                self.solve_step(inc_x, inc_y)

            if not move_made:
                won = self.board.win_check()
                if won:
                    self.results.append(deepcopy(self.board.matrix))
        self.board.undo_move()

    def solve(self):
        self.solve_step(0, 0)
        return self.results
