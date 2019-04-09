from os import listdir, getcwd
from src import read_problem, Board
from .solution import Solution

menu_options = 'Select option:\n' \
               '\tn - new game\n' \
               '\ts = solve with AI\n' \
               '\tq - quit\n'


prompt = '> '


# loading available boards from test_data folder
boards = []

for filename in listdir(getcwd() + '/test_data'):
    problem = read_problem(filename)
    board = Board(matrix=problem['matrix'], constraints=problem['constraints'], name=problem['name'])
    boards.append(board)


def read_field():
    x = input('x ' + prompt)
    y = input('y' + prompt)
    return int(x), int(y)


def read_value():
    value = input('value: ' + prompt)
    return int(value)


def print_game_state(board):
    print(repr(board))
    for c in board.constraints:
        print(repr(c))


def list_boards():
    out = ''
    if range(len(boards)) is 0:
        print('Warning! There are no available boards!')
    for i in range(len(boards)):
        out += str(i) + ' - ' + boards[i].name + '\n'
    return out


def game(board):
    running = True
    while running:
        print_game_state(board)
        print('Select field')
        try:
            x, y = read_field()
            value = read_value()
            result = board.make_move(x, y, value)
            if not result:
                if not board.move_sanity_checks(x, y, value):
                    print('Sanity checks not passed')
                if not board.move_rows_cols_check(x, y, value):
                    print('Rows columnts check not passed')
                if not board.move_constraints_check(x, y, value):
                    print('Constraints check not passed')
                print('This move is illegal and will be ignored')
        except:
            decision = input('Wrong value, do you want to return to the menu?(y/n)' + prompt)
            if decision == 'y':
                return


def solve():
    option = int(input('Which board do you want to solve?\n' + list_boards() + prompt))
    list_boards()
    board = boards[option]
    solution = Solution(board=board)
    results = solution.solve()
    for result in results:
        print(repr(result))


def run_cli(board):
    running = True
    print('Welcome to futoshiki game')
    while running:
        option = input(menu_options + prompt)
        if option == 'n':
            game(board)
        if option == 's':
            solve()
        elif option == 'q':
            running = False
        else:
            print('Wrong command')
