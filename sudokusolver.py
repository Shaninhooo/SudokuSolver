import numpy as np
import sudokugenerator as sg

def is_valid(num, col, row, map):
      # Check row
  if map[row, :].tolist().count(num) > 0:
    return False

      # Check column
  if map[:, col].tolist().count(num) > 0:
    return False

      # Check block
  block = sg.findBlock(col, row, map)
  if block.flatten().tolist().count(num) > 0:
    return False
  return True

def findEmptylocation(x, y, map):
  coordinates = [0, 0]
  for row in range(y, 9):
    for col in range(x, 9):
        if map[row, col] == 0:
          coordinates[0] = row
          coordinates[1] = col
          return coordinates
  return False
          

def solve(map):
  x = 0
  y = 0
  
  if findEmptylocation(x, y, map) is False:
      print("Solution Found:")
      print(map)
      return True

  emptyCoordinates = findEmptylocation(x, y, map)
  y = emptyCoordinates[0]
  x = emptyCoordinates[1]

  for num in range(1, 10):
    if is_valid(num, x, y, map):
        map[y, x] = num

        if solve(map):
          return True

        map[y, x] = 0
  return False






  