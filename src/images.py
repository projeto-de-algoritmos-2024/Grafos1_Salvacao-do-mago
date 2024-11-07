import pygame
import os
from constants import TILE_SIZE

def load_images():
    # Carregando em variáveis as imagens dos elementos
    images = {
        "mage_img": load_image('../assets/mage.png'),
        "ally_img": load_image('../assets/ally.png'),
        "ogre_img": load_image('../assets/ogre.png'),
        "river_img": load_image('../assets/river.png'),
        "mountain_img": load_image('../assets/mountain.png'),
        "forest_img": load_image('../assets/forest.png'),
        "floor_img": load_image('../assets/floor.png'),
        "floor2_img": load_image('../assets/floor2.png')
    }

    return images

def load_image(image_path, scale = True):
    image = pygame.image.load(image_path)
    if scale:
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    return image
