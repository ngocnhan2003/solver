
from colorit import color, Colors, init_colorit

init_colorit()


def cl(value):
    if value != 0:
        return color(value, Colors.red)
    return value


class Cell:
    value = 0
    notes = []
    block = False
    H = 0
    V = 0
    h = 0
    v = 0

    def __init__(self, H, V, value):
        self.H = H
        self.V = V
        self.value = value
        if value != 0:
            self.block = True
        else:
            self.notes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.notes.remove(value)
        self.h = H % 3
        self.v = V % 3

    def get_value(self):
        return self.value

    def get_pos(self):
        return f'{self.H}:{self.V}'

    def on_border(self, pos):
        return pos if 0 <= pos <= 8 else -1

    def cell_on_left(self):
        return self.on_border(self.H -1)
    
    def cell_on_right(self):
        return self.on_border(self.H + 1)

    def cell_on_above(self):
        return self.on_border(self.V - 1)

    def cell_on_below(self):
        return self.on_border(self.V + 1)


class Matrix:
    cells = []
    sudoku = {}

    def __init__(self):
        pass

    def add(self, cell):
        self.sudoku[cell.get_pos()] = cell.get_value()
        if cell.get_value() != 0:
            self.cells.append(cell)

    def print(self):
        for v in range(0, 9):
            for h in range(0, 9):
                 print(cl(self.sudoku[f'{v}:{h}']), end='\t')
            print('\n')


def load_from_file(file_path):
    matrix = Matrix()
    sdk = open(file_path).read()
    vi = 0
    for v in sdk.split('\n'):
        hi = 0
        for h in v.split(' '):
            matrix.add(Cell(vi, hi, int(h)))
            hi += 1
        vi += 1
    return matrix


matrix = load_from_file('sudoku.input')
matrix.print()
