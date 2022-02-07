import pygame, sys, os
from settings import *
from level import Level
from background import Background
from text import Text
from button import Button
from pygame import mixer
import pygame._sdl2

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, 32, vsync=1)
window = pygame._sdl2.Window.from_display_module()
CLOCK = pygame.time.Clock()
objects = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

reset = False
spawned = True
menu = True

mixer.init()
click_s = mixer.Sound('sounds/select.wav')
click_s.set_volume(0.1)
mixer.music.load('sounds/theme_main.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

window.maximize()

previous_level = 0
level_changed = False

while True:
    with open('data/current_level.dat', 'r') as l:
        current_level = int(l.readlines()[0])
        if current_level > previous_level:
            level_changed = True
        previous_level = current_level

    click = False
    
    #pygame.event.post(pygame.event.Event(pygame.VIDEOEXPOSE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == pygame.VIDEORESIZE:
            SCREEN.blit(pygame.transform.scale(objects, event.dict['size']), (0, 0))
            pygame.display.update()
        elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))
            pygame.display.update()

    try:
        if level_changed:
            click_s.play()
            del level
            del background
            objects.fill('black')
            SCREEN.fill('black')
            reset = True
            spawned = False
            level_changed = False

        if menu:
            if 'level' not in locals():
                level = Level(levels[current_level], objects)
            if 'background' not in locals():
                background = Background(objects,level,False,True)
            level.world_shift = 1
            background.update()
            clicked = background.render(click)
            header = Text('The Weird World', 'black', objects, (objects.get_rect().width/2, objects.get_rect().height/6), 7)
            header.draw()
            playButton = Button('Play', 'white', 'black', objects, SCREEN, 7, (objects.get_rect().width/2, objects.get_rect().height/3), click)
            playClicked = playButton.update()
            quitButton = Button('Quit', 'white', 'black', objects, SCREEN, 7, (objects.get_rect().width/2, objects.get_rect().height/2), click)
            quitClicked = quitButton.update()
            SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))
            if quitClicked:
                click_s.play()
                break
            elif playClicked:
                click_s.play()
                level.world_shift = 0
                objects.fill('black')
                SCREEN.fill('black')
                menu = False
        else:
            background.update()
            clicked = background.render(click)
            level.run(click)
            SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))

        if level.gameover and reset == False:
            header = Text('You Died', 'black', objects, (objects.get_rect().width/2, objects.get_rect().height/6), 7)
            header.draw()
            restartButton = Button('Restart', 'white', 'black', objects, SCREEN, 7, (objects.get_rect().width/2, objects.get_rect().height/3), click)
            restartClicked = restartButton.update()
            menuButton = Button('Return to menu', 'white', 'black', objects, SCREEN, 7, (objects.get_rect().width/2, objects.get_rect().height/2), click)
            menuClicked = menuButton.update()
            SCREEN.blit(pygame.transform.scale(objects, SCREEN.get_size()), (0, 0))
            if restartClicked:
                click_s.play()
                del level
                del background
                objects.fill('black')
                SCREEN.fill('black')
                reset = True
                spawned = False
            if menuClicked:
                click_s.play()
                del level
                del background
                objects.fill('black')
                SCREEN.fill('black')
                menu = True
    except Exception as e:
        print(e)
        if not spawned:
            try:
                level = Level(levels[current_level], objects)
                background = Background(objects,level,True,False)
                spawned = True
            except:
                print("GAME COMPLETE")
        reset = False
    
    pygame.display.update()
    CLOCK.tick(60)
    objects.fill('black')