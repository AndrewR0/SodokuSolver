import unittest
import mock
from Solver import Solver

class TestSolver(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.correct_board = [[1,2,3,4,5,6,7,8,9],
    #                         [7,8,9,1,2,3,4,5,6],
    #                         [4,5,6,7,8,9,1,2,3],
    #                         [3,1,2,8,4,5,9,6,7],
    #                         [6,9,7,3,1,2,8,4,5],
    #                         [8,4,5,6,9,7,3,1,2],
    #                         [2,3,1,5,7,4,6,9,8],
    #                         [9,6,8,2,3,1,5,7,4],
    #                         [5,7,4,9,6,8,2,3,1]]
        

        
    #     self.wrong_board = [[1,2,3,4,5,6,7,8,9],
    #                         [2,3,4,5,6,7,8,9,1],
    #                         [3,4,5,6,7,8,9,1,2],
    #                         [4,5,6,7,8,9,1,2,3],
    #                         [5,6,7,8,9,1,2,3,4],
    #                         [6,7,8,9,1,2,3,4,5],
    #                         [7,8,9,1,2,3,4,5,6],
    #                         [8,9,1,2,3,4,5,6,7],
    #                         [9,1,2,3,4,5,6,7,8]]
    
    def test_initializing_square_board(self):
        
        board = [[1,1], [2,2]]
        solver = Solver(board)

        return self.assertEqual(solver.board_height, 2)

    def test_initializing_asymmetrical_board(self):
        
        board = [[1,1], [2]]
        solver = Solver(board)

        return self.assertRaises(ValueError)

    def test_valid_row(self):
        ...

    def test_valid_column(self):
        ...
    
    def test_valid_box(self):
        ...

    def test_get_xy_bounds(self):
        ...

    def test_valid_placement(self):
        ...

    def test_solve(self):
        ...

if __name__ == '__main__':
    unittest.main()