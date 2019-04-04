'''
Created on 31 Mar 2019

@author: matan
'''
import unittest
import minesweeper

class TestMinesweeper(unittest.TestCase):
    def createField_test(self):
        F1=minesweeper()
        F1.createField(1,1)
        self.assertNotEqual(F1.field[1], "+", "a field didn't created")
      
if __name__ == '__main__':
    unittest.main()