from sudokugenerator import createSudoku
from sudokusolver import solve

map = createSudoku()
print(map)
solve(map)