import numpy as np
from board import board

class Solve:
    def __init__(self, board):
        #self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.factor = int(self.rows ** 0.5) #The board can only be made up of perfect squares (just how it be) so this variable is the square root of that value

    #Determines whether the number at the inputted posistion is valid
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
                xSkew = x + r*self.factor
                ySkew = y + c*self.factor
                #print(xSkew, ySkew, board[xSkew][ySkew], pos)
                val = board[xSkew][ySkew] #get the value of each position in the box
                if (xSkew,ySkew) != pos and val != 0 and val == num:
                    return False
                else:
                    continue
        return True

    def solve(self):        
        for i in range(self.rows):
            for j in range(self.cols):
                #Empty cell
                if board[i][j] == 0:
                    for num in range(1,self.rows+1):
                        board[i][j] = num
                        if self.validate(board, (i,j), num):
                            if self.solve():
                                return True
                        board[i][j] = 0
                    return False
        return True
        
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


#Use later to generate a board to any size (as long as the size is a perfect square)
#Need to debug this, not returning correct board layout with printBoard
#Return a 2D matrix
'''
def generateBoard(self, board, size):
    root = size**0.5
    if int(root + 0.5) ** 2 == size:
        board = [[0 for i in range(size)] for j in range(size)]
        return self.printBoard(board)
    return "Size needs to be a perfect square"
'''

if __name__ == '__main__':
    x = Solve(board)
    #print(x.generateBoard(16))
    print(x.printBoard(board))
    #print(x.validate(board, (8,8), 9))
    print(x.solve())
    print(x.printBoard(board))