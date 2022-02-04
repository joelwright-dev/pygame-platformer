import pygame, sys

SCREEN_WIDTH,SCREEN_HEIGHT = 1280,720    
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, 32, vsync=1)
objects = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        
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
    pygame.display.update()