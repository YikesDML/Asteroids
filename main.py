import pygame
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

def main():
    pygame.init()
    print("""Starting Asteroids!
Screen width: 1280
Screen height: 720""")
    
running = True
while running:
    event = pygame.event.wait ()
    if event.type == pygame.QUIT:
        running = False
    pygame.Surface.fill(screen, (20, 20, 20))
    pygame.display.flip()    
pygame.quit ()


if __name__ == "__main__":
        main()