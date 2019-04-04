'''
Created on 31 Mar 2019

@author: matan
'''
from enum import Enum
from queue import Queue

class GameStatus(Enum):
    WIN =0
    LOST=1
    PLAYING=2
class Minesweeper():
    def __init__(self):
        self.mineNum=0
        self.exlore=0
    def createFeild(self,rows,columns):
        self.stat=GameStatus.PLAYING
        self.rows=rows
        self.columns=columns
        self.field=[]
        self.exposed=[]
        for _ in range(rows):
            self.field.append(["+"]*columns)
            self.exposed.append(["0"]*columns)
    def layMine(self,column,row):
        if self.field[row][column]!="*":
            self.mineNum+=1
            self.field[row][column]="*"
            #update value North
            if row>0:
                if self.field[row-1][column]=="+":
                    self.field[row-1][column]=1
                elif type(self.field[row-1][column]) is int:
                    self.field[row-1][column]+=1
            #update value North West
            if column>0 and row>0:
                if self.field[row-1][column-1]=="+":
                    self.field[row-1][column-1]=1
                elif type(self.field[row-1][column-1]) is int:
                    self.field[row-1][column-1]+=1
            #update value West
            if column>0:
                if self.field[row][column-1]=="+":
                    self.field[row][column-1]=1
                elif type(self.field[row][column-1]) is int:
                    self.field[row][column-1]+=1
            #update value south west
            if column>0 and self.rows-1>row:
                if self.field[row+1][column-1]=="+":
                    self.field[row+1][column-1]=1
                elif type(self.field[row+1][column-1]) is int:
                    self.field[row+1][column-1]+=1
            #update value south
            if self.rows-1>row:
                if self.field[row+1][column]=="+":
                    self.field[row+1][column]=1
                elif type(self.field[row+1][column]) is int:
                    self.field[row+1][column]+=1
            #update value south east
            if self.rows-1>row and self.columns-1>column:
                if self.field[row+1][column+1]=="+":
                    self.field[row+1][column+1]=1
                elif type(self.field[row+1][column+1]) is int:
                    self.field[row+1][column+1]+=1
            #update value east
            if self.columns-1>column:
                if self.field[row][column+1]=="+":
                    self.field[row][column+1]=1
                elif type(self.field[row][column+1]) is int:
                    self.field[row][column+1]+=1
            #update value north east
            if row>0 and self.columns-1>column:
                if self.field[row-1][column+1]=="+":
                    self.field[row-1][column+1]=1
                elif type(self.field[row-1][column+1]) is int:
                    self.field[row-1][column+1]+=1
    def play(self,row,column):
        if self.stat==GameStatus.PLAYING:
            if self.field[row][column]=="*":
                self.stat=GameStatus.LOST
                for r in range(self.rows):
                    for c in range(self.columns):
                        if self.field[r][c]=="*":
                            self.exposed[r][c]="1"
            elif self.field[row][column]=="+":
                self.revalcells(row,column)
            else:
                self.exposed[row][column]="1"
                self.exlore+=1
            if self.exlore==self.rows*self.columns-self.mineNum:
                self.stat=GameStatus.WIN
                for r in range(self.rows):
                    for c in range(self.columns):
                        self.exposed[r][c]="1"
    def status(self):
        print( self.stat)
    def printField(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.exposed[r][c]=="0":
                    print(". ", end="")
                elif self.exposed[r][c]=="1":
                    print("{} ".format(self.field[r][c]), end="")
            print()
        print()
    def revalcells(self,row,column):
        q = Queue()
        self.exposed[row][column]="1"
        self.exlore+=1
        q.put(row)
        q.put(column)
        while not q.empty():
            r=q.get()
            c=q.get()
            #update value North
            if r>0 and self.exposed[r-1][c]!="1":
                if self.field[r-1][c]=="+":
                    self.exposed[r-1][c]="1"
                    self.exlore+=1
                    q.put((r-1))
                    q.put(c)
                else:
                    self.exposed[r-1][c]="1"
                    self.exlore+=1
            #update value West
            if c>0 and self.exposed[r][c-1]!="1":
                if self.field[r][c-1]=="+":
                    self.exposed[r][c-1]="1"
                    self.exlore+=1
                    q.put(r)
                    q.put(c-1)
                else:
                    self.exposed[r][c-1]="1"
                    self.exlore+=1
            #update value south
            if self.rows-1>r and self.exposed[r+1][c]!="1":
                if self.field[r+1][c]=="+":
                    self.exposed[r+1][c]="1"
                    self.exlore+=1
                    q.put(r+1)
                    q.put(c)
                else:
                    self.exposed[r+1][c]+="1"
                    self.exlore+=1
            #update value east
            if self.columns-1>c and self.exposed[r][c+1]!="1":
                if self.field[r][c+1]=="+":
                    self.exposed[r][c+1]="1"
                    self.exlore+=1
                    q.put(r)
                    q.put(c+1)
                else:
                    self.exposed[r][c+1]="1"
                    self.exlore+=1
            
# game setup
game = Minesweeper()
game.createFeild(3,3)
game.layMine(0, 0)
game.layMine(1, 1)

# game play
game.printField();
". . ."
". . ."
". . ."

game.status();
"PLAYING"

game.play(0, 0)
game.printField();
"* . ."
". * ."
". . ."

game.status();
"LOST"