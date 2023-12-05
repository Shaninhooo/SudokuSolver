import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import sudokugenerator as sg

class SudokuGenerationTest:    
  def runTests(self):
    self.Test1()
            
        
    
  def Test1(self):
    map1 = sg.createSudoku()
    print("Testing...")
    if sg.checkValid(map1) == True:
      print("Passed Test 1")
      print(map1)
    else:
      print("Failed")
      
      
      
    
    
      
      

    
      
      
