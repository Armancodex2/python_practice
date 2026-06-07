import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 35)


def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])


def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [180, 250])


game_over = False
game_close = False

x1 = WIDTH / 2
y1 = HEIGHT / 2

x1_change = 0
y1_change = 0

snake_list = []
length = 1

foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

while not game_over:

    while game_close:
        screen.fill(black)
        message("You Lost! Press Q-Quit or C-Play Again", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False

                if event.key == pygame.K_c:
                    game_over = False
                    game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0

            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0

            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0

            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        game_close = True

    x1 += x1_change
    y1 += y1_change

    screen.fill(black)

    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    snake_list.append(snake_head)

    if len(snake_list) > length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    draw_snake(snake_block, snake_list)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
        foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
        length += 1

    clock.tick(snake_speed)

pygame.quit()
