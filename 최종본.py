import pygame
import random

pygame.init() #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



RED = (255, 0, 0)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
missed = 0
game_over = False

background_image = pygame.image.load('background.png')

rock_image = pygame.image.load('rock.png')
rocks = []
for i in range(3):
    rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
    dy = random.randint(3, 9)
    rocks.append((rock, dy))

missile_image = pygame.image.load('missile.png')
missiles = []

explosion_image = pygame.image.load('explosion.png')

fighter_image = pygame.image.load('fighter.png')
fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

pygame.mixer.init()
pygame.mixer.music.load('music.mid')
pygame.mixer.music.play(-1)
missile_sound = pygame.mixer.Sound('missile.wav')
explosion_sound = pygame.mixer.Sound('explosion.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

while True:
    screen.blit(background_image, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN and not game_over:
        if event.key == pygame.K_SPACE:
            missile = missile_image.get_rect(centerx=fighter.centerx, top=fighter.top)
            missiles.append(missile)
            missile_sound.play()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and not game_over:
        fighter.left -= 5
    elif pressed[pygame.K_RIGHT] and not game_over:
        fighter.left += 5

    if not game_over:
        for rock, dy in rocks:
            rock.top += dy
            if rock.top > SCREEN_HEIGHT:
                rocks.remove((rock, dy))
                rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
                dy = random.randint(3, 9)
                rocks.append((rock, dy))
                missed += 1

        if missed >= 5:
            game_over = True
            pygame.mixer.music.stop()
            game_over_sound.play()

        for missile in missiles:
            missile.top -= 6
            if missile.top < 0:
                missiles.remove(missile)

        if fighter.left < 0:
            fighter.left = 0
        elif fighter.right > SCREEN_WIDTH:
            fighter.right = SCREEN_WIDTH

        for rock, dy in rocks:
            for missile in missiles:
                if missile.colliderect(rock):
                    #print('bomp')
                    #print(rock)
                    #print(missile)
                    rocks.remove((rock, dy))
                    missiles.remove(missile)
                    screen.blit(explosion_image, (rock.left, rock.top))
                    rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
                    dy = random.randint(3, 9)
                    rocks.append((rock, dy))
                    score += 1
                    explosion_sound.play()

        for rock, dy in rocks:
            if rock.colliderect(fighter):
                #print('bomp')
                #print(rock)
                #print(fighter)
                game_over = True
                pygame.mixer.music.stop()
                game_over_sound.play()


    for rock, dy in rocks:
        screen.blit(rock_image, rock)

    for missile in missiles:
        screen.blit(missile_image, missile)

    screen.blit(fighter_image, fighter)

    score_image = small_font.render('Score {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))

    missed_image = small_font.render('Missed rock {}'.format(missed), True, YELLOW)
    screen.blit(missed_image, missed_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

    if game_over :
        game_over_image = large_font.render('Game Over', True, RED)
        screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(70)

pygame.quit()
