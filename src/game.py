import pygame
import random
from constants import *
from map import draw_map, create_map

class Game:
    def __init__(self):
        # Definindo o tamanho da janela e o título
        self.screen = pygame.display.set_mode((MAP_SIZE * TILE_SIZE, MAP_SIZE * TILE_SIZE + MENU_HEIGHT))
        pygame.display.set_caption("Mapa do Mago")
        self.map = create_map()
        self.allies_added = False
        self.enemies_added = False

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
    
    def handle_button_click(self, button_text):
        if button_text["text"] == "Add Aliados" and not self.allies_added:
            self.add_characters(2, 3)
            self.allies_added = True
        elif button_text["text"] == "Add Inimigos" and not self.enemies_added:
            self.add_characters(3, 3)
            self.enemies_added = True
        elif button_text["text"] == "Iniciar BFS":
            print("Iniciando BFS...")

    def run(self):
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
                    for button in self.buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            self.handle_button_click(button)
            self.screen.fill(WHITE)

            pygame.draw.rect(self.screen, BLACK, (0, 0, MAP_SIZE * TILE_SIZE, MENU_HEIGHT))
            draw_map(self.screen, self.map)
            self.draw_buttons()
            pygame.display.flip()

        pygame.quit()