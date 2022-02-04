import pygame
from support import import_folder

class Pickup(pygame.sprite.Sprite):
    def __init__(self, pos, surface, player, type):
        super().__init__()
        self.pos = pos
        self.surface = surface
        self.player = player
        self.image = pygame.Surface((16,16))
        self.rect = self.image.get_rect(topleft = pos)
        self.frame_index = 0
        self.animation_speed = 0.1
        self.type = type
        if self.type == "heart":
            self.frames = import_folder('graphics/level/pickups/heart')
        if self.type == "coin":
            self.frames = import_folder('graphics/level/pickups/coin')

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]

    def update(self,world_shift):
        self.animate()
        self.world_shift = world_shift
        self.rect.x += self.world_shift