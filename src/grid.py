import pygame 

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols 
        self.grid = [[0 for i in range(cols)] for i in range(rows)]


    # spawns cell at row, col
    def fill_cell(self, row, col):
        self.grid[row][col] = 1


    # 'kills' cell at row, col
    def delete_cell(self, row, col):
        self.grid[row][col] = 0 


    # step to next state of game of life
    def step(self):
        pass 

    
    # draw current grid to screen at (x, y) with provided size
    def draw(self, screen, x, y, width, border_color, alive_color, dead_color):
        block_size = width//len(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                outer_rect = pygame.Rect(i*block_size+x, j*block_size+y, block_size, block_size)
                inner_rect = pygame.Rect(i*block_size + 1 + x, j*block_size + 1 + y, block_size-2, block_size-2)
                pygame.draw.rect(screen, border_color, outer_rect)
                pygame.draw.rect(screen, alive_color if self.grid[i][j]==1 else dead_color, inner_rect)


    # prints grid to console
    def print_grid(self):
        for row in self.grid:
            for col in row:
                print(col, end=' ')
            print()
        print()