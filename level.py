import pygame
from tiles import Tile
from player import Player
from enemy import Enemy
from gui import GUI
from settings import TILE_SIZE, SCREEN_WIDTH
from particles import ParticleEffect

class Level:
    def __init__(self, level_data, surface):
        super().__init__()
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = 0

        self.setup_level(level_data)

        #dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def create_jump_particles(self,pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10,5)
        else:
            pos += pygame.math.Vector2(10,-5)
        jump_particle_sprite = ParticleEffect(pos,'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10,15)
            else:
                offset = pygame.math.Vector2(-10,15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
            self.dust_sprite.add(fall_dust_particle)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.gui = pygame.sprite.Group()
        self.decor = pygame.sprite.Group()
        self.border = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == "P":
                    player_sprite = Player((x,y),self.display_surface,self.create_jump_particles)
                    self.player.add(player_sprite)
                    for i in range(0,int(self.player.sprite.health/10)):
                        gui = GUI((4 + (8*i) + (i*4),4), self.display_surface)
                        self.gui.add(gui)
                elif col != " ":
                    if col != 'F' and col != "S" and col != "Q" and col != 'D' and col != "N" and col != "E":
                        tile = Tile((x,y),TILE_SIZE,col)
                        self.tiles.add(tile)
                    else:
                        if col == "N":
                            tile = Tile((x,y),TILE_SIZE,col)
                            self.border.add(tile)
                        elif col == "E":
                            enemy_sprite = Enemy((x,y),self.display_surface, self.player)
                            self.enemies.add(enemy_sprite)
                        else:
                            tile = Tile((x,y),TILE_SIZE,col)
                            self.decor.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH / 8 and direction_x < 0:
            self.world_shift = 3
            player.speed = 0
        elif player_x > SCREEN_WIDTH * 7/8 and direction_x > 0:
            self.world_shift = -3
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 3

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        for sprite in self.border.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    player.touching_border = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    player.touching_border = True
                    self.current_x = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
            player.touching_border = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
            player.touching_border = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def horizontal_movement_collision_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.rect.x += enemy.direction.x * enemy.speed

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                        enemy.on_left = True
                        self.current_x = enemy.rect.left
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                        enemy.on_right = True
                        self.current_x = enemy.rect.right

            for sprite in self.border.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                        enemy.on_left = True
                        enemy.touching_border = True
                        self.current_x = enemy.rect.left
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                        enemy.on_right = True
                        enemy.touching_border = True
                        self.current_x = enemy.rect.right
            
            if enemy.on_left and (enemy.rect.left < self.current_x or enemy.direction.x >= 0):
                enemy.on_left = False
                enemy.touching_border = False
            if enemy.on_right and (enemy.rect.right > self.current_x or enemy.direction.x <= 0):
                enemy.on_right = False
                enemy.touching_border = False

    def vertical_movement_collision_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.apply_gravity()

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.y > 0:
                        enemy.rect.bottom = sprite.rect.top
                        enemy.direction.y = 0
                        enemy.on_ground = True
                    elif enemy.direction.y < 0:
                        enemy.rect.top = sprite.rect.bottom
                        enemy.direction.y = 0
                        enemy.on_ceiling = True
            
            if enemy.on_ground and enemy.direction.y < 0 or enemy.direction.y > 1:
                enemy.on_ground = False
            if enemy.on_ceiling and enemy.direction.y > 0:
                enemy.on_ceiling = False

    def player_collision_enemy(self):
        player = self.player.sprite
        for enemy in self.enemies.sprites():
            if player.rect.colliderect(enemy.rect):
                player.image.fill('blue')

    def update_gui(self):
        player = self.player.sprite
        health = int(player.health)
        if(health > 0):
            first = int(str(health)[0])
        if(len(str(health)) >= 2):
            second = int(str(health)[1])
        for enemy in self.enemies.sprites():
            if player.rect.colliderect(enemy.rect) and health > 0:
                player.health -= 0.1

        for index,heart in enumerate(self.gui):
            if health > 0:
                if (index == first):
                    if (len(str(health)) >= 2 and second <= 5 and len(str(health)) > 1):
                        heart.full = False
                        heart.half = True
                    elif len(str(health)) > 1:
                        heart.full = True
                        heart.half = False
                    else:
                        heart.full = False
                        heart.half = False
                elif (len(str(health)) >= 1 and index < first and len(str(health)) > 1):
                    heart.full = True
                    heart.half = False
                else:
                    heart.full = False
                    heart.half = False
            else:
                heart.full = False
                heart.half = False

            print(int(health), heart.full, heart.half)

    def run(self):
        #dust particles
        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)

        #Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.border.update(self.world_shift)
        self.border.draw(self.display_surface)
        
        #Player
        self.player.update()
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.create_landing_dust()
        self.player.draw(self.display_surface)

        self.update_gui()

        self.gui.update()
        self.gui.draw(self.display_surface)

        #enemies
        self.enemies.update(self.world_shift)
        self.horizontal_movement_collision_enemy()
        self.vertical_movement_collision_enemy()
        self.enemies.draw(self.display_surface)

        self.player_collision_enemy()

        self.decor.update(self.world_shift)
        self.decor.draw(self.display_surface)
        self.scroll_x()