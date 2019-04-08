import unittest
from src import Board, Constraint, Solution


def create_board():
    matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [3, 1, 0, 0, 2],
        [5, 0, 0, 0, 0]
    ]
    constraints = [
        Constraint(4, 4, 3, 4),
    ]

    return Board(matrix, constraints)


def create_simple_board():
    matrix = [
        [1, 0],
        [0, 0]
    ]
    return Board(matrix, [])


def create_solution():
    board = create_board()
    solution = Solution(board)
    return solution


def create_simple_solution():
    board = create_simple_board()
    s = Solution(board)
    return s


simple_board_expected_solution = [
    [1, 2],
    [2, 1]
]


class SolutionTestCase(unittest.TestCase):

    def test_solution_creation_from_board(self):
        solution = create_solution()
        self.assertEqual(solution.board.N, len(solution.domains_matrix))
        self.assertEqual(solution.board.N, len(solution.domains_matrix[0]))

    def test_solution_initially_removes_impossible_values_from_domains(self):
        s = create_solution()
        expected_domain_row_4_col_0 = [5]
        expected_domain_row_3_col_0 = [3]
        expected_domain_row_3_col_4 = [2]
        expected_domain_row_0_col_0 = [1, 2, 3, 4, 5]
        self.assertListEqual(s.domains_matrix[4][0], expected_domain_row_4_col_0)
        self.assertListEqual(s.domains_matrix[3][0], expected_domain_row_3_col_0)
        self.assertListEqual(s.domains_matrix[3][4], expected_domain_row_3_col_4)
        self.assertListEqual(s.domains_matrix[0][0], expected_domain_row_0_col_0)

    def test_solution_increments_indexes(self):
        s = create_solution()
        self.assertTupleEqual(s.increment_indexes(0, 0), (0, 1))
        self.assertTupleEqual(s.increment_indexes(0, 4), (1, 0))
        self.assertTupleEqual(s.increment_indexes(4, 4), (-1, -1))

    def test_solution_solves_simple_board(self):
        s = create_simple_solution()
        results = s.solve()
        self.assertListEqual(results[0], simple_board_expected_solution)


if __name__ == '__main__':
    unittest.main()
