import pygame
from text import Text

class Button(pygame.sprite.Sprite):
    def __init__(self, text, text_color, button_color, surface, screen, size, pos, click):
        super().__init__()
        self.surface = surface
        self.screen = screen
        self.size = size
        self.pos = pos
        self.click = click
        self.button_color = button_color
        self.text = Text(text, text_color, self.surface, (pos[0]+1, pos[1]+1), self.size)
        self.image = pygame.Surface((self.text.textobj.get_rect().width + 3, self.text.textobj.get_rect().height + 3))
        self.rect = self.image.get_rect(center = pos)

    def draw(self):
        self.surface.blit(self.image, self.rect)
        self.border = pygame.image.load('graphics/gui/buttons/button_border.png')
        self.border_rect_left = self.border.get_rect(center = (self.pos[0]-(self.image.get_rect().width/2)-2, self.pos[1]))
        self.border_rect_right = self.border.get_rect(center = ((self.pos[0])+(self.image.get_rect().width/2)+2, self.pos[1]))
        self.image.fill(self.button_color)
        self.rect = self.image.get_rect(center = self.pos)
        self.text.draw()
        self.surface.blit(self.border, self.border_rect_left)
        self.surface.blit(pygame.transform.flip(self.border,True, True), self.border_rect_right)

    def update(self):
        self.draw()
        mpos = list(pygame.mouse.get_pos())
        ratio_x = (self.screen.get_rect().width / self.surface.get_rect().width)
        ratio_y = (self.screen.get_rect().height / self.surface.get_rect().height)
        scaled_pos = (mpos[0] / ratio_x, mpos[1] / ratio_y)
        if self.rect.collidepoint(scaled_pos):
            if self.click:
                return True