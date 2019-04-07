import unittest
from src import read_problem, Constraint


filename = 'futoshiki_4_0.txt'


class ReadTestCase(unittest.TestCase):
    def test_symbol_to_indexes(self):
        pass

    def test_read_N(self):
        result = read_problem(filename)
        self.assertEqual(result['N'], 4)

    def test_read_matrix(self):
        expected_matrix = [
            [0, 0, 0, 3],
            [0, 1, 0, 0],
            [2, 0, 0, 0],
            [4, 0, 0, 0]
        ]
        result = read_problem(filename)
        self.assertEqual(result['matrix'], expected_matrix)

    def test_read_constraints(self):
        # expected_constraints = [Constraint(x_1=)]
        pass


if __name__ == '__main__':
    unittest.main()
