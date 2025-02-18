import pygame, sys, math

# Setup pygame
pygame.init()

# Define the screen
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

# Load image assets
ball = pygame.image.load("GolfBall.png").convert_alpha()
ball_rect = ball.get_rect()

# Create a clock to help compute a consistent framerate
clock = pygame.time.Clock()

# Main part of the game
is_playing = True
while is_playing:  # while is_playing is True, repeat
    # Check for events
    for event in pygame.event.get():
        # Stop loop if click on window close button
        if event.type == pygame.QUIT:
            is_playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_rect.move_ip(-5, 0)
            if event.key == pygame.K_RIGHT:
                ball_rect.move_ip(5, 0)
            if event.key == pygame.K_UP:
                ball_rect.move_ip(0, -5)
            if event.key == pygame.K_DOWN:
                ball_rect.move_ip(0, 5)


    pos = pygame.mouse.get_pos()
    ball_rect.center = pos
    # Erase the screen with a background color
    screen.fill((0,100,50)) # fill the window with a color
    # Draw the ball where the rect is
    screen.blit(ball, ball_rect)
    # Bring all the changes to the screen into view
    pygame.display.update()
    # Set a maximum framerate of 60 frames per second
    clock.tick(60)

# Once the game loop is done, close the window and quit.
pygame.quit()
sys.exit()