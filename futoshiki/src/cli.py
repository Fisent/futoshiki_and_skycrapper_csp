
menu_options = 'Select option:\n' \
               '\tn - new game\n' \
               '\tq - quit\n'
prompt = '> '

def game(board):
    print(repr(board))


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
