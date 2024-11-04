import pygame
import random
from constants import *
from map import draw_map, create_map
from image_loader import load_images  # Importe a função para carregar imagens

class Game:
    def __init__(self):
        # Definindo o tamanho da janela e o título
        self.screen = pygame.display.set_mode((MAP_SIZE * TILE_SIZE, MAP_SIZE * TILE_SIZE + MENU_HEIGHT))
        pygame.display.set_caption("Mapa do Mago")
        self.map = create_map()
        self.allies_positions = []  # Lista para armazenar as posições dos aliados

        # Carregando todas as imagens
        self.images = load_images()  # Carrega todas as imagens, incluindo a do aliado
        self.ally_image = self.images["ally_img"]  # Usa a imagem do aliado carregada

        self.buttons = [
            {"rect": pygame.Rect(115, 730, 150, 40), "text": "Add Aliados"},
            {"rect": pygame.Rect(285, 730, 150, 40), "text": "Add Inimigos"},
            {"rect": pygame.Rect(455, 730, 150, 40), "text": "Iniciar BFS"}
        ]

    def add_characters(self, character_type, count):
        added = 0
        while added < count:
            x = random.randint(0, MAP_SIZE - 1)
            y = random.randint(0, MAP_SIZE - 1)
            if self.map[y][x] == 0:  # Verifica se a posição está vazia
                self.map[y][x] = character_type  # Adiciona o personagem no mapa
                if character_type == ALLY:
                    self.allies_positions.append((x, y))  # Adiciona a posição do aliado à lista
                added += 1
                print(f"{character_type} adicionado em: ({x}, {y})")

    def bfs(self, start, goal):
        queue = [start]
        visited = set()
        paths = {start: []}
        
        while queue:
            current = queue.pop(0)
            print(f"Visitando: {current}, Caminho até agora: {paths[current]}")

            if current == goal:
                return paths[current]
            
            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimentos: cima, baixo, esquerda, direita
                neighbor = (x + dx, y + dy)
                if 0 <= neighbor[0] < MAP_SIZE and 0 <= neighbor[1] < MAP_SIZE:  # Verifica limites do mapa
                    if neighbor not in visited and self.map[neighbor[1]][neighbor[0]] not in [ENEMY, FOREST, RIVER, MOUNTAIN]:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        paths[neighbor] = paths[current] + [neighbor]
        
        return []  # Retorna uma lista vazia se não encontrar caminho

    def find_all_paths(self, start):
        paths = []
        for ally in self.allies_positions:
            path = self.bfs(start, ally)
            if path:
                paths.append((ally, path))
                start = ally  # Atualiza a posição inicial para o próximo aliado
        return paths

    def handle_button_click(self, button):
        if button["text"] == "Add Aliados":
            self.add_characters(ALLY, 1)  # Adiciona um aliado
        elif button["text"] == "Add Inimigos":
            self.add_characters(ENEMY, 1)  # Adiciona um inimigo
        elif button["text"] == "Iniciar BFS":
            start = (0, 0)  # Posição inicial do mago
            paths = self.find_all_paths(start)  # Encontra todos os caminhos para os aliados
            
            # Atualiza o mapa com todos os caminhos encontrados
            for ally, path in paths:
                for (x, y) in path:  # Desenha cada caminho encontrado
                    self.map[y][x] = PATH
            print("Caminhos encontrados:", paths)

    def draw_buttons(self):
        for button in self.buttons:
            pygame.draw.rect(self.screen, BUTTON_COLOR, button["rect"])
            font = pygame.font.SysFont("Monospace", 15, True)
            text = font.render(button["text"], True, WHITE)
            self.screen.blit(text, (button["rect"].x + 25, button["rect"].y + 10))

    def draw_characters(self):
        for ally in self.allies_positions:  # Desenha todos os aliados no mapa
            x, y = ally
            self.screen.blit(self.ally_image, (x * TILE_SIZE, y * TILE_SIZE))  # Usa a imagem do aliado

    def run(self):
        running = True
        print("Iniciando o jogo...")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Saindo do jogo...")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    print(f"Clique em: {mouse_pos}")  # Exibir a posição do clique
                    for button in self.buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            self.handle_button_click(button)

            self.screen.fill(WHITE)
            pygame.draw.rect(self.screen, BLACK, (0, 0, MAP_SIZE * TILE_SIZE, MENU_HEIGHT))
            draw_map(self.screen, self.map)
            self.draw_characters()  # Desenha os aliados após desenhar o mapa
            self.draw_buttons()
            pygame.display.flip()

        pygame.quit()

