import unittest
import numpy as np
from game import board_game
from game import player_automate


class TestBoardMethods(unittest.TestCase):

    def setUp(self):
        self.n = 6
        self.m = 3

    def test_grid_size(self):
        board = board_game(num_tiles=self.n, num_colors=self.m)
        self.assertEqual(board.grid.shape, (self.n,self.n), 'Error in the initialized board size')

    def test_flooding_count(self):
        board = board_game(num_tiles=self.n, num_colors=self.m)
        board.grid = np.zeros((self.n,self.n))
        board.initialize_temp()
        board.flooding_count((0,0),1,0)
        self.assertEqual(board.count, self.n*self.n, 'Flooding count algorithm is not flooing correctly or counting correctly')

    def test_flooding_fill(self):
        board = board_game(num_tiles=self.n, num_colors=self.m)
        board.grid = np.zeros((self.n,self.n))
        board.flooding_fill((0,0),1,0)
        self.assertEqual(np.ravel(board.grid).all(),1, 'Flooding fill algorithm is not flooing correctly ')


class TestPlayerMethods(unittest.TestCase):

    def setUp(self):
        self.n = 6
        self.m = 3
    
    def test_decide_best_move(self):
        board = board_game(num_tiles=self.n, num_colors=self.m)
        board.grid = np.ones((self.n,self.n)) * 2
        board.grid[(0,0)] = 1
        player = player_automate(board)
        move = player.decide_best_move()
        self.assertEqual(move,2, 'player is not deciding the best move for the given board')

    def test_make_move(self):
        board = board_game(num_tiles=self.n, num_colors=self.m)
        board.grid = np.ones((self.n,self.n)) * 2
        board.grid[(0,0)] = 1
        player = player_automate(board)
        move = player.decide_best_move()
        player.make_move(move)
        self.assertEqual(len(player.move_list),1, 'player is not keeping track of the moves made')
        isEq = np.array_equal(player.board.grid, np.ones((self.n, self.n))*2 )
        self.assertTrue(isEq,'player is not updating the board after the move')
    
    def test_board_complete(self):
        
        board = board_game(num_tiles=self.n, num_colors=self.m)
        board.grid = np.ones((self.n,self.n)) * 2
        board.grid[(0,0)] = 1
        player = player_automate(board)
        move = player.decide_best_move()
        player.make_move(move)
        isComp = player.board_complete()
        self.assertTrue(isComp,'player is not detecting that the game is complete')



if __name__ == '__main__':
    unittest.main()