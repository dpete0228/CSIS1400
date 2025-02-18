import pygame, sys, math

def main():
    # Setup pygame
    pygame.init()

    # Define the screen
    screen_size = width, height = 600, 400
    screen = pygame.display.set_mode(screen_size)

    # Load image assets
    alien1 = pygame.image.load("alien1.png").convert_alpha()
    alien2 = pygame.image.load("alien2.png").convert_alpha()
    alien3 = pygame.image.load("alien3.png").convert_alpha()
    aliens = [alien1, alien2, alien3]
    alien_rect = alien1.get_rect()

    alien_rect.center = (width // 2, height // 2)

    # Create a clock to help compute a consistent framerate
    clock = pygame.time.Clock()

    # Main part of the game
    frame_number = 0
    is_playing = True
    # while loop
    while is_playing:# while is_playing is True, repeat

        # Check for events
        for event in pygame.event.get():
            # Stop loop if click on window close button
            if event.type == pygame.QUIT:
                is_playing = False
            # Check for a key press, and if they match the left or right arrow, move the rect.
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         alien_rect.move_ip(-5, 0)
            #     if event.key == pygame.K_RIGHT:
            #         alien_rect.move_ip(5, 0)

        # Set the alien to the mouse location
        # pos = pygame.mouse.get_pos()
        # alien_rect.center = pos

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            alien_rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT]:
            alien_rect.move_ip(5, 0)
        if keys[pygame.K_UP]:
            alien_rect.move_ip(0, -5)
        if keys[pygame.K_DOWN]:
            alien_rect.move_ip(0, 5)

        # Erase the screen with a background color
        screen.fill((0,100,50)) # fill the window with a color
        # Draw the alien
        screen.blit(aliens[int(frame_number)%3], alien_rect)
        # Bring all the changes to the screen into view
        pygame.display.update()
        # Set the frame rate
        clock.tick(30)

        frame_number += 0.1

    # Once the game loop is done, close the window and quit.
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()