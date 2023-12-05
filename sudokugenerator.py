import numpy as np
import random

#Blocks, rows and columns must sum up to 45
#No Same numbers in each rows, blocks and columns

def findBlock(x, y, map):
    row_start = (y // 3) * 3
    col_start = (x // 3) * 3
    return map[row_start:row_start+3, col_start:col_start+3]
    
def generateNum(x, y, map):
  randNum = random.randint(1, 9)
  block = findBlock(x, y, map) 
  column = map[:, x]
  row = map[y, :]

      
  while randNum in block or randNum in column or randNum in row:
    randNum = random.randint(1, 9)
  return randNum

def checkValid(map):
  for row in range(9):
    for col in range(9):
      num = map[row, col]
          # Check row
      if num > 0 and map[row, :].tolist().count(num) > 1:
              print(map)
              print(map[row, col])
              print(row, col)
              return False

          # Check column
      if num > 0 and map[:, col].tolist().count(num) > 1:
              print(map)
              print(map[row, col])
              print(row, col)
              return False

          # Check block
      block = findBlock(col, row, map)
      if num > 0 and block.flatten().tolist().count(num) > 1:
              print(map)
              print(map[row, col])
              print(row, col)
              return False
  return True

def createSudoku():
  map = np.zeros((9,9), dtype=int)
  for _ in range(25):   
    x = random.randint(0, 8)
    y = random.randint(0, 8)
      
    while map[y, x] != 0:
      x = random.randint(0, 8)
      y = random.randint(0, 8)
    num = generateNum(x, y, map)
    map[y, x] = num
  while checkValid(map) == False:
    map = createSudoku()
  return map  
  
