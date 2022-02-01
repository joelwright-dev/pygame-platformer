import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, text, color, surface, pos, size):
        super().__init__()
        font = pygame.font.Font('graphics/fonts/WayfarersToyBoxRegular-gxxER.ttf', size)
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect(center = pos)
        self.surface = surface
    
    def draw(self):
        self.surface.blit(self.textobj, self.textrect)