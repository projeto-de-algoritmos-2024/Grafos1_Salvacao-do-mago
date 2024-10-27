import pygame
pygame.init()

TILE_SIZE = 35
MAP_SIZE = 40

screen = pygame.display.set_mode((MAP_SIZE * TILE_SIZE, MAP_SIZE * TILE_SIZE))
pygame.display.set_caption("Mapa do Mago")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

mage_img = pygame.image.load('assets/mage.png')
ally_img = pygame.image.load('assets/ally.png')
ogre_img = pygame.image.load('assets/ogre.png')
river_img = pygame.image.load('assets/river.png')
mountain_img = pygame.image.load('assets/mountain.png')
forest_img = pygame.image.load('assets/forest.png')

mage_img = pygame.transform.scale(mage_img, (TILE_SIZE, TILE_SIZE))
ally_img = pygame.transform.scale(ally_img, (TILE_SIZE, TILE_SIZE))
ogre_img = pygame.transform.scale(ogre_img, (TILE_SIZE, TILE_SIZE))
forest_img = pygame.transform.scale(forest_img, (TILE_SIZE, TILE_SIZE))
river_img = pygame.transform.scale(river_img, (TILE_SIZE, TILE_SIZE))
mountain_img = pygame.transform.scale(mountain_img, (TILE_SIZE, TILE_SIZE))

map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

map[0][0] = 1
map[5][5] = 2
map[10][10] = 2
map[15][15] = 2
map[20][20] = 3
map[25][25] = 3

map[2][3] = 4
map[7][8] = 4
map[4][15] = 5
map[10][20] = 5
map[18][2] = 6
map[22][10] = 6

def draw_map():
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            if map[y][x] == 1:
                screen.blit(mage_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif map[y][x] == 2:
                screen.blit(ally_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif map[y][x] == 3:
                screen.blit(ogre_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif map[y][x] == 4:
                screen.blit(forest_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif map[y][x] == 5:
                screen.blit(river_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif map[y][x] == 6:
                screen.blit(mountain_img, (x * TILE_SIZE, y * TILE_SIZE))
            else: 
                pygame.draw.rect(screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

            pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_map()
    pygame.display.flip()

pygame.quit()