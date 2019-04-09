'''
Created on 31 Mar 2019

@author: matan
'''
import unittest
from minesweeper import Minesweeper
import io
import sys
class TestMinesweeper(unittest.TestCase):
    def testCreateNewClass(self):
        M1=Minesweeper()
        expectedresult=0;
        result=M1.mineNum
        self.assertEqual(result, expectedresult, "a field didn't created well, mineNum should be 0")
    def testCreateFieldValueTopLeft(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        expect="+"
        result=F1.field[0][0]
        self.assertEqual(expect, result, "a field didn't created well, Value at Top Left should be +")
    def testCreateFieldValueTopRight(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        expect="+"
        result=F1.field[0][3]
        self.assertEqual(expect, result, "a field didn't created well, Value at Top Right should be +")
    def testCreateFieldValueBottomLeft(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        expect="+"
        result=F1.field[3][0]
        self.assertEqual(expect, result, "a field didn't created well, Value at Bottom Left should be +")
    def testCreateFieldValueBottomRight(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        expect="+"
        result=F1.field[3][3]
        self.assertEqual(expect, result, "a field didn't created well, Value at Bottom Left should be +")
    def testCreateFieldRandomValue(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        expect="+"
        result=F1.field[2][2]
        self.assertEqual(expect, result, "a field didn't created well,all field Value should be +")
    def testLayMine(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        F1.layMine(1,1)
        expect="*"
        result=F1.field[1][1]
        self.assertEqual(expect, result, "The mine didn't laid well")
    def testLayMineCircle(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        F1.layMine(1,1)
        expect=1
        result=F1.field[2][2]
        self.assertEqual(expect, result, "The circle around the mine update well")
    def testLayTwoMine(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        F1.layMine(1,1)
        F1.layMine(1,2)
        expect=2
        result=F1.field[2][2]
        self.assertEqual(expect, result, "the circle around the mines update well to 2, with two bombs")
    def testWinSituationPrint(self):
        F1=Minesweeper()
        F1.createFeild(2,2)
        F1.layMine(0,0)
        F1.layMine(1,1)
        F1.play(0,1)
        F1.play(1,0)
        expected="WIN\n"
        
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                     
        F1.status()                                  
        sys.stdout = sys.__stdout__ 
          
        actual=capturedOutput.getvalue()     
        self.assertEqual(expected,actual, "the game status should be Win")
    def testLostSituationPrint(self):
        F1=Minesweeper()
        F1.createFeild(2,2)
        F1.layMine(0,0)
        F1.layMine(1,1)
        F1.play(0,1)
        F1.play(1,1)
        expected="LOST\n"
        
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                     
        F1.status()                                  
        sys.stdout = sys.__stdout__ 
          
        actual=capturedOutput.getvalue()     
        self.assertEqual(expected,actual, "the game status should be LOST")
        
    def testPrintFieldAtStart(self):
        game = Minesweeper()
        game.createFeild(3,3)
        game.layMine(0, 0)
        game.layMine(1, 1)
        expected=". . . \n. . . \n. . . \n"
        
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                     
        game.printField();                                 
        sys.stdout = sys.__stdout__ 
          
        actual=capturedOutput.getvalue()     
        self.assertEqual(expected,actual, "the empty field didn't print well")
    def testPrintFieldAtWin(self):
        game = Minesweeper()
        game.createFeild(3,8)
        game.layMine(1, 1)
        game.layMine(2, 0)
        game.play(0, 4)
        game.play(0, 0)
        game.play(1, 0)
        game.play(0, 1)
        game.play(2, 1)
        expected="1 1 1 + + + + + \n2 * 1 + + + + + \n* 2 1 + + + + + \n"
        "1 1 1 + + + + + "
        "2 * 1 + + + + + "
        "* 2 1 + + + + + "
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                     
        game.printField();                                 
        sys.stdout = sys.__stdout__ 
          
        actual=capturedOutput.getvalue()     
        self.assertEqual(expected,actual, "the full field didn't print well when player win")
    def testPrintFieldAtLOST(self):
        game = Minesweeper()
        game.createFeild(3,3)
        game.layMine(0, 0)
        game.layMine(1, 1)
        game.play(0, 0)
        expected="* . . \n. * . \n. . . \n"
        "* . . "
        ". * . "
        ". . . "
        capturedOutput = io.StringIO()                 
        sys.stdout = capturedOutput                     
        game.printField();                                 
        sys.stdout = sys.__stdout__ 
          
        actual=capturedOutput.getvalue()     
        self.assertEqual(expected,actual, "the full field didn't print well when player lost")
    def testRevealCell1(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        F1.layMine(0, 0)
        expect="1"
        F1.play(2,2)
        result=F1.exposed[1][1]
        self.assertEqual(expect, result, "The cell should be reveal")
    def testRevealCell2(self):
        F1=Minesweeper()
        F1.createFeild(4,4)
        F1.layMine(0, 0)
        F1.layMine(1, 1)
        expect="0"
        F1.play(2,2)
        result=F1.exposed[1][1]
        self.assertEqual(expect, result, "The cell should not be reveal")
if __name__ == '__main__':
    unittest.main()