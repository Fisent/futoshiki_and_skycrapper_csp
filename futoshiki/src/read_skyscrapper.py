from os import getcwd
from src import ConstraintSkyscrapper

test_data_prefix = getcwd() + '/skyscrapper_test_data/'


def read_skyscrapper_problem(filename, prefix=''):
    if prefix == '':
        prefix = test_data_prefix

    f = open(prefix + filename)
    N = int(f.readline())

    constraints = []
    for line in f:
        tab = line.split(';')
        for i in range(1, N + 1):
            value = int(tab[i])
            if value != 0:
                constraints.append(ConstraintSkyscrapper(direction=tab[0], index=i, N=value))


    f.close()
    return {
        'N': N,
        'constraints': constraints
    }
