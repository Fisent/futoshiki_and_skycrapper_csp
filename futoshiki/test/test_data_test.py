from os import listdir, getcwd
import unittest
from src import read_futoshiki_problem, BoardFutoshiki, Solver, read_skyscrapper_problem, BoardSkyscrapper


prefix = getcwd() + '/futoshiki_test_data/'
unique = True


skyscrapper_prefix = getcwd() + '/skyscrapper_test_data/'


def test_for_futoshiki_file(filename):
    print(filename)
    problem = read_futoshiki_problem(filename, prefix)
    board = BoardFutoshiki(problem['matrix'], problem['constraints'])
    solver = Solver(board)
    results = solver.solve()

    print(' number of results: ' + str(len(results)))
    for result in results:
        print(result)

    if not check_if_unique(results):
        global uniqueq
        unique = False

def test_for_skyscrapper_file(filename):
    print(filename)
    problem = read_skyscrapper_problem(filename, skyscrapper_prefix)
    board = BoardSkyscrapper(N=problem['N'], constraints=problem['constraints'], name=problem['name'])
    solver = Solver(board)
    results = solver.solve()

    print(filename + ' number of results: ' + str(len(results)))
    for result in results:
        print(result)

    if not check_if_unique(results):
        global unique
        unique = False


def check_if_unique(lst):
    new_list = []
    result = True
    for e in lst:
        if e in new_list:
            result = False
        new_list.append(e)
    return result


def get_filenames(prefix):
    filenames = []
    for file in listdir(prefix):
        filenames.append(file)
    return filenames


class TestDataCase(unittest.TestCase):
    pass
    def test_all_futoshiki(self):
        print('\n=============FUTOSHIKI TESTING=============\n')
        filenames = get_filenames(prefix=prefix)
        for file in filenames:
            test_for_futoshiki_file(file)

        global unique
        self.assertTrue(unique)

    def test_all_skyscrapper(self):
        print('\n=============SKYSCRAPPER TESTING=============\n')
        filenames = get_filenames(prefix=skyscrapper_prefix)
        for file in filenames:
            test_for_skyscrapper_file(file)


