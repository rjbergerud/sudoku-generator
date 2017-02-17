import sys
from Sudoku.Generator import *

# setting difficulties and their cutoffs for each solve method
difficulties = {
    'easy': (35, 0),
    'medium': (81, 5),
    'hard': (81, 10),
    'extreme': (81, 15)
}

difficulty = difficulties['medium']

# constructing generator object from puzzle file (space delimited columns, line delimited rows)
gen = Generator("base.txt")
gen.randomize(100)
print("{0}\r\n".format(gen.board))

# Create puzzle such that each cell has only one
# possible entry given row, col, block
gen.reduce_via_logical(difficulty[0])
print("{0}\r\n".format(gen.board))

# Take out more cells but keep unique solution
gen.reduce_via_random(difficulty[1])
print(gen.board)
