import pygame
from grid import Grid 

pygame.init()

# globals 
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)

black = 0, 0, 0
white = 233, 238, 247
grey = 90, 93, 97

grid = Grid(100, 100)



def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill(grey)
        grid.draw(screen, 0, 0, 1000, grey, black, white)
        pygame.display.flip() 


if __name__ == "__main__":
    run()
    