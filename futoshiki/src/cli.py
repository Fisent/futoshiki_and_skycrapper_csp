from os import listdir, getcwd
import time
from src import read_futoshiki_problem, BoardFutoshiki
from .solver import Solver

menu_options = 'Select option:\n' \
               '\tn - new game\n' \
               '\tf = solve futoshiki with AI\n' \
               '\ts - solve skycrapper with AI\n'\
               '\tq - quit\n'


prompt = '> '


# loading available boards from futoshiki_test_data folder
boards = []

for filename in listdir(getcwd() + '/futoshiki_test_data/'):
    problem = read_futoshiki_problem(filename=filename, prefix=getcwd() + '/futoshiki_test_data/')
    board = BoardFutoshiki(matrix=problem['matrix'], constraints=problem['constraints'], name=problem['name'])
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


# def futoshiki_game(board):
#     running = True
#     while running:
#         print_game_state(board)
#         print('Select field')
#         try:
#             x, y = read_field()
#             value = read_value()
#             result = board.make_move(x, y, value)
#             if not result:
#                 if not board.move_sanity_checks(x, y, value):
#                     print('Sanity checks not passed')
#                 if not board.move_rows_cols_check(x, y, value):
#                     print('Rows columnts check not passed')
#                 if not board.move_constraints_check(x, y, value):
#                     print('Constraints check not passed')
#                 print('This move is illegal and will be ignored')
#         except:
#             decision = input('Wrong value, do you want to return to the menu?(y/n)' + prompt)
#             if decision == 'y':
#                 return

def futoshiki_solve():
    option = int(input('Which board do you want to solve?\n' + list_boards() + prompt))
    list_boards()
    board = boards[option]
    solution = Solver(board=board)
    start = time.time()
    results = solution.solve()
    end = time.time()
    print('Time: ' + str(end - start))
    print('Found ' + str(len(results)) + ' solutions!')
    for result in results:
        print(repr(result))
    print('kroki: ' + str(solution.counter))


def run_cli():
    running = True
    print('Welcome to futoshiki game')
    while running:
        option = input(menu_options + prompt)
        if option == 'n':
            print('Temporarly not supported')
            # futoshiki_game(board)
        elif option == 'f':
            futoshiki_solve()
        elif option == 's':
            print('Skycrapper not implemented yet')
        elif option == 'q':
            running = False
        else:
            print('Wrong command')
