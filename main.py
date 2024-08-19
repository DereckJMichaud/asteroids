import pygame
from player import Player
from constants import *

def main():
    pygame.init
    
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for obj in updatable:
            obj.update(dt)
        
        screen.fill(pygame.Color(0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()