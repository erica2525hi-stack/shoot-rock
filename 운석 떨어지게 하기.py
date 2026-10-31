import pygame
import random

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load('background.png')

rock_image = pygame.image.load('rock.png')
rocks = []
for i in range(3):
    rock = rock_image.get_rect(left=(i + 1) * 100, top=(i + 1) * 100)
    rocks.append(rock)

fighter_image = pygame.image.load('fighter.png')
fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

while True:
    screen.blit(background_image, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        fighter.left -= 5
    elif pressed[pygame.K_RIGHT]:
        fighter.right += 5

    for rock in rocks:
        rock.top += 3

    if fighter.left < 0:
        fighter.left = 0
    elif fighter.right > SCREEN_WIDTH:
        fighter.right = SCREEN_WIDTH

    for rock in rocks:
        screen.blit(rock_image, rock)

    screen.blit(fighter_image, fighter)

    pygame.display.update()
    clock.tick(30)

pygame.quit()