'''
Created on 31 Mar 2019

@author: Matan Davidian
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
    def layMinecicl(self,y,x):
        if self.field[y][x]=="+":
            self.field[y][x]=1
        elif type(self.field[y][x]) is int:
            self.field[y][x]+=1
    def layMine(self,column,row):
        if self.field[row][column]!="*":
            self.mineNum+=1
            self.field[row][column]="*"
            #update value North
            if row>0:
                self.layMinecicl(row-1,column)
            #update value North West
            if column>0 and row>0:
                self.layMinecicl(row-1,column-1)
            #update value West
            if column>0:
                self.layMinecicl(row,column-1)
            #update value south west
            if column>0 and self.rows-1>row:
                self.layMinecicl(row-1,column-1)
            #update value south
            if self.rows-1>row:
                self.layMinecicl(row+1,column)
            #update value south east
            if self.rows-1>row and self.columns-1>column:
                self.layMinecicl(row+1,column+1)
            #update value east
            if self.columns-1>column:
                self.layMinecicl(row,column+1)
            #update value north east
            if row>0 and self.columns-1>column:
                self.layMinecicl(row-1,column+1)
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
    def revalcellscircl(self,q,y,x):
        if self.field[y][x]=="+":
            self.exposed[y][x]="1"
            self.exlore+=1
            q.put((y))
            q.put(x)
        else:
            self.exposed[y][x]="1"
            self.exlore+=1
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
                self.revalcellscircl(q,r-1,c)
            #update value West
            if c>0 and self.exposed[r][c-1]!="1":
                self.revalcellscircl(q,r,c-1)
            #update value south
            if self.rows-1>r and self.exposed[r+1][c]!="1":
                self.revalcellscircl(q,r+1,c)
            #update value east
            if self.columns-1>c and self.exposed[r][c+1]!="1":
                self.revalcellscircl(q,r,c+1)
# game setup
game = Minesweeper()
game.createFeild(3,8)
game.layMine(1, 1)
game.layMine(0, 2)

# game play
game.printField();
". . . . . . . . "
". . . . . . . . "
". . . . . . . . "


game.play(0, 4)
game.printField();
". . 1 + + + + + "
". . 1 + + + + + "
". . 1 + + + + + "

game.play(0, 0)
game.printField();
"1 . 1 + + + + + "
". . 1 + + + + + "
". . 1 + + + + + "

game.play(1, 0)
game.printField();
"1 . 1 + + + + + "
"2 . 1 + + + + + "
". . 1 + + + + + "

game.play(0, 1)
game.printField();
"1 1 1 + + + + + "
"2 . 1 + + + + + "
". . 1 + + + + + "

game.play(2, 1)
game.printField();
"1 1 1 + + + + + "
"2 * 1 + + + + + "
"* 2 1 + + + + + "

game.status();
"WIM"
