import unittest
from src import read_problem, Constraint, symbol_to_indexes


filename = 'futoshiki_4_0.txt'


class ReadTestCase(unittest.TestCase):
    def test_symbol_to_indexes_simple(self):
        symbol = 'A1'
        result = symbol_to_indexes(symbol)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 0)

    def test_symbol_to_indexes(self):
        symbol = 'B3'
        result = symbol_to_indexes(symbol)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 1)

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
        expected_constraints = [Constraint(x_1=3, y_1=3, x_2=3, y_2=2)]
        result = read_problem(filename)
        self.assertListEqual(result['constraints'], expected_constraints)


if __name__ == '__main__':
    unittest.main()
