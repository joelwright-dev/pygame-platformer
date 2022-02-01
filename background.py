import pygame

class Background():
    def __init__(self, display_surface, level):
        self.level = level
        self.display_surface = display_surface
        self.bgimage = pygame.image.load('graphics/background/background_0.png')
        self.bgimagemid = pygame.image.load('graphics/background/background_1.png')
        self.bgimagefor = pygame.image.load('graphics/background/background_2.png')
        self.rectBGimg = self.bgimage.get_rect()
        self.rectBGimgmid = self.bgimagemid.get_rect()
        self.rectBGimgfor = self.bgimagefor.get_rect()

        self.bgY1 = -52
        self.bgX1 = 0

        self.bgY1mid = -52
        self.bgX1mid = 0

        self.bgY1for = -52
        self.bgX1for = 0
        
    def update(self):
        self.bgX1 -= self.level.world_shift * -0.1
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width

        self.bgX1mid -= self.level.world_shift * -0.15
        if self.bgX1mid <= -self.rectBGimg.width:
            self.bgX1mid = self.rectBGimg.width

        self.bgX1for -= self.level.world_shift * -0.25
        if self.bgX1for <= -self.rectBGimg.width:
            self.bgX1for = self.rectBGimg.width
            
    def render(self):
        self.rel_x = self.bgX1 % self.bgimage.get_rect().width
        self.display_surface.blit(self.bgimage, (self.rel_x - self.bgimage.get_rect().width, self.bgY1))
        self.display_surface.blit(self.bgimage, (self.rel_x, self.bgY1))
        if self.rel_x < self.display_surface.get_rect().width:
            self.display_surface.blit(self.bgimage, (self.rel_x + self.bgimage.get_rect().width, self.bgY1))
        
        self.rel_xmid = self.bgX1mid % self.bgimagemid.get_rect().width
        self.display_surface.blit(self.bgimagemid, (self.rel_xmid - self.bgimagemid.get_rect().width, self.bgY1mid))
        self.display_surface.blit(self.bgimagemid, (self.rel_xmid, self.bgY1mid))
        if self.rel_xmid < self.display_surface.get_rect().width:
            self.display_surface.blit(self.bgimagemid, (self.rel_xmid + self.bgimagemid.get_rect().width, self.bgY1mid))

        self.rel_xfor = self.bgX1for % self.bgimagefor.get_rect().width
        self.display_surface.blit(self.bgimagefor, (self.rel_xfor - self.bgimagefor.get_rect().width, self.bgY1for))
        self.display_surface.blit(self.bgimagefor, (self.rel_xfor, self.bgY1for))
        if self.rel_xfor < self.display_surface.get_rect().width:
            self.display_surface.blit(self.bgimagefor, (self.rel_xfor + self.bgimagefor.get_rect().width, self.bgY1for))