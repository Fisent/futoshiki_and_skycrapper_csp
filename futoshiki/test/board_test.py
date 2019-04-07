import unittest
from src import Board, Constraint


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


def create_expected_result_matrix():
    matrix = [
        [4, 2, 3, 5, 1],
        [1, 5, 2, 3, 4],
        [2, 3, 4, 1, 5],
        [3, 1, 5, 4, 2],
        [5, 4, 1, 2, 3]
    ]
    return matrix


class BoardTestCase(unittest.TestCase):

    def test_board_move_sanity_checks(self):
        board = create_board()
        self.assertFalse(board.move_sanity_checks(15, 15, 1))
        self.assertTrue(board.move_sanity_checks(1, 1, 1))
        self.assertFalse(board.move_sanity_checks(1, 1, 15))

    def test_board_move_rows_cols_checks(self):
        board = create_board()
        self.assertTrue(board.move_rows_cols_check(x=1, y=0, value=1))
        self.assertFalse(board.move_rows_cols_check(x=1, y=0, value=3))

    def test_board_move_constraints_checks(self):
        board = create_board()
        self.assertTrue(board.move_constraints_check(x=4, y=4, value=1))
        self.assertFalse(board.move_constraints_check(x=4, y=4, value=3))

    def test_board_makes_move(self):
        board = create_board()
        result = board.make_move(0, 0, 1)
        self.assertTrue(result)
        self.assertEqual(board.matrix[0][0], 1)
        result = board.make_move(0, 0, 5)
        self.assertFalse(result)
        self.assertEqual(board.matrix[0][0], 1)

    def test_board_checks_win_condition(self):
        matrix = create_expected_result_matrix()
        solved_board = Board(matrix=matrix, constraints=[])
        unsolved_board = create_board()
        self.assertFalse(unsolved_board.win_check())
        self.assertTrue(solved_board.win_check())


    def test_board_solves_problem(self):
        pass


if __name__ == '__main__':
    unittest.main()
