import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import sudokugenerator as sg

class BlockFinderTest:    
  def runTests(self):
    self.Test1()
            
        
    
  def Test1(self):
    map1 = sg.createSudoku()
    block = sg.findBlock(4, 2, map1)
    realBlock = map1[0:3,3:6]
    print(map1)
    print(block)
    print(realBlock)
    print("Testing...")
    # if sg.checkValid(map1) == True:
    #   print("Passed Test 1")
    #   print(map1)
    # else:
    #   print("Failed")
      
      
      
    
    