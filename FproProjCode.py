#FproProj
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## fechar tela
            running = False