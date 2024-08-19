import pygame
from constants import *

def main():
    pygame.init
    class pygame.time.Clock :
        def __init__(self, dt):
            self.dt = 0

    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(pygame.Color(0,0,0))
        pygame.display.flip()
        

if __name__ == "__main__":
    main()