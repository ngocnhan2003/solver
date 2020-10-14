
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
    lock = False
    found = False
    v = 0
    h = 0

    def __init__(self, v, h, value):
        self.value = value
        if value != 0:
            self.lock = True
        else:
            self.notes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.v = v
        self.h = h

    def reduce_note(self, note):
        if note in self.notes:
            self.notes.remove(note)
        if len(self.notes) == 1:
            self.value = self.notes[0]
            self.found = True
        return self

    def __str__(self):
        return f'{self.get_pos()}:{self.value}'

    def get_pos(self):
        return f'{self.v}:{self.h}'


class Matrix:
    cells = []
    mtx = {}

    def __init__(self):
        pass

    def add(self, cell):
        self.mtx[cell.get_pos()] = cell
        if cell.value != 0 and cell not in self.cells:
            self.cells.append(cell)

    def get(self, v, h):
        return self.mtx[f'{v}:{h}']

    def reduce_notes(self):
        for cell in self.cells:
            if len(self.cells) <= 81:
                self.reduce_note_horizontal(cell)
                self.reduce_note_vertical(cell)
                self.reduce_note_square(cell)

    def reduce_note_horizontal(self, cell):
        for h in range(0, 9):
            self.add(self.get(cell.v, h).reduce_note(cell.value))

    def reduce_note_vertical(self, cell):
        for v in range(0, 9):
            self.add(self.get(v, cell.h).reduce_note(cell.value))

    def reduce_note_square(self, cell):
        vi = int(cell.v / 3) * 3
        hi = int(cell.h / 3) * 3
        for v in range(0, 3):
            for h in range(0, 3):
                self.add(self.get(vi + v, hi + h).reduce_note(cell.value))

    def print(self):
        for v in range(0, 9):
            for h in range(0, 9):
                print(color(v, h, self.get(v, h).value), end='')
            print()

    def print_notes(self):
        for v in range(0, 9):
            for h in range(0, 9):
                print(self.get(v, h).notes, end='\t')
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


matrix = load_from_file('sudoku.m.input')
matrix.print()
# matrix.print_notes()
matrix.reduce_notes()
print()
# matrix.print_notes()
matrix.print()
