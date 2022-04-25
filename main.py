import pygame
from pygame.locals import *


def draw_Snake():
    # print out on surface (background screen) our Snake
    surface.fill((22, 55, 33))
    surface.blit(head, (head_x,head_y))
    surface.blit(body, (body_x,body_y))
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    print('Init Pygame')

#initialize a window for display
    surface = pygame.display.set_mode((1824, 920))

#load a head and body of Snake
    head = pygame.image.load("resources/snake_head.png").convert()
    body = pygame.image.load("resources/snake_body.png").convert()

#background screen is a surface where we print out our Snake
    head_x = 100
    head_y = 100
    body_x = 177
    body_y = 100

    pygame.display.flip()

#event loop which is waiting for user inpunt useing pygame.locals

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                #moveing our Snake on x and y coordinates
                if event.key == K_UP:
                    head_y -= 10
                    body_y -= 10
                    draw_Snake()
                if event.key == K_DOWN:
                    head_y += 10
                    body_y += 10
                    draw_Snake()
                if event.key == K_LEFT:
                    head_x -= 10
                    body_x -= 10
                    draw_Snake()
                if event.key == K_RIGHT:
                    head_x += 10
                    body_x += 10
                    draw_Snake()
            elif event.type == QUIT:
                running = False


