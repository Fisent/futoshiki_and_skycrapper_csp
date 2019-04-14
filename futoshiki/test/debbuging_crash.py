import unittest
from src import read_futoshiki_problem, BoardFutoshiki, Solver


expected_solution_of_5_2= [
    [3, 5, 2, 1, 4],
    [4, 1, 3, 5, 2],
    [5, 3, 4, 2, 1],
    [1, 2, 5, 4, 3],
    [2, 4, 1, 3, 5]
]


class DebbugingCrashTestCase(unittest.TestCase):
    def test_solving_futoshiki_4_2_doesnt_crash_program(self):
        problem = read_futoshiki_problem('futoshiki_4_2.txt')
        board = BoardFutoshiki(matrix=problem['matrix'], constraints=problem['constraints'])
        # print(board.matrix)
        solver = Solver(board)
        results = solver.solve()
    #
    # def test_result_of_solving_futoshiki_5_2(self):
    #     problem = read_problem('futoshiki_5_2.txt')
    #     board = BoardFutoshiki(matrix=problem['matrix'], constraints=problem['constraints'])
    #     solver = Solver(board)
    #     results = solver.solve()
    #     print(results)
    #
    # def test_result_of_solving_futoshiki_4_1(self):
    #     problem = read_problem('futoshiki_4_1.txt')
    #     board = BoardFutoshiki(matrix=problem['matrix'], constraints=problem['constraints'])
    #     solver = Solver(board)
    #     results = solver.solve()

