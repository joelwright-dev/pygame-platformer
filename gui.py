import pygame

class GUI(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.full = True
        self.half = False
        self.pos = pos
        self.surface = surface

    def update(self):
        if self.full:
            self.half = False
            self.image = pygame.Surface((8,8))
            self.image = pygame.image.load('graphics/gui/hearts/heart_full.png')
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface
        elif self.half:
            self.image = pygame.Surface((8,8))
            self.image = pygame.image.load('graphics/gui/hearts/heart_half.png')
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface
        else:
            self.image = pygame.Surface((8,8))
            self.image = pygame.image.load('graphics/gui/hearts/heart_empty.png')
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface