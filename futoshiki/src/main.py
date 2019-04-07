from cli import run_cli
from board import Board

def main_cli():
    b = Board(matrix=[], constraints=[])
    run_cli(b)

main_cli()
