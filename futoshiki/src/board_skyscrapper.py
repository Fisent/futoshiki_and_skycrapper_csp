from enum import Enum
from .board import Board


# This constraint means that from direction 'direction' there should be visible N buildings
# Directions:
# G - up
# D - down
# L - left
# P - right


class Direction(Enum):
    up = 0
    down = 1
    left = 2
    right = 3


def create_N_N_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        matrix.append(row)
    return matrix


def how_many_visible(array):
    counter = 0
    max_height = 0
    for element in array:
        if element > max_height:
            counter += 1
            max_height = element
    return counter


class ConstraintSkyscrapper:

    def parse_direction(self, direction):
        if direction == 'G':
            self.direction = Direction.up
        elif direction == 'D':
            self.direction = Direction.down
        elif direction == 'L':
            self.direction = Direction.left
        elif direction == 'P':
            self.direction = Direction.right
        else:
            raise Exception('Impossible direction value')

    def __init__(self, direction, index, N):
        self.parse_direction(direction)
        self.index = index
        self.N = N

    def __eq__(self, other):
        return self.direction == other.direction and self.N == other.N

    def __repr__(self):
        return 'Skyscrapper constraints, direction:  ' + str(self.direction) + ', index:' + str(self.index)  +', no of visible buildings: ' + str(self.N)


class BoardSkyscrapper(Board):

    def __init__(self, N, constraints):
        self.N = N
        self.matrix = create_N_N_matrix(N)
        self.constraints = constraints
        self.moves_stack = []

    def get_col(self, index):
        col = []
        for row in self.matrix:
            col.append(row[index])
        return col

    def check_constraint(self, constraint):
        array = []
        if constraint.direction == Direction.up:
            array = self.get_col(constraint.index).copy()
        elif constraint.direction == Direction.down:
            array = self.get_col(constraint.index).copy()
            array.reverse()
        elif constraint.direction == Direction.left:
            array = self.matrix[constraint.index].copy()
        elif constraint.direction == Direction.right:
            array = self.matrix[constraint.index].copy()
            array.reverse()
        no_of_visible_buildings = how_many_visible(array)
        return no_of_visible_buildings == constraint.N
