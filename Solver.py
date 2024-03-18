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
        try:
            self.board = np.array(board)
        except ValueError:
            for _ in board:
                print(_)
            print("Board shape is not square!")
            return
        self.board_height = len(self.board)
        self.board_width = len(self.board[0])

        self.bounding_box_len = int(math.sqrt(self.board_height))

        # Preprocessing submatrix bounds
        self.bounding_limits = []
        current_index = 0
        for _ in range(self.bounding_box_len):
            start = current_index
            stop = start + self.bounding_box_len
            current_index = stop
            self.bounding_limits.append((start, stop)) # Note: The range is exclusive -> 0,3 does not include 3

    def valid_row(self, y_coord: int, possible_num: int) -> bool:
        if possible_num in self.board[y_coord,:]:
            return False
        return True

    def valid_column(self, x_coord: int, possible_num: int) -> bool:
        if possible_num in self.board[:, x_coord]:
            return False
        return True

    def valid_box(self, x_coord: int, y_coord: int, possible_num: int) -> bool:
        x_bound, y_bound = self.get_xy_bounds(x_coord, y_coord)

        flattened = self.board[y_bound[0]:y_bound[1], x_bound[0]:x_bound[1]].flatten()

        if possible_num in flattened:
            return False
        return True

    def get_xy_bounds(self, x_coord: int, y_coord: int) -> tuple:
        x_bound = None
        y_bound = None
        for bounds in self.bounding_limits:
            if bounds[0] <= x_coord <= bounds[1]:
                x_bound = bounds
            if bounds[0] <= y_coord <= bounds[1]:
                y_bound = bounds

        return (x_bound, y_bound)

    def valid_placement(self, x_coord: int, y_coord: int, possible_num: int) -> bool:
        if self.valid_row(y_coord, possible_num) and self.valid_column(x_coord, possible_num) and self.valid_box(x_coord, y_coord, possible_num):
            return True
        return False

    def solve(self) -> list:
        print("Solving...")
    

if __name__ == "__main__":
    # board = BOARD
    # Solver(board).solve()
    ...