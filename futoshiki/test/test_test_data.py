from os import listdir, getcwd
import unittest
from src import read_problem, BoardFutoshiki, Solver


prefix = getcwd() + '/futoshiki_test_data/'


def test_for_file(filename):
    problem = read_problem(filename, prefix)
    board = BoardFutoshiki(problem['matrix'], problem['constraints'])
    solver = Solver(board)
    results = solver.solve()
    print(filename + ' number of results: ' + str(len(results)))
    print(results)


filenames = []


for file in listdir(prefix):
    filenames.append(file)


class TestDataCase(unittest.TestCase):
    pass
    # def test_all(self):
    #     for file in filenames:
    #         test_for_file(file)
