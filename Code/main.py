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

apple_color = (255, 0, 0)
apple_size = grid_size


def collision(x, y):
    return x < 0 or x >= screen_width or y < 0 or y >= screen_height

def death_screen():
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, ((screen_width - text.get_width()) // 2, (screen_height - text.get_height()) // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

def spawn_apple():
    x = random.randint(0, (screen_width - grid_size) // grid_size) * grid_size
    y = random.randint(0, (screen_height - grid_size) // grid_size) * grid_size
    return x, y

def draw_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Game loop ######################################################################
def game_loop():
    global player_x, player_y, direction
    running = True

    apple_x, apple_y = spawn_apple()
    score = 0

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

        if collision(player_x, player_y):
            death_screen()
            running = False
            continue

        if player_x == apple_x and player_y == apple_y:
            apple_x, apple_y = spawn_apple()
            score += 1
            # GROW SNAKE HERE

        pygame.draw.rect(screen, apple_color, (apple_x, apple_y, apple_size, apple_size))

        draw_score(score)

        screen.blit(player_image, (player_x, player_y))
        pygame.display.flip()

        clock.tick(10)

# End game loop ###################################################################

    pygame.quit()

game_loop()
