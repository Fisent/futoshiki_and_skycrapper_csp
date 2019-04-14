import unittest
from src import BoardSkyscrapper, ConstraintSkyscrapper, read_skyscrapper_problem, how_many_visible


def create_board():
    problem = read_skyscrapper_problem('skyscrapper_4_0.txt')
    board = BoardSkyscrapper(problem['N'], problem['constraints'])
    board.matrix[0][0] = 1
    return board


def create_board_to_check_constraints(constraints=[]):
    matrix_to_check_constraints = [
        [1, 2, 3],
        [2, 3, 1],
        [3, 1, 0]
    ]

    board = BoardSkyscrapper(N=3, constraints=constraints)
    board.matrix = matrix_to_check_constraints
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

    def test_get_col(self):
        board = create_board_to_check_constraints()
        self.assertListEqual(board.get_col(0), [1, 2, 3])
        self.assertListEqual(board.get_col(1), [2, 3, 1])
        self.assertListEqual(board.get_col(2), [3, 1, 0])

    # def test_how_many_visible(self):
    #     one_visible = [3, 2, 1]
    #     two_visible = [2, 3, 1]
    #     three_visible = [1, 2, 3]
    #     one_visible_long = [7, 4, 2, 1, 3, 5, 6]
    #     three_visible_long = [3, 1, 4, 7, 2, 5, 6]
    #
    #     self.assertEqual(how_many_visible(one_visible), 1)
    #     self.assertEqual(how_many_visible(two_visible), 2)
    #     self.assertEqual(how_many_visible(three_visible), 3)
    #     self.assertEqual(how_many_visible(one_visible_long), 1)
    #     self.assertEqual(how_many_visible(three_visible_long), 3)

    def test_board_constraint_check(self):
        constraint_pass = ConstraintSkyscrapper(direction='L', index=0, N=3)
        constraint_fail = ConstraintSkyscrapper(direction='G', index=0, N=1)
        constraint_pass_harder = ConstraintSkyscrapper(direction='P', index=0, N=1)
        constraint_fail_harder = ConstraintSkyscrapper(direction='D', index=0, N=3)

        board = create_board_to_check_constraints()
        self.assertTrue(board.check_constraint(constraint_pass))
        self.assertFalse(board.check_constraint(constraint_fail))
        self.assertTrue(board.check_constraint(constraint_pass_harder))
        self.assertFalse(board.check_constraint(constraint_fail_harder))

    def test_board_move_constraints_check(self):
        constraints_for_value_2 = [
            ConstraintSkyscrapper(direction='P', index=2, N=2),
            ConstraintSkyscrapper(direction='D', index=2, N=2)
        ]

        constraints_for_value_1 = [
            ConstraintSkyscrapper(direction='P', index=2, N=1),
            ConstraintSkyscrapper(direction='D', index=2, N=1)
        ]

        board_for_val_2 = create_board_to_check_constraints(constraints=constraints_for_value_2)
        self.assertTrue(board_for_val_2.move_constraints_check(2, 2, 2))

        board_for_val_1 = create_board_to_check_constraints(constraints=constraints_for_value_1)
        self.assertTrue(board_for_val_1.move_constraints_check(2, 2, 3))
