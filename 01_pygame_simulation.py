#!/usr/bin/env python

import pygame
import sys
import random

from pygame.locals import *

FPS = 30
pygame.init()
fpsClock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((125, 125, 125))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

screen.blit(surface, (0, 0))

def draw_box(surf, color, pos):
    r = pygame.Rect((pos[0], pos[1]), (10, 10))
    pygame.draw.rect(surf, color, r)


if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        surface.fill((255, 255, 255))
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(0, 0, 400, 400))

        screen.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.display.update()