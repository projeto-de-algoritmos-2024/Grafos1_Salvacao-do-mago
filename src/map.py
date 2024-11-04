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
    # Dicionário que mapeia o tipo de obstáculo para suas respectivas coordenadas
    obstacles = {
        FOREST: [(2, 3), (7, 8), (16, 11)],
        RIVER: [(4, 10), (8, 2), (10, 15)],
        MOUNTAIN: [(6, 12), (9, 6), (14, 2)]
    }

    # Loop para inserir os obstáculos no mapa
    for obstacle_type, positions in obstacles.items():
        for x, y in positions:
            game_map[y][x] = obstacle_type

# Função que desenha o mapa
def draw_map(screen, game_map):
    images = load_images()

    image_mapping = {
        MAGE: images["mage_img"],
        ALLY: images["ally_img"],
        ENEMY: images["ogre_img"],
        FOREST: images["forest_img"],
        RIVER: images["river_img"],
        MOUNTAIN: images["mountain_img"],
        PATH: images["floor2_img"]  # Adicione a imagem do caminho se necessário
    }

    # Aqui, estamos percorrendo a matriz
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            # Preenchendo todos os quadrados com a imagem do chão
            screen.blit(images["floor_img"], (x * TILE_SIZE, y * TILE_SIZE))

            element = game_map[y][x]
            if element in image_mapping:
                screen.blit(image_mapping[element], (x * TILE_SIZE, y * TILE_SIZE))
