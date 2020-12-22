#FproProj
import pygame

pygame.init()



screen = pygame.display.set_mode((1600,900))

pygame.display.set_caption("Flicky")
icon = pygame.image.load("D:/GitHub/FproProj/img/bird.png")
pygame.display.set_icon(icon)


#player while i dont realize how to use sheets
playerimg = pygame.image.load("D:/GitHub/FproProj/img/bird.png")
playerX = 20
playerY = 800
def player():
    screen.blit(playerimg,(playerX, playerY))

#Game loop
running = True
screen.fill((0,255,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Close window
            running = False
    
    
    player()  #draw the player
    pygame.display.update()