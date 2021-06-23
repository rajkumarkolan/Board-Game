import numpy as np
import copy

class board_game:
    
    """
    This class defines the game board with the chosen grid size and color
    """
    def __init__(self, num_tiles,num_colors):
        
        self.num_colors = num_colors
        self.n = num_tiles
        self.color_space = np.arange(num_colors) # Colours are mapped to numbers for easier handling
        np.random.seed(1)
        self.grid = np.random.choice(a=self.color_space, size=(self.n,self.n)) # define the board
        self.temp_grid = copy.deepcopy(self.grid)
        self.pos = (0,0) # initial position
        self.count = 0

    def initialize_temp(self):
        """
        Support fuction to reset the counting process
        """
        self.count = 0
        self.temp_grid = copy.deepcopy(self.grid)
    
    def flooding_count(self, curr_pos, fill_color, old_color):
        """
        This function counts the number of tiles to be colored with the chosen color
        """
        if self.temp_grid[curr_pos] == fill_color or self.temp_grid[curr_pos] == old_color:
            self.temp_grid[curr_pos] = self.num_colors
            self.count = self.count + 1
        
            if curr_pos[0] > 0:
                self.flooding_count((curr_pos[0]-1,curr_pos[1]),fill_color, old_color)
            if curr_pos[0] < self.temp_grid.shape[1] - 1:
                self.flooding_count((curr_pos[0]+1,curr_pos[1]),fill_color, old_color)

            if curr_pos[1] > 0:
                self.flooding_count((curr_pos[0],curr_pos[1]-1),fill_color, old_color)
            if curr_pos[1] < self.temp_grid.shape[0] - 1:
                self.flooding_count((curr_pos[0],curr_pos[1]+1),fill_color, old_color)

    def flooding_fill(self, curr_pos = (0,0), fill_color=0, old_color=0):
        """
        This function colors the tiles with the chosen color
        """
        if self.grid[curr_pos] == old_color:
            self.grid[curr_pos] = fill_color
        
            if curr_pos[0] > 0:
                self.flooding_fill((curr_pos[0]-1,curr_pos[1]),fill_color, old_color)
            if curr_pos[0] < self.temp_grid.shape[1] - 1:
                self.flooding_fill((curr_pos[0]+1,curr_pos[1]),fill_color, old_color)
            if curr_pos[1] > 0:
                self.flooding_fill((curr_pos[0],curr_pos[1]-1),fill_color, old_color)
            if curr_pos[1] < self.temp_grid.shape[0] - 1:
                self.flooding_fill((curr_pos[0],curr_pos[1]+1),fill_color, old_color)



class player_automate:

    """
    This class defines the possible movements of the player
    """
    def __init__(self,board):
        self.board = board
        self.move_list = []

    
    def decide_best_move(self):
        """
        This function chooses the best posible color for the next step by brute forcing each color
        """
        self.counts_list = []
        for color in range(self.board.num_colors):
            self.board.initialize_temp()
            self.board.flooding_count(self.board.pos,color, self.board.grid[self.board.pos])
            self.counts_list.append(self.board.count)

        return np.argmax(self.counts_list)

    def make_move(self, color):
        """
        This function makes the move with the chosen color
        """
        self.move_list.append(color)
        self.board.flooding_fill(fill_color=color, old_color=self.board.grid[self.board.pos])

    def board_complete(self):
        """
        This function checks whether the game is done or not
        """
        OneDBoard = np.ravel(self.board.grid)
        print(OneDBoard)
        result = np.all(OneDBoard==OneDBoard[0])


        return result
        



if __name__ == '__main__':

    board = board_game(6,3)
    player = player_automate(board)

    # Loop untill the board game is done
    while(player.board_complete() == False):
        best_color = player.decide_best_move()
        player.make_move(best_color)
    
    print('color choise: ', player.move_list)