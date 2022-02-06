import pygame
from support import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, surface, player):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.05
        self.image = pygame.Surface((16,16))
        self.status = 'run'
        self.image = self.animations['attack'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = surface
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
        self.touching_player = False

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
        if not self.touching_player:
            self.status = 'run'
        else:
            self.status = 'attack'

    def move_to_player(self):
        self.x_distance = self.player_direction.x
        self.y_distance = self.player_direction.y
        if self.x_distance <= self.radius:
            if self.x_distance < 0:
                self.direction.x = 1
                self.facing_right = True
            else:
                self.direction.x = -1
                self.facing_right = False
        elif self.x_distance > self.radius:
            self.direction.x = 0
        
        if self.on_right or self.on_left:
            self.status = 'climb'
            self.jump()

    def import_character_assets(self):
        character_path = 'graphics/enemy/'
        self.animations = {
            'attack':[],
            'run':[],
            'climb':[]
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('graphics/character/dust_particles/run')

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        
    def update(self, world_shift):
        if self.player:
            self.look_at_player()
            self.move_to_player()
        #self.get_input()
        self.animate()
        self.world_shift = world_shift
        self.rect.x += self.world_shift