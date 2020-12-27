#FproProj
import pygame


pygame.init()

screen = pygame.display.set_mode((1600,900))

pygame.display.set_caption("Flicky")
icon = pygame.image.load("D:/GitHub/FproProj/img/bird.png")
pygame.display.set_icon(icon)
background = pygame.image.load("D:/GitHub/FproProj/img/corte1.png")

#need to find the images of the movement
walkRight = [pygame.image.load('img/bird.png'), pygame.image.load('img/bird.png'), 
             pygame.image.load('img/bird.png'), pygame.image.load('img/bird.png'), 
             pygame.image.load('img/bird.png'), pygame.image.load('img/bird.png')]
walkLeft = [pygame.image.load('img/bird.png'), pygame.image.load('img/bird.png'), 
            pygame.image.load('img/bird.png'), pygame.image.load('img/bird.png'), 
            pygame.image.load('img/bird.png'), pygame.image.load('img/bird.png')]
playeridle = pygame.image.load("img/bird.png")


playerX = 20
playerY = 808
playerX_change = 0
clock = pygame.time.Clock()
left = False
right = False
isJump = False
walkcount = 0

def draw():
    global walkcount
    screen.blit(background,(0,0))
    screen.blit(playeridle,(playerX, playerY))
    if walkcount + 1 >= 30:
        walkcount = 0       
    if left:  
        screen.blit(walkLeft[walkcount//5], (playerX,playerY))
        walkcount += 1                          
    elif right:
        screen.blit(walkRight[walkcount//5], (playerX,playerY))
        walkcount += 1
    else:
        screen.blit(playeridle, (playerX, playerY))
        walkcount = 0
    pygame.display.update()

    
#Game loop
running = True
jumpcount = 15
while running:   
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Close window           
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:     #movement 
                playerX_change = -10
                left = True
                right = False
            elif event.key == pygame.K_RIGHT:            
                playerX_change = 10
                right = True
                left = False
            
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT:
                  playerX_change = 0     
                  left = False
                  walkcount = 0
              if event.key == pygame.K_RIGHT:
                  playerX_change = 0
                  right = False
                  walkcount = 0
        
    playerX += playerX_change
        
    keys = pygame.key.get_pressed()
    if not isJump:
        if keys[pygame.K_UP]:  #jump
                isJump = True
                right = False
                left = False
                walkcount = 0
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
        
    draw()
                
                
                  
    
    