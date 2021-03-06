from src import Constraint
from os import getcwd

data_file_prefix = 'futoshiki_test_data/'


letter_to_index_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10
}


def symbol_to_indexes(symbol):
    letter = symbol[0]
    number = int(symbol[1]) - 1
    return number, letter_to_index_map[letter]


# returns dict with keys: N, matrix, constraints
def read_futoshiki_problem(filename, prefix=''):
    if prefix == '':
        prefix = data_file_prefix
    f = open(prefix + filename)
    N = int(f.readline())

    if f.readline() != 'START:\n':
        print('WARNING! "START" string not found in file where it is expected')

    # read matrix
    matrix = []
    line = f.readline()
    while line != 'REL:\n':
        matrix_row = []
        tab = line.split(';')
        for i in tab:
            matrix_row.append(int(i))
        matrix.append(matrix_row)
        line = f.readline()

    # read constraints
    constraints = []
    for line in f:
        tab = line.split(';')
        symbols = []
        for symbol in tab:
            symbols.append(symbol_to_indexes(symbol))
        constraints.append(Constraint(x_1=symbols[0][0], y_1=symbols[0][1], x_2=symbols[1][0], y_2=symbols[1][1]))

    f.close()
    return {
        'N': N,
        'matrix': matrix,
        'constraints': constraints,
        'name': filename
    }
