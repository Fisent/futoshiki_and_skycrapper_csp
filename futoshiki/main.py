from src import run_cli
from src import Board
from src import read_problem


def main_cli():
    file_dict = read_problem('futoshiki_4_0.txt')
    b = Board(matrix=file_dict['matrix'], constraints=file_dict['constraints'])
    run_cli(b)


main_cli()
