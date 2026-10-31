import pygame
import random

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

Yellow = (255, 255, 0)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
missed = 0

background_image = pygame.image.load('background.png')

rock_image = pygame.image.load('rock.png')
rocks = []
for i in range(3):
    rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
    rocks.append(rock)

missile_image = pygame.image.load('missile.png')
missiles = []

explosion_image = pygame.image.load('explosion.png')

fighter_image = pygame.image.load('fighter.png')
fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

while True:
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            missile = missile_image.get_rect(centerx=fighter.centerx, top=fighter.top)
            missiles.append(missile)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        fighter.left -= 5
    elif pressed[pygame.K_RIGHT]:
        fighter.left += 5

    for rock in rocks:
        rock.top += 3
        if rock.top > SCREEN_HEIGHT:
            rocks.remove(rock)
            rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
            rocks.append(rock)
            missed += 1

    for missile in missiles:
        missile.top -= 6
        if missile.top < 0:
            missiles.remove(missile)

    if fighter.left < 0:
        fighter.left = 0
    elif fighter.right > SCREEN_WIDTH:
        fighter.right = SCREEN_WIDTH

    for rock in rocks:
        for missile in missiles:
            if missile.colliderect(rock):
                rocks.remove(rock)
                missiles.remove(missile)
                screen.blit(explosion_image, (rock.left, rock.top))
                rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
                rocks.append(rock)
                score += 1


    for rock in rocks:
        screen.blit(rock_image, rock)

    for missile in missiles:
        screen.blit(missile_image, missile)

    screen.blit(fighter_image, fighter)

    score_image = small_font.render('score {}'.format(score), True, Yellow)
    screen.blit(score_image, (10, 10))

    missed_image = small_font.render('no.missed rock {}'.format(missed), True, Yellow)
    screen.blit(missed_image, missed_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

    pygame.display.update()
    clock.tick(100)

pygame.quit()