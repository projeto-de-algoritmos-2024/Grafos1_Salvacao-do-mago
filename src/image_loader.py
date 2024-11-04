import pygame
from constants import TILE_SIZE  # Certifique-se de que TILE_SIZE está definido em constants.py

def load_images():
    images = {
        "ally_img": load_image('../assets/ally.png'),  # Carregando a imagem do aliado com a função load_image
    }
    return images

def load_image(image_path, scale=True):
    image = pygame.image.load(image_path).convert_alpha()  # Carrega a imagem
    if scale:
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))  # Redimensiona a imagem para TILE_SIZE
    return image
