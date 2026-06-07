import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

font = pygame.font.SysFont("Consolas", 20)
chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

drops = [0 for _ in range(WIDTH // 20)]

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(drops)):
        text = font.render(random.choice(chars), True, (0, 255, 0))
        x = i * 20
        y = drops[i] * 20

        screen.blit(text, (x, y))

        if y > HEIGHT and random.random() > 0.975:
            drops[i] = 0

        drops[i] += 1

    pygame.display.update()

pygame.quit()
