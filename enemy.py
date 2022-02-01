import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, surface, player):
        super().__init__()
        self.image = pygame.Surface((16,16))
        self.image.fill('purple')
        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = surface

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1
        self.gravity = 0.4
        self.jump_speed = -5

        #player status
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.touching_border = False

        #movement to player
        self.player = player
        self.radius = 150

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = self.jump_speed

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        
        if keys[pygame.K_w] and (self.on_ground or self.on_left or self.on_right) and not self.touching_border:
            self.jump()

    def look_at_player(self):
        self.playersprite = self.player.sprite
        self.player_direction = pygame.math.Vector2(self.rect.x - self.playersprite.rect.x, self.rect.y - self.playersprite.rect.y)

    def move_to_player(self):
        self.x_distance = self.player_direction.x
        self.y_distance = self.player_direction.y
        if self.x_distance <= self.radius:
            if self.x_distance < 0:
                self.direction.x = 1
                self.facing_right = False
            else:
                self.direction.x = -1
                self.facing_right = True
        elif self.x_distance > self.radius:
            self.direction.x = 0
        
        if self.on_right or self.on_left:
            self.jump()
        
    def update(self, world_shift):
        if self.player:
            self.look_at_player()
            self.move_to_player()
        #self.get_input()
        self.world_shift = world_shift
        self.rect.x += self.world_shift