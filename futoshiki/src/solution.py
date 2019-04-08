
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
                    self.domains_matrix[i][j].remove(board_value)

    def __init__(self, board):
        self.board = board
        self.domains_matrix = self.create_domains_matrix()
        self.initially_remove_impossible_values_from_domains()

    def remove_value_from_domain(self, x, y, value):
        self.domains_matrix[x][y].remove(value)

    def solve_step(self):
        pass
