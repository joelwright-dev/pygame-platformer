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
            self.image.fill("red")
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface
        elif self.half:
            self.image = pygame.Surface((4,8))
            self.image.fill("red")
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface
        else:
            self.image = pygame.Surface((8,8))
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface