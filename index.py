import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1v1 Gun Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 60
PLAYER_VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 5

# Define players
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.bullets = []
        self.health = 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        for bullet in self.bullets:
            pygame.draw.rect(win, self.color, bullet)

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.x += BULLET_VEL if self.color == RED else -BULLET_VEL
            if bullet.x < 0 or bullet.x > WIDTH:
                self.bullets.remove(bullet)

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    red_player = Player(100, HEIGHT // 2, RED)
    blue_player = Player(WIDTH - 150, HEIGHT // 2, BLUE)

    def draw_window():
        WIN.fill(WHITE)
        red_player.draw(WIN)
        blue_player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_player.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_player.x + PLAYER_WIDTH, red_player.y + PLAYER_HEIGHT // 2, 10, 5)
                    red_player.bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(blue_player.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue_player.x, blue_player.y + PLAYER_HEIGHT // 2, 10, 5)
                    blue_player.bullets.append(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and red_player.x - PLAYER_VEL > 0:
            red_player.x -= PLAYER_VEL
        if keys[pygame.K_d] and red_player.x + PLAYER_VEL + PLAYER_WIDTH < WIDTH:
            red_player.x += PLAYER_VEL
        if keys[pygame.K_w] and red_player.y - PLAYER_VEL > 0:
            red_player.y -= PLAYER_VEL
        if keys[pygame.K_s] and red_player.y + PLAYER_VEL + PLAYER_HEIGHT < HEIGHT:
            red_player.y += PLAYER_VEL

        if keys[pygame.K_LEFT] and blue_player.x - PLAYER_VEL > 0:
            blue_player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and blue_player.x + PLAYER_VEL + PLAYER_WIDTH < WIDTH:
            blue_player.x += PLAYER_VEL
        if keys[pygame.K_UP] and blue_player.y - PLAYER_VEL > 0:
            blue_player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and blue_player.y + PLAYER_VEL + PLAYER_HEIGHT < HEIGHT:
            blue_player.y += PLAYER_VEL

        red_player.move_bullets()
        blue_player.move_bullets()

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
