import pygame
from text import Text
from support import import_folder

class GUI(pygame.sprite.Sprite):
    def __init__(self, pos, surface, count, artifact):
        super().__init__()
        self.artifact = artifact
        self.count = count
        self.frame_index = 0
        self.animation_speed = 0.1
        self.full = True
        self.half = False
        self.pos = pos
        self.surface = surface
        if self.artifact:
            self.frames = import_folder('graphics/gui/artifacts')

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        if self.artifact:
            self.image = pygame.Surface((8,8))
            self.animate()
            self.rect = self.image.get_rect(topleft = self.pos)
            self.display_surface = self.surface
            self.text = Text(str(int(self.count/2)), 'white', self.surface, (self.pos[0]-8, self.pos[1]+5), 7)
            self.text.draw()
        
        else:
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