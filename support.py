from os import walk
import os
import pygame

def import_folder(path):
    surface_list = []
    images = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            images.append(full_path)

        images = sorted(images, key=lambda i: int(os.path.splitext(os.path.basename(i))[0]))
        
        for image in images:
            image_surf = pygame.image.load(image).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list

def import_level(path):
    levels = []

    for _,__,dat_files in walk(path):
        for level in dat_files:
            full_path = path + '/' + level
            levels.append(full_path)

        levels = sorted(levels, key=lambda i: int(os.path.splitext(os.path.basename(i))[0]))
    
    return levels