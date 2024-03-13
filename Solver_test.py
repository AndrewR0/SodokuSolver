import unittest
import mock
from Solver import Solver

class TestSolver(unittest.TestCase):
    
    def test_initializing_square_board(self):
        
        board = [[1,1], [2,2]]
        solver = Solver(board)

        return self.assertEqual(solver.board_height, 2)

    def test_initializing_asymmetrical_board(self):
        
        board = [[1,1], [2]]
        solver = Solver(board)

        return self.assertRaises(ValueError)

    def test_valid_row(self):
         board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,0,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]
         
         solver = Solver(board)

         return self.assertTrue(solver.valid_row(4,1))
    
    def test_invalid_row(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,1,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]
        
        solver = Solver(board)

        return self.assertFalse(solver.valid_row(4,1))

    def test_valid_column(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,0,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertTrue(solver.valid_column(4,1))
    
    def test_invalid_column(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,1,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertFalse(solver.valid_column(4,1))
    
    def test_valid_box(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,0,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertTrue(solver.valid_box(4,4,1))
    
    def test_invalid_box(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,1,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertFalse(solver.valid_box(4,4,1))

    def test_get_xy_bounds(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,1,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertEqual(solver.get_xy_bounds(4,4), ((3,6),(3,6)))

    def test_valid_placement(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,0,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertTrue(solver.valid_placement(4,4,1))
    
    def test_invalid_placement(self):
        board = [[1,2,3,4,5,6,7,8,9],
                [7,8,9,1,2,3,4,5,6],
                [4,5,6,7,8,9,1,2,3],
                [3,1,2,8,4,5,9,6,7],
                [6,9,7,3,1,2,8,4,5],
                [8,4,5,6,9,7,3,1,2],
                [2,3,1,5,7,4,6,9,8],
                [9,6,8,2,3,1,5,7,4],
                [5,7,4,9,6,8,2,3,1]]

        solver = Solver(board)

        return self.assertFalse(solver.valid_placement(4,4,1))

    def test_solve(self):
        ...

if __name__ == '__main__':
    unittest.main()