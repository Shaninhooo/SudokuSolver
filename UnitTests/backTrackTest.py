from sudokusolver import backTrack
import sudokugenerator as sg
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class sudokuBacktrackTest:    
  def runTests(self):
    self.Test1()
            
  def Test1(self):
    map1 = sg.createSudoku()
    map1[1,0] = 0
    map1[1,1] = 0
    backTracked = backTrack(1, 1, map1.copy, map1)
    print("Testing...")
    if sg.checkValid(backTracked) == True:
      print("Passed Test 1")
      print(map1)
    else:
      print("Failed")
      
      
      
    
    
      
      

    
      
      
