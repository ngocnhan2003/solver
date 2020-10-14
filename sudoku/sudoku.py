
import os
from pprint import pprint
from colorit import color as fg, background as bg

os.system("clear")


def color(v, h, value):
    iv = int(v / 3)
    ih = int(h / 3)
    return bg(
        fg(f' {value} ', (0, 0, 0) if value != 0 else (200, 200, 200)),
        (180, 180, 180) if iv in [0, 2] and ih in [0, 2] or iv == ih == 1 else (140, 140, 140)
    )


class Cell:
    value = 0
    notes = []
    block = False
    v = 0
    h = 0

    def __init__(self, v, h, value):
        self.value = value
        if value != 0:
            self.block = True
        else:
            self.notes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.v = v
        self.h = h

    def reduce_note(self, value):
        if value in self.notes:
            self.notes.remove(value)

    def get_pos(self):
        return f'{self.h}:{self.v}'

    def on_border(self, pos):
        return pos if 0 <= pos <= 8 else -1

    def cell_on_left(self):
        return self.on_border(self.h - 1)
    
    def cell_on_right(self):
        return self.on_border(self.h + 1)

    def cell_on_above(self):
        return self.on_border(self.v - 1)

    def cell_on_below(self):
        return self.on_border(self.v + 1)


class Matrix:
    cells = []
    mtx = {}

    def __init__(self):
        pass

    def add(self, cell):
        self.mtx[cell.get_pos()] = cell
        if cell.value != 0:
            self.cells.append(cell)

    def get(self, v, h):
        return self.mtx[f'{v}:{h}']

    def reduce_note_horizontal(self, cell):
        if cell.value != 0:
            for h in range(0, 9):
                self.get(cell.v, h).reduce_note(cell.value)

    def reduce_note_vertical(self, cell):
        if cell.value != 0:
            for v in range(0, 9):
                self.get(v, cell.h).reduce_note(cell.value)

    def reduce_note_square(self, cell):
        if cell.value != 0:
            pass

    def print(self):
        for v in range(0, 9):
            for h in range(0, 9):
                print(color(v, h, self.get(v, h).value), end='')
            print()


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
