import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    print('Init Pygame')

#initialize a window for display
    surface = pygame.display.set_mode((1024, 1024))

#change window background
    surface.fill((255,255,255))
    pygame.display.flip()

#event loop which is waiting for user inpunt useing pygame.locals

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.hey == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False


