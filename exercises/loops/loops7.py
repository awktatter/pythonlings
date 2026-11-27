# Exercise: Loops 7
# I AM DONE
#
# Use nested `for` loops to build a multiplication table as a list of lists.
# `table[i][j]` should equal `(i + 1) * (j + 1)` for i, j in 0..2.
# The result should be:
#   [[1, 2, 3],
#    [2, 4, 6],
#    [3, 6, 9]]
# Build `table` row by row; for each row build `row` element by element.

table = []
# write your nested for loops here
for i in range(0, 3):
    row = list()
    for j in range(0, 3):
        row.append((i + 1) * (j + 1))
    table.append(row)