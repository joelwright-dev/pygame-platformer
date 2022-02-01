import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, type):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.type = type
        if type == 'C':
            #CENTER
            self.image = pygame.image.load('graphics/level/center.png')
        elif type == 'X':
            #PLATFORM MIDDLE
            self.image = pygame.image.load('graphics/level/platformcenter.png')
        elif type == 'M':
            #RIGHT PLATFORM
            self.image = pygame.image.load('graphics/level/platformright.png')
        elif type == 'K':
            #LEFT PLATFORM
            self.image = pygame.image.load('graphics/level/platformleft.png')
        elif type == 'T':
            #TOP
            self.image = pygame.image.load('graphics/level/edge.png')
        elif type == 'H':
            #TOP RIGHT
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/corner.png'), -90)
        elif type == 'I':
            #TOP LEFT
            self.image = pygame.image.load('graphics/level/corner.png')
        elif type == 'R':
            #RIGHT
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/edge.png'), -90)
        elif type == 'L':
            #LEFT
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/edge.png'), 90)
        elif type == 'B':
            #BOTTOM
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/edge.png'), 180)
        elif type == 'G':
            #BOTTOM RIGHT
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/corner.png'), 180)
        elif type == 'J':
            #BOTTOM LEFT
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/corner.png'), 90)
        elif type == 'N':
            #BORDER
            self.image = pygame.transform.rotate(pygame.image.load('graphics/level/border.png'), 180)
        elif type == 'D':
            #DRIP
            self.image = pygame.image.load('graphics/level/drip.png')
        elif type == 'F':
            #FOLIAGE
            self.image = pygame.image.load('graphics/level/foliage.png')
        elif type == 'Q':
            #GRASS
            self.image = pygame.image.load('graphics/level/grass.png')
        elif type == 'S':
            #ROCK
            self.image = pygame.image.load('graphics/level/rock.png')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift