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
    screen.blit(background_image, (0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.blit(fighter_image, fighter)

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30)

pygame.quit()