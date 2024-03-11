import numpy as np
import math

BOARD = [[1,2,3,4,5,6,7,8,9],
         [2,3,4,5,6,7,8,9,1],
         [3,4,5,6,7,8,9,1,2],
         [4,5,6,7,8,9,1,2,3],
         [5,6,7,8,9,1,2,3,4],
         [6,7,8,9,1,2,3,4,5],
         [7,8,9,1,2,3,4,5,6],
         [8,9,1,2,3,4,5,6,7],
         [9,1,2,3,4,5,6,7,8]]

class Solver:
    def __init__(self, board: list):
        self.board = np.array(board)
        # print(self.board[:,5])
        self.board_height = len(self.board)

        if not all(len(row) == self.board_height for row in self.board):
            for _ in self.board:
                print(_)
            raise ValueError("Board shape is not square!")

        self.board_width = len(self.board[0])

        #TODO: There probably needs to be a check somewhere to make sure the size of the board is actually square
        self.bounding_box_len = int(math.sqrt(self.board_height))

        # Preprocessing submatrices
        self.bounding_limits = []
        current_index = 0
        for _ in range(self.bounding_box_len):
            start = current_index
            stop = start + self.bounding_box_len - 1
            current_index = stop + 1
            self.bounding_limits.append((start, stop))
        
        print(self.bounding_limits)

    def valid_row(self, y_coord: int, possible_num: int) -> bool:
        if possible_num in self.board[y_coord,:]:
            return False
        return True

    def valid_column(self, x_coord: int, possible_num: int) -> bool:
        if possible_num in self.board[:, x_coord]:
            return False
        return True

    def valid_box(self, x_coord: int, y_coord: int, possible_num: int) -> bool:
        ...

    def valid_placement(self, x_coord: int, y_coord: int, possible_num: int) -> bool:
        '''Function to call the above valid functions at once'''
        ...

    def solve(self) -> list:
        print("Solving...")
    

if __name__ == "__main__":
    board = BOARD
    Solver(board).solve()
    # ...