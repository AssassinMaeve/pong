import pygame, sys, random  # Import necessary modules

# Function to handle ball movement and collisions
def ballAnimation():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX  # Move ball in X direction
    ball.y += ballSpeedY  # Move ball in Y direction

    # Bounce off top and bottom walls
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    
    # Restart ball if it goes off the left or right side
    if ball.left <= 0 or ball.right >= screenWidth:
        ballRestart()
    
    # Bounce off player or opponent paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1

# Function to reset ball to the center after scoring
def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth / 2 , screenHeight / 2)  # Reset ball position
    ballSpeedY *= random.choice((1,-1))  # Randomize Y direction
    ballSpeedX *= random.choice((1,-1))  # Randomize X direction

# Function to handle player movement
def playerAnimation():
    player.y += playerSpeed  # Move player paddle
    
    # Prevent paddle from going off the screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

# Function for AI opponent movement
def opponentAi():
    # Move opponent towards the ball
    if opponent.top < ball.y - 10:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y + 10:
        opponent.bottom -= opponentSpeed
    
    # Prevent opponent from moving off the screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

# Screen dimensions
screenWidth = 1280
screenHeight = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Create game window
pygame.display.set_caption("Pong")  # Set window title

# Create game objects
ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15, 30, 30)  # Ball rectangle
player = pygame.Rect(screenWidth - 20, screenHeight/2 - 70, 10, 140)  # Player paddle
opponent = pygame.Rect(10, screenHeight/2 - 70, 10, 140)  # Opponent paddle

# Colors
bgColor = pygame.Color("grey12")  # Background color
lightGrey = (200, 200, 200)  # Paddle and ball color

# Speeds
ballSpeedX = 7 * random.choice((1,-1))  # Random initial X direction
ballSpeedY = 7 * random.choice((1,-1))  # Random initial Y direction
playerSpeed = 0  # Player speed starts at 0
opponentSpeed = 7  # Opponent speed

# Game loop
while True:
    for event in pygame.event.get():  # Event handling
        if event.type == pygame.QUIT:  # Check if player closes the window
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7  # Move player down
            if event.key == pygame.K_UP:
                playerSpeed -= 7  # Move player up
        
        # Handle key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7  # Stop moving down
            if event.key == pygame.K_UP:
                playerSpeed += 7  # Stop moving up

    # Update game elements
    ballAnimation()
    playerAnimation()
    opponentAi()
    player.y += playerSpeed  # Apply movement to player

    # Drawing elements
    screen.fill(bgColor)  # Clear screen
    pygame.draw.rect(screen, lightGrey, player)  # Draw player paddle
    pygame.draw.rect(screen, lightGrey, opponent)  # Draw opponent paddle
    pygame.draw.ellipse(screen, lightGrey, ball)  # Draw ball
    pygame.draw.aaline(screen, lightGrey, (screenWidth / 2, 0), (screenWidth / 2, screenHeight))  # Draw center line

    pygame.display.flip()  # Refresh the screen
    clock.tick(60)  # Maintain 60 FPS
