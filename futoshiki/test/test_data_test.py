from os import listdir, getcwd
import unittest
from src import read_futoshiki_problem, BoardFutoshiki, Solver


prefix = getcwd() + '/futoshiki_test_data/'
unique = True


def test_for_file(filename):
    problem = read_futoshiki_problem(filename, prefix)
    board = BoardFutoshiki(problem['matrix'], problem['constraints'])
    solver = Solver(board)
    results = solver.solve()

    print(filename + ' number of results: ' + str(len(results)))
    for result in results:
        print(result)

    if not check_if_unique(results):
        global uniqueq
        unique = False


def check_if_unique(lst):
    new_list = []
    result = True
    for e in lst:
        if e in new_list:
            result = False
        new_list.append(e)
    return result


filenames = []


for file in listdir(prefix):
    filenames.append(file)


class TestDataCase(unittest.TestCase):
    pass
    def test_all(self):
        for file in filenames:
            test_for_file(file)

        global unique
        self.assertTrue(unique)


