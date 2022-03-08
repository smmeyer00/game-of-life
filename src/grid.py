import pygame 

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols 
        self.grid = [[0 for i in range(cols)] for i in range(rows)]


    def clear(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = 0


    # spawns cell at row, col
    def fill_cell(self, row, col):
        self.grid[row][col] = 1


    # 'kills' cell at row, col
    def delete_cell(self, row, col):
        self.grid[row][col] = 0 


    # returns neighbor count of cell at row, col
    def neighbor_count(self, row, col):
        offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        n = 0
        for o in offsets:
            r = row + o[0]
            c = col + o[1]
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 1:
                n+=1

        return n 


    # step to next state of game of life
    def step(self):
        new_grid = [[0 for i in range(self.cols)] for i in range(self.rows)] 
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 1: # alive
                    n = self.neighbor_count(row, col)
                    if n == 2 or n == 3:
                        # cell survives
                        new_grid[row][col] = 1
                    else:
                        # cell dies
                        new_grid[row][col] = 0 
                else: # dead
                    n = self.neighbor_count(row, col)
                    if n == 3:
                        # new cell spawns
                        new_grid[row][col] = 1
                    else:
                        # cell stays dead
                        new_grid[row][col] = 0

        self.grid = new_grid

    
    # draw current grid to screen at (x, y) with provided size
    def draw(self, screen, x, y, width, height, border_color, alive_color, dead_color):
        block_width = width//len(self.grid[0])
        block_height = height//len(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                outer_rect = pygame.Rect(j*block_width+x, i*block_height+y, block_width, block_height)
                inner_rect = pygame.Rect(j*block_width + 1 + x, i*block_height + 1 + y, block_width-2, block_height-2)
                pygame.draw.rect(screen, border_color, outer_rect)
                pygame.draw.rect(screen, alive_color if self.grid[i][j]==1 else dead_color, inner_rect)


    # prints grid to console
    def print_grid(self):
        for row in self.grid:
            for col in row:
                print(col, end=' ')
            print()
        print()