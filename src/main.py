import pygame
import time
from grid import Grid 

pygame.init()
pygame.display.set_caption("Steven's Game of Life")

# globals 
size = width, height = 1200, 700
screen = pygame.display.set_mode(size)

black = 0, 0, 0
white = 233, 238, 247
grey = 90, 93, 97

grid = Grid(height//10, width//10)
grid.fill_cell(10, 10)
grid.fill_cell(10, 11)
grid.fill_cell(10, 12)



def run():
    t1 = time.perf_counter()
    started = False 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:    
                    started = not started  
                if event.key == pygame.K_ESCAPE:
                    grid.clear()
                    started = False

        if pygame.mouse.get_pressed()[0] and not started:
            # fill cells 
            pos = pygame.mouse.get_pos()
            col = pos[0] // 10
            row = pos[1] // 10
            grid.fill_cell(row, col)

        if pygame.mouse.get_pressed()[2] and not started:
            # erase cells
            pos = pygame.mouse.get_pos()
            col = pos[0] // 10
            row = pos[1] // 10
            grid.delete_cell(row, col)


        screen.fill(grey)

        # only step every .1 seconds
        if (time.perf_counter() - t1 > 0.2) and started:
            grid.step()
            t1 = time.perf_counter()

        grid.draw(screen, 0, 0, 1200, 700, grey, black, white)
        pygame.display.flip() 



if __name__ == "__main__":
    run()
    