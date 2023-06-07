import pygame
import random


def draw(screen):
    for i in range(10000):
        screen.fill(pygame.Color('red'), (random.random() * width, random.random() * height, 1, 1))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

draw(screen)
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()