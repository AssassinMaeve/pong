import pygame, sys, random

def ballAnimation():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX
    ball.y += ballSpeedY 

    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= screenWidth:
        ballRestart()
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1

def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth / 2 , screenHeight / 2)
    ballSpeedY *= random.choice((1,-1))
    ballSpeedX *= random.choice((1,-1))

def playerAnimation():
    player.y += playerSpeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def opponentAi():
    if opponent.top < ball.y - 10:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y + 10:
        opponent.bottom -= opponentSpeed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1280
screenHeight = 960
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pong")


ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30, 30)
player = pygame.Rect(screenWidth - 20, screenHeight/2 - 70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2 - 70, 10, 140)

bgColor = pygame.Color("grey12")
lightGrey = (200, 200, 200)

ballSpeedX = 7 * random.choice((1,-1))
ballSpeedY = 7 * random.choice((1,-1))
playerSpeed = 0
opponentSpeed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7


    ballAnimation()
    playerAnimation()
    opponentAi()
    player.y += playerSpeed


    screen.fill(bgColor)
    pygame.draw.rect(screen,lightGrey,player)
    pygame.draw.rect(screen,lightGrey,opponent)
    pygame.draw.ellipse(screen,lightGrey,ball)
    pygame.draw.aaline(screen, lightGrey, (screenWidth / 2,0), (screenWidth / 2,screenHeight))



    pygame.display.flip()
    clock.tick(60)