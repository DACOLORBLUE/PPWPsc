import pygame
import sys
import random
import math

# Setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bullet Hell - Deltarune Style (Pygame)")
clock = pygame.time.Clock()
FPS = 60

# Colors
DARKGRAY = (40, 40, 40)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Play area (outline only)
play_area = pygame.Rect(100, 100, 600, 400)

# Player
player_pos = pygame.Vector2(screen_width / 2, screen_height / 2)
player_radius = 10
player_speed = 3.5

# Bullets
bullets = []
bullet_radius = 8
bullet_spawn_timer = 0
bullet_spawn_delay = 0.2  # seconds

def check_collision(a, r1, b, r2):
    return a.distance_to(b) < (r1 + r2)

def spawn_bullet():
    # Spawn from one of 4 edges of the play area
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    if edge == 'top':
        x = random.uniform(play_area.left, play_area.right)
        y = play_area.top
        vx, vy = 0, random.uniform(1.5, 3)
    elif edge == 'bottom':
        x = random.uniform(play_area.left, play_area.right)
        y = play_area.bottom
        vx, vy = 0, random.uniform(-3, -1.5)
    elif edge == 'left':
        x = play_area.left
        y = random.uniform(play_area.top, play_area.bottom)
        vx, vy = random.uniform(1.5, 3), 0
    else:  # right
        x = play_area.right
        y = random.uniform(play_area.top, play_area.bottom)
        vx, vy = random.uniform(-3, -1.5), 0

    bullets.append({
        "pos": pygame.Vector2(x, y),
        "vel": pygame.Vector2(vx, vy),
        "radius": bullet_radius
    })

# Game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000  # Time delta in seconds
    bullet_spawn_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: player_pos.x += player_speed
    if keys[pygame.K_LEFT]:  player_pos.x -= player_speed
    if keys[pygame.K_DOWN]:  player_pos.y += player_speed
    if keys[pygame.K_UP]:    player_pos.y -= player_speed

    # Clamp to play area
    player_pos.x = max(play_area.left + player_radius, min(player_pos.x, play_area.right - player_radius))
    player_pos.y = max(play_area.top + player_radius, min(player_pos.y, play_area.bottom - player_radius))

    # Spawn bullets
    if bullet_spawn_timer >= bullet_spawn_delay:
        spawn_bullet()
        bullet_spawn_timer = 0

    # Update bullets
    for bullet in bullets:
        bullet["pos"] += bullet["vel"]

    # Collision detection
    for bullet in bullets:
        if check_collision(player_pos, player_radius, bullet["pos"], bullet["radius"]):
            pygame.quit()
            sys.exit()

    # Draw
    screen.fill(DARKGRAY)

    # Draw green play area outline (thick)
    pygame.draw.rect(screen, GREEN, play_area, width=6)

    # Draw player
    pygame.draw.circle(screen, RED, (int(player_pos.x), int(player_pos.y)), player_radius)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (int(bullet["pos"].x), int(bullet["pos"].y)), bullet["radius"])

    pygame.display.flip()

pygame.quit()
sys.exit()