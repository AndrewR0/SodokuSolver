board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1],
         [0,0,0,5,0,6,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,2,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

def printBoard(board):
    output = ""
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            if (j+1) % 3 == 0 and j != 0:
                output += str(board[i][j]) + "|"
            else:
                output += str(board[i][j]) + " "
        output += "\n"
        
        if (i+1) % 3 == 0 and i != 0 and i != rows-1:
            output += "- - - - - - - - -\n"
    return output
                
if __name__ == '__main__':
    print(printBoard(board))