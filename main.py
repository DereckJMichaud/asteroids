import pygame
from constants import *

def main():
    pygame.init
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running == True :
        screen.fill(pygame.Color(0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygme.quit
                sys.exit()
                running = False

if __name__ == "__main__":
    main()