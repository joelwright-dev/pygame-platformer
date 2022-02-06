import pygame
from support import import_folder

class Portal(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.pos = pos
        self.surface = surface
        self.image = pygame.Surface((16,32))
        self.rect = self.image.get_rect(topleft = pos)
        self.frame_index = 0
        self.animation_speed = 0.1
        self.frames = import_folder('graphics/level/end_portal')

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]

    def update(self,world_shift):
        self.animate()
        self.world_shift = world_shift
        self.rect.x += self.world_shift