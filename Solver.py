import numpy as np
from board import board
import math

class Solve:
    def __init__(self, board):
        #self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.factor = int(self.rows ** 0.5) #

    def validate(self, board, pos, num):
        
        T = np.array(board) #numpy makes matrices easier :)

        tempRow = T[pos[0]] #extract row from matrix
        tempCol = T[:,pos[1]] #extract col from matrix

        #------rows/cols------
        #0's represent empty positions on the board
        #Consider only the values that are not 0's
        row = [i for i in tempRow if i != 0] 
        col = [j for j in tempCol if j != 0]

        #if there are multiple instances of a single number in a row or col, then this will catch the invalid placement
        if len(set(row)) != len(row) or len(set(col)) != len(col):
            return False
        
        #------box------
        #temp values for the row and col of the n^1/2 x n^1/2 positions. In a 9x9 board, these will be the 3x3 box positions the value that
        # is being check resides
        r = int(pos[0] / self.factor)
        c = int(pos[1] / self.factor)

        #iterate through the box
        for x in range(self.factor):
            for y in range(self.factor):
                val = board[x + r*3][y + c*3] #get the value of each position in the box
                if val != 0 and val == num:
                    return False
                else:
                    continue

    def solve(self, board):
        pass
    
    def printBoard(self, board): #done for a 9x9, maybe change later for make for nxn (check if the n's are perfect squares)
        output = ""
        for i in range(self.rows):
            for j in range(self.cols):
                if (j+1) % 3 == 0 and j != 0 and j != self.cols-1:
                    output += str(board[i][j]) + "|"
                else:
                    output += str(board[i][j]) + " "
            output += "\n"
            
            if (i+1) % 3 == 0 and i != 0 and i != self.rows-1:
                output += "- - - - - - - - -\n"
        return output

if __name__ == '__main__':
    x = Solve(board)
    print(x.printBoard(board))
    print(x.validate(board, (8,8), 9))