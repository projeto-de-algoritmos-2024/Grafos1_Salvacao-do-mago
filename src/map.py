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
def draw_map(screen, game_map):
    images = load_images()
    # Aqui, estamos percorrendo a matriz
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            # Preenchendo todos os quadrados com a imagem do chão
            screen.blit(images["floor_img"], (x * TILE_SIZE, y * TILE_SIZE))

            # Aqui, verificamos qual o conteúdo do quadrado e, se for algum componente, adicionamos a imagem dele
            if game_map[y][x] == MAGE:
                screen.blit(images["mage_img"], (x * TILE_SIZE, y * TILE_SIZE))
            elif game_map[y][x] == ALLY:
                screen.blit(images["ally_img"], (x * TILE_SIZE, y * TILE_SIZE))
            elif game_map[y][x] == ENEMY:
                screen.blit(images["ogre_img"], (x * TILE_SIZE, y * TILE_SIZE))
            elif game_map[y][x] == FOREST:
                screen.blit(images["forest_img"], (x * TILE_SIZE, y * TILE_SIZE))
            elif game_map[y][x] == RIVER:
                screen.blit(images["river_img"], (x * TILE_SIZE, y * TILE_SIZE))
            elif game_map[y][x] == MOUNTAIN:
                screen.blit(images["mountain_img"], (x * TILE_SIZE, y * TILE_SIZE))