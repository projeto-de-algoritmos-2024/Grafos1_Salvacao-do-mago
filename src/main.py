import pygame
import random

pygame.init()

# Definindo o tamanho de cada quadrado e o tamanho da matriz
TILE_SIZE = 40
MAP_SIZE = 18
MENU_HEIGHT = 60

# Definindo o tamanho da janela e o título
screen = pygame.display.set_mode((MAP_SIZE * TILE_SIZE, MAP_SIZE * TILE_SIZE + MENU_HEIGHT))
pygame.display.set_caption("Mapa do Mago")

# Criando algumas constantes de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MENU_BG = (58, 90, 64) 
BUTTON_COLOR = (52, 78, 65)

# Carregando em variáveis as imagens dos elementos
mage_img = pygame.image.load('assets/mage.png')
ally_img = pygame.image.load('assets/ally.png')
ogre_img = pygame.image.load('assets/ogre.png')
river_img = pygame.image.load('assets/river.png')
mountain_img = pygame.image.load('assets/mountain.png')
forest_img = pygame.image.load('assets/forest.png')
floor_img = pygame.image.load('assets/floor.png')

# Mudando a escala dos elementos para se adequar aos quadrados do mapa
mage_img = pygame.transform.scale(mage_img, (TILE_SIZE, TILE_SIZE))
ally_img = pygame.transform.scale(ally_img, (TILE_SIZE, TILE_SIZE))
ogre_img = pygame.transform.scale(ogre_img, (TILE_SIZE, TILE_SIZE))
forest_img = pygame.transform.scale(forest_img, (TILE_SIZE, TILE_SIZE))
river_img = pygame.transform.scale(river_img, (TILE_SIZE, TILE_SIZE))
mountain_img = pygame.transform.scale(mountain_img, (TILE_SIZE, TILE_SIZE))
floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))

# Criando o mapa e preenchendo com nada
map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Mago = 1, Aliados = 2, Inimigos = 3, Floresta = 4, Rio = 5, Montanha = 6

# Inserindo a posição do mago
map[0][0] = 1

# Inserindo os obstáculos
# Floresta
map[2][3] = 4
map[7][8] = 4
map[16][11] = 4

# Rio
map[4][10] = 5
map[8][2] = 5
map[10][15] = 5

# Montanha
map[6][12] = 6
map[9][6] = 6
map[14][2] = 6

allies_added = False
enemies_added = False

buttons = [
    {"rect": pygame.Rect(115, 730, 150, 40), "text": "Add Aliados"},
    {"rect": pygame.Rect(285, 730, 150, 40), "text": "Add Inimigos"},
    {"rect": pygame.Rect(455, 730, 150, 40), "text": "Iniciar BFS"}
]

def add_characters(character_type, count):
    added = 0
    while added < count:
        x = random.randint(0, MAP_SIZE - 1)
        y = random.randint(0, MAP_SIZE - 1)
        if map[y][x] == 0:
            map[y][x] = character_type
            added+=1

def draw_buttons():
    for button in buttons:
        pygame.draw.rect(screen, BUTTON_COLOR, button["rect"])
        font = pygame.font.SysFont("Monospace", 15, True)
        text = font.render(button["text"], True, WHITE)
        screen.blit(text, (button["rect"].x + 25, button["rect"].y + 10))

# Função que desenha o mapa
def draw_map():
    # Aqui, estamos percorrendo a matriz
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            # Preenchendo todos os quadrados com a imagem do chão
            screen.blit(floor_img, (x * TILE_SIZE, y * TILE_SIZE))

            # Aqui, verificamos qual o conteúdo do quadrado e, se for algum componente, adicionamos a imagem dele
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


# Enquanto o programa estiver em execução, ocorre o que ta dentro do loop
running = True
while running:
    # Capturamos o evento
    for event in pygame.event.get():
        # Se for evento de quit, ou seja, fechar a janela, alteramos o estado de running
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for button in buttons:
                if button["rect"].collidepoint(mouse_pos):
                    if button["text"] == "Add Aliados" and not allies_added:
                        add_characters(2, 3)
                        allies_added = True
                    elif button["text"] == "Add Inimigos" and not enemies_added:
                        add_characters(3, 3)
                        enemies_added = True
                    elif button["text"] == "Iniciar BFS":
                        print("Iniciando BFS...")

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, MAP_SIZE * TILE_SIZE, MENU_HEIGHT))
    draw_map()
    draw_buttons()
    pygame.display.flip()

pygame.quit()