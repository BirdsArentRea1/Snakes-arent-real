import pygame
import random

pygame.init()

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()

player_image = pygame.image.load("solidsnake.webp")
player_image = pygame.transform.scale(player_image, (50, 50))

grid_size = 50
direction = 0

player_x = screen_width // 2
player_y = screen_height // 2
direction = (0, 0)

# Game loop ######################################################################
def game_loop():
    global player_x, player_y, direction
    running = True

    while running:  
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = (-grid_size, 0)
        elif keys[pygame.K_RIGHT]:
            direction = (grid_size, 0)
        elif keys[pygame.K_UP]:
            direction = (0, -grid_size)
        elif keys[pygame.K_DOWN]:
            direction = (0, grid_size)
        else:
            direction = (0, 0) 
            
        player_x += direction[0]
        player_y += direction[1]

        screen.blit(player_image, (player_x, player_y))
        pygame.display.flip()

        clock.tick(10)

# End game loop ###################################################################

    pygame.quit()

game_loop()
