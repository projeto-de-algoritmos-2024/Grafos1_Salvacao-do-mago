import pygame
import random
from constants import *
from map import draw_map, create_map
from collections import deque


class Game:
    def __init__(self):
        # Definindo o tamanho da janela e o título
        self.screen = pygame.display.set_mode((MAP_SIZE * TILE_SIZE, MAP_SIZE * TILE_SIZE + MENU_HEIGHT))
        pygame.display.set_caption("Mapa do Mago")
        self.map = create_map()
        self.allies_added = False
        self.enemies_added = False
        self.last_path = None  # Inicializa last_path como None


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
            if self.map[y][x] == 0:
                self.map[y][x] = character_type
                added+=1

    def draw_buttons(self):
        for button in self.buttons:
            pygame.draw.rect(self.screen, BUTTON_COLOR, button["rect"])
            font = pygame.font.SysFont("Monospace", 15, True)
            text = font.render(button["text"], True, WHITE)
            self.screen.blit(text, (button["rect"].x + 25, button["rect"].y + 10))
    

    def bfs(self, game_map, start, goals):
        rows, cols = len(game_map), len(game_map[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(start, [start])])  # Fila que armazena o nó atual e o caminho até ele

        while queue:
            (x, y), path = queue.popleft()

            # Verifica se chegamos a um dos aliados
            if (x, y) in goals:
                print(f"Caminho encontrado: {path}")  # Adicione esta linha
                return path  # Retorna o caminho encontrado

            # Marca o nó como visitado
            visited[y][x] = True

            # Movimentos possíveis: cima, baixo, esquerda, direita
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx] and game_map[ny][nx] == 0:
                    queue.append(((nx, ny), path + [(nx, ny)]))

        print("Nenhum caminho encontrado.")  # Adicione esta linha
        return None  # Retorna None se não houver caminho

    def highlight_path(self, path):
        if path:
            for (x, y) in path:
                pygame.draw.rect(self.screen, (255, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))



    def handle_button_click(self, button):
        if button["text"] == "Add Aliados" and not self.allies_added:
            self.add_characters(ALLY, 3)
            self.allies_added = True
        elif button["text"] == "Add Inimigos" and not self.enemies_added:
            self.add_characters(ENEMY, 3)
            self.enemies_added = True
        elif button["text"] == "Iniciar BFS":
            start = (0, 0)  # Posição inicial
            goals = []  # Lista para armazenar as posições dos aliados
            for y in range(MAP_SIZE):
                for x in range(MAP_SIZE):
                    if self.map[y][x] == ALLY:  # Adiciona a posição dos aliados
                        goals.append((x, y))

            # Chame o método bfs usando self
            path = self.bfs(self.map, start, goals)  # Passa o mapa como argumento
            self.last_path = path  # Armazena o caminho encontrado
            if path:
                print("Caminho encontrado:", path)
            else:
                print("Nenhum caminho encontrado.")


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in self.buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            self.handle_button_click(button)

            self.screen.fill(WHITE)
            pygame.draw.rect(self.screen, BLACK, (0, 0, MAP_SIZE * TILE_SIZE, MENU_HEIGHT))
            
            # Passa o caminho encontrado para a função draw_map
            draw_map(self.screen, self.map, getattr(self, 'last_path', None))  # Passa o caminho se ele existir
            self.highlight_path(self.last_path)  # Destaque o caminho
            self.draw_buttons()
            pygame.display.flip()

        pygame.quit()
