'''
Created on 31 Mar 2019

@author: matan
'''
class Minesweeper():
    def createField(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.field=[]
        #col=["+"]*columns
        for _ in range(rows):
            self.field.append(["+"]*columns)
    def layMine(self,row,column):
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
        if column>0 and self.rows>row:
            if self.field[row+1][column-1]=="+":
                self.field[row+1][column-1]=1
            elif type(self.field[row+1][column-1]) is int:
                self.field[row+1][column-1]+=1
        #update value south
        if self.rows>row:
            if self.field[row+1][column]=="+":
                self.field[row+1][column]=1
            elif type(self.field[row+1][column]) is int:
                self.field[row+1][column]+=1
        #update value south east
        if self.rows>row and self.columns>column:
            if self.field[row+1][column+1]=="+":
                self.field[row+1][column+1]=1
            elif type(self.field[row+1][column+1]) is int:
                self.field[row+1][column+1]+=1
        #update value east
        if self.columns>column:
            if self.field[row][column+1]=="+":
                self.field[row][column+1]=1
            elif type(self.field[row][column+1]) is int:
                self.field[row][column+1]+=1
        #update value north east
        if row>0 and self.columns>column:
            if self.field[row-1][column+1]=="+":
                self.field[row-1][column+1]=1
            elif type(self.field[row-1][column+1]) is int:
                self.field[row-1][column+1]+=1
    def play(self,row,column):
        pass
    def status(self):
        pass
    def prinfField(self):
        pass
m1=Minesweeper()
m1.createField(4, 5)
m1.layMine(0, 0)
m1.layMine(3, 4)
m1.layMine(0, 4)
m1.layMine(3, 0)
