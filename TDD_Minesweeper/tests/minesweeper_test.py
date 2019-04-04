'''
Created on 31 Mar 2019

@author: matan
'''
import unittest
from TDD_Minesweeper.game import minesweeper
class TestMinesweeper(unittest.TestCase):
    def testcreateField_test(self):
        F1=minesweeper()
        F1.createField(1,1)
        result="+"
        expect=F1.field[1]
        self.assertEqual(expect, result, "a field didn't created")
    def testcreateClass(self):
        M1=minesweeper()
        self.assertEqual(M1.mineNum, 0, "a field didn't created")

if __name__ == '__main__':
    unittest.main()