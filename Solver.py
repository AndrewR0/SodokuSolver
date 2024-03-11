
class Solver:
    def __init__(self, board: list):
        self.board = board
        self.board_height = len(self.board)
        self.board_width = len(self.board[0])

        #TODO: Write better check to make sure board is square. Right now it's only checking that the first row is same as height. Other rows might be different size
        if self.board_height != self.board_width:
            print(f"Board shape is not square!")
            for row in self.board:
                print(row)
            raise ValueError
    
    def valid_row(self, y_coord: int) -> bool:
        ...

    def valid_column(self, x_coord: int) -> bool:
        ...

    def valid_box(self, x_coord: int, y_coord: int) -> bool:
        ...

    def valid_placement(self, x_coord: int, y_coord: int) -> bool:
        '''Function to call the above valid functions at once'''
        ...

    def solve(self) -> list:
        print("Solving...")
    

if __name__ == "__main__":
    # board = [[]]
    # Solver(board).solve()
    ...    