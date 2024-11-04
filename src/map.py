from os import path

import pygame
from constants import *
from images import load_images

def create_map():
    # Criando o mapa e preenchendo com nada
    game_map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    # Inserindo a posição do mago
    game_map[0][0] = MAGE
    add_obstacles(game_map)
    return game_map

def add_obstacles(game_map):
    # Inserindo os obstáculos
    # Floresta
    game_map[2][3] = FOREST
    game_map[7][8] = FOREST
    game_map[16][11] = FOREST

    # Rio
    game_map[4][10] = RIVER
    game_map[8][2] = RIVER
    game_map[10][15] = RIVER

    # Montanha
    game_map[6][12] = MOUNTAIN
    game_map[9][6] = MOUNTAIN
    game_map[14][2] = MOUNTAIN

# Função que desenha o mapa
def draw_map(screen, game_map, path=None):
    images = load_images()

    image_mapping = {
        MAGE: images["mage_img"],
        ALLY: images["ally_img"],
        ENEMY: images["ogre_img"],
        FOREST: images["forest_img"],
        RIVER: images["river_img"],
        MOUNTAIN: images["mountain_img"]
    }

    # Percorrendo a matriz do mapa
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            # Preenchendo todos os quadrados com a imagem do chão
            screen.blit(images["floor_img"], (x * TILE_SIZE, y * TILE_SIZE))

            element = game_map[y][x]
            if element in image_mapping:
                screen.blit(image_mapping[element], (x * TILE_SIZE, y * TILE_SIZE))

            # Desenhar o caminho se fornecido
            if path and (x, y) in path:
                # Desenhar um retângulo vermelho para destacar o caminho
                pygame.draw.rect(screen, (255, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

                