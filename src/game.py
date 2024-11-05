import pygame
import random
from constants import *
from collections import deque
from map import draw_map, create_map
from images import load_images  # Importe a função para carregar imagens

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

        self.animating = False
        self.all_paths = []
        self.current_path_index = 0
        self.current_step_index = 0

        self.buttons = [
            {"rect": pygame.Rect(30, 730, 150, 40), "text": "Add Aliados"},
            {"rect": pygame.Rect(200, 730, 150, 40), "text": "Add Inimigos"},
            {"rect": pygame.Rect(370, 730, 150, 40), "text": "Start BFS"},
            {"rect": pygame.Rect(540, 730, 150, 40), "text": "Reset Game"} 
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
        queue = deque([start])
        visited = set()
        paths = {start: []}
        
        while queue:
            current = queue.popleft()
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
        self.all_paths = []
        for ally in self.allies_positions:
            path = self.bfs(start, ally)
            if path:
                self.all_paths.append(path)
                start = ally  # Atualiza a posição inicial para o próximo aliado

    def handle_button_click(self, button):
        if button["text"] == "Add Aliados":
            self.add_characters(ALLY, 1)  # Adiciona um aliado
        elif button["text"] == "Add Inimigos":
            self.add_characters(ENEMY, 1)  # Adiciona um inimigo
        elif button["text"] == "Start BFS":
            start = (0, 0)  # Posição inicial do mago
            self.find_all_paths(start)  # Encontra todos os caminhos para os aliados
            # Atualiza o mapa com todos os caminhos encontrados
            if self.all_paths:
                self.animate_path()

        elif button["text"] == "Reset Game":
            self.reset_game()

    def animate_path(self):
        self.animating = True
        self.current_path_index =  0
        self.current_step_index = 0

    def reset_game(self):
        self.map = create_map()
        self.allies_positions = []
        print("Jogo resetou meu bom")

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
            self.screen.fill(WHITE)
            draw_map(self.screen, self.map)

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
            
            if self.animating:
                if self.current_path_index < len(self.all_paths):
                    path = self.all_paths[self.current_path_index]
                    if self.current_step_index < len(path):
                        x, y = path[self.current_step_index]
                        self.map[y][x] = PATH
                        self.current_step_index += 1
                    else:
                        self.current_path_index += 1
                        self.current_step_index = 0
                else:
                    self.animating = False

            self.draw_characters()  # Desenha os aliados após desenhar o mapa
            self.draw_buttons()
            pygame.display.flip()
            pygame.time.delay(100) 

        pygame.quit()

