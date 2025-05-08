import pygame
import random

pygame.init()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()

player_image = pygame.image.load("solidsnake.webp")
player_image = pygame.transform.scale(player_image, (50, 50))

player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Game loop ######################################################################
def game_loop():
    global player_x, player_y
    running = True

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        screen.blit(player_image, (player_x, player_y))

        pygame.display.flip()
        clock.tick(60)

# End game loop ###################################################################

    pygame.quit()

game_loop()
