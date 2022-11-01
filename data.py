import pygame

width, height = 0, 0
screen = pygame.display.set_mode((width, height))
allsprites = pygame.sprite.Group()
allmeteors = pygame.sprite.Group()
count = 0

pygame.display.set_icon(pygame.image.load('/images/background/planet1.png'))
