#FproProj
import pygame


pygame.init()



screen = pygame.display.set_mode((1600,900))

pygame.display.set_caption("Flicky")
icon = pygame.image.load("D:/GitHub/FproProj/img/bird.png")
pygame.display.set_icon(icon)
background = pygame.image.load("D:/GitHub/FproProj/img/corte1.png")

#player while i dont realize how to use sheets
playerimg = pygame.image.load("D:/GitHub/FproProj/img/bird.png")
playerX = 20
playerY = 808
playerX_change = 0
clock = pygame.time.Clock()

def player(x,y):
    screen.blit(playerimg,(x, y))

#Game loop
running = True
isJump = False
jumpcount = 15
while running:   
    clock.tick(60)
    screen.fill((0,255,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Close window           
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT and playerX_change == 0:     #movement 
                playerX_change -= 10              
            if event.key == pygame.K_RIGHT and playerX_change == 0:
                playerX_change += 10
            
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change = 0     
        
        
    keys = pygame.key.get_pressed()
    if not isJump:
        if keys[pygame.K_UP]:  #Provisory jump
                isJump = True
    else:
        if jumpcount >= -15:
            neg = 1
            if jumpcount < 0:
                neg = -1
            playerY -= (jumpcount ** 2) /5 * neg
            jumpcount -= 1
        else:
            isJump = False
            jumpcount = 15 
                   
    
    
                      
    
        
     
    #player stay on the screen
    if playerX <= 0:
        playerX = 0
    if playerX >= 1568:
        playerX = 1568
                
                
    playerX += playerX_change               
    player(playerX, playerY)  #draw the player
    pygame.display.update()