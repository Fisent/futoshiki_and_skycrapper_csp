import unittest
from src import BoardSkyscrapper, ConstraintSkyscrapper

def create_board():
    board = [
        [0, 0, 0],
        [0, 3, 0],
        [0, 0, 0]
    ]


class SkyscrapperBoardCase(unittest.TestCase):

    def test_constraint_throws_exception_on_impossible_direction(self):
        with self.assertRaises(Exception):
            c1 = ConstraintSkyscrapper(direction='DUPA', index=0, N=0)
        c2 = ConstraintSkyscrapper('D', index=0, N=1)
        print(c2)

    def test_board_makes_move(self):
        pass
