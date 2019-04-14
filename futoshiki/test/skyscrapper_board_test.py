import unittest
from src import BoardSkyscrapper, ConstraintSkyscrapper, read_skyscrapper_problem

def create_board():
    problem = read_skyscrapper_problem('skyscrapper_4_0.txt')
    board = BoardSkyscrapper(problem['N'], problem['constraints'])
    board.matrix[0][0] = 1
    return board


class SkyscrapperBoardCase(unittest.TestCase):

    def test_constraint_throws_exception_on_impossible_direction(self):
        with self.assertRaises(Exception):
            c1 = ConstraintSkyscrapper(direction='DUPA', index=0, N=0)
        c2 = ConstraintSkyscrapper('D', index=0, N=1)
        print(c2)

    def test_board_sanity_check(self):
        board = create_board()
        self.assertTrue(board.move_sanity_check(x=0, y=0, value=1))
        self.assertFalse(board.move_sanity_check(x=board.N + 10, y=0, value=1))
        self.assertFalse(board.move_sanity_check(x=-10, y=0, value=10))

    def test_board_rows_cols_check(self):
        board = create_board()
        self.assertFalse(board.move_rows_cols_check(0, 1, 1))
        self.assertTrue(board.move_rows_cols_check(0, 1, 2))

    def test_board_constraint_check(self):
        pass
        # TODO
