import unittest
from src import read_skyscrapper_problem, ConstraintSkyscrapper


expected_constraints_skyscrapper_4_0 = [
    ConstraintSkyscrapper('G', index=0, N=2),
    ConstraintSkyscrapper('G', index=1, N=3),
    ConstraintSkyscrapper('G', index=3, N=1),

    ConstraintSkyscrapper('D', index=1, N=1),
    ConstraintSkyscrapper('D', index=2, N=2),
    ConstraintSkyscrapper('D', index=3, N=4),

    ConstraintSkyscrapper('P', index=0, N=2),

    ConstraintSkyscrapper('L', index=0, N=3)
]




class ReadSkyscrapperTestCase(unittest.TestCase):

    def test_read_N_skyscrapper_4_0(self):
        problem = read_skyscrapper_problem(filename='skyscrapper_4_0.txt')
        self.assertEqual(problem['N'], 4)

    def test_read_constraints_skyscrapper_4_0(self):
        problem = read_skyscrapper_problem(filename='skyscrapper_4_0.txt')
        expected = expected_constraints_skyscrapper_4_0
        self.assertListEqual(expected_constraints_skyscrapper_4_0, problem['constraints'])
