import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load('background.png')

fighter_image = pygame.image.load('fighter.png')
fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

while True:
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        fighter.left -= 5
    elif pressed[pygame.K_RIGHT]:
        fighter.right += 5

    if fighter.left < 0:
        fighter.left = 0
    elif fighter.right > SCREEN_WIDTH:
        fighter.right = SCREEN_WIDTH

    screen.blit(fighter_image, fighter)

    pygame.display.update()
    clock.tick(30)

pygame.quit()