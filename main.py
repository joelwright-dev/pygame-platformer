import pygame, sys
from settings import *
from level import Level
from background import Background

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, 32)
CLOCK = pygame.time.Clock()
objects = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
level = Level(LEVEL_MAP, objects)
background = Background(objects,level,True,False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            SCREEN.blit(pygame.transform.scale(objects, event.dict['size']), (0, 0))
            pygame.display.update()
        elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))
            pygame.display.update()

    if not level.gameover:
        background.update()
        background.render()
    level.run()

    SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))
    
    pygame.display.update()
    CLOCK.tick(60)
    objects.fill('black')