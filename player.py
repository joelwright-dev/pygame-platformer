import pygame
from support import import_folder
from pygame import mixer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface,create_jump_particles):
        super().__init__()
        mixer.init()
        self.walk = mixer.Sound("sounds/walk1.wav")
        self.walk.set_volume(0.1)
        self.jump_s = mixer.Sound('sounds/jump.wav')
        self.jump_s.set_volume(0.1)
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.05
        self.image = pygame.Surface((16,16))
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        #dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.15
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 2
        self.gravity = 0.4
        self.jump_speed = -5

        #player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.touching_border = False

        #player health
        self.health = 100

    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {
            'idle':[],
            'run':[],
            'jump':[],
            'fall':[],
            'climb':[]
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('graphics/character/dust_particles/run')

    def animate(self):
        animation = self.animations[self.status]
        
        if self.status == 'climb':
            self.animation_speed = 0.2
        else:
            self.animation_speed = 0.05

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

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(0,16)
                self.display_surface.blit(dust_particle,pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(16,16)
                flipped_dust_particle = pygame.transform.flip(dust_particle,True,False)
                self.display_surface.blit(flipped_dust_particle,pos)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
            self.walk.stop()

        if keys[pygame.K_UP] and self.on_ground and not (self.on_left or self.on_right):
            self.jump_speed = -5
            self.jump()
            self.create_jump_particles(self.rect.midbottom)
            self.jump_s.play()
        elif keys[pygame.K_UP] and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.on_ground and self.status == 'climb' and not self.touching_border:
            self.jump_speed = -1
            self.jump()

    def get_status(self):
        if self.on_right or self.on_left:
            self.status = 'climb'
        else:
            if self.direction.y < 0:
                self.status = 'jump'
            elif self.direction.y > 1:
                self.status  = 'fall'
            else:
                if self.direction.x != 0:
                    self.status = 'run'
                else:
                    self.status = 'idle'

    def apply_gravity(self):
        if (self.on_left or self.on_right) and not self.on_ground and not self.touching_border:
            self.direction.y += self.gravity * 0.001
            self.rect.y += self.direction.y
        else:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = self.jump_speed
        
    def advanced_movement(self):
        pass

    def update(self):
        self.get_status()
        self.get_input()
        self.advanced_movement()
        self.animate()
        self.run_dust_animation()