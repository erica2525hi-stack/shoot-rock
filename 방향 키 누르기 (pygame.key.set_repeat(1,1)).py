import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

background_image = pygame.image.load('background.png')

fighter_image = pygame.image.load('fighter.png')
fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

while True:
    screen.blit(background_image, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            fighter.left -= 5
        elif event.key == pygame.K_RIGHT:
            fighter.right += 5

    screen.blit(fighter_image, fighter)

    pygame.display.update()
    clock.tick(30)

pygame.quit()