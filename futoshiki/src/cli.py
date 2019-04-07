
menu_options = 'Select option:\n' \
               '\tn - new game\n' \
               '\tq - quit\n'


prompt = '> '


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


def run_cli(board):
    running = True
    print('Welcome to futoshiki game')
    while running:
        option = input(menu_options + prompt)
        if option == 'n':
            game(board)
        elif option == 'q':
            running = False
        else:
            print('Wrong command')
