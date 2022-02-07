import pygame, sys, os
from settings import *
from level import Level
from background import Background
from text import Text
from button import Button
from pygame import mixer
import pygame._sdl2

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, 32, vsync=1)
window = pygame._sdl2.Window.from_display_module()
CLOCK = pygame.time.Clock()
objects = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

window.maximize()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == pygame.VIDEORESIZE:
            SCREEN.blit(pygame.transform.scale(objects, event.dict['size']), (0, 0))
            pygame.display.update()
        elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))
            pygame.display.update()

    pygame.display.update()
    CLOCK.tick(60)
    objects.fill('black')