import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mapa do Mago")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()