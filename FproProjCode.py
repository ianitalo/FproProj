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
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerimg,(x, y))

#Game loop
running = True
Jump = False
while running:   
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Close window
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP and playerY == 800:  #Provisory jump
                playerY_change -= 1
                Jump = True                
            if event.key == pygame.K_LEFT:     #movement
                playerX_change -= 1              
            if event.key == pygame.K_RIGHT:
                playerX_change += 1
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change = 0        
              if event.key == pygame.K_UP:
                  Jump = False     
    
    #Provisory jump
    if Jump == False and playerY < 800:
        playerY_change = 1
        print("hello")
        print(playerY)        
    if playerY_change == 1 and playerY == 800 and Jump == False:
        playerY_change = 0
        playerY = 800
        print("ian")
     
    #player stay on the screen
    if playerX <= 0:
        playerX = 0
    if playerX >= 1568:
        playerX = 1568
                
                
    playerX += playerX_change 
    playerY += playerY_change           
    player(playerX, playerY)  #draw the player
    pygame.display.update()