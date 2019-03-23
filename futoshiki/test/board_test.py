import unittest
from src import Board, Constraint


def create_board():
    matrix = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [3, 1, -1, -1, -1],
        [5, -1, -1, -1, -1]
    ]
    constraints = [
        Constraint(1, 1, 0, 1),
        Constraint(2, 0, 1, 0),
        Constraint(3, 0, 1, 0),
        Constraint(2, 2, 2, 1),
        Constraint(2, 4, 2, 3),
        Constraint(4, 4, 3, 4)
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


class BoardTestCase(unittest.TestCase):
    def board_is_created(self):
        board = create_board()
        print(board.matrix[0][1])
        print(board)

    def board_solves_problem(self):
        board = create_board()
        result_matrix = create_expected_result_matrix()


if __name__ == '__main__':
    unittest.main()
