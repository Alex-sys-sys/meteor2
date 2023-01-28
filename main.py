import pygame
import random
import data
from gameclasses.background_classes import Meteor, Planet, Star
from gameclasses.main_classes import Player

fps = 20
pygame.init()
pygame.font.init()

pygame.display.set_caption("Unusual Game")
clock = pygame.time.Clock()
run = True

font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 70)
player = Player()

while run:
    data.count += 1
    if data.count % 20 == 0:
        st = Star()
        data.allsprites.add(st)
    if data.count % 200 == 0:
        pl = Planet()
        data.allsprites.add(pl)
    if data.count % 40 == 0:
        mt = Meteor()
        data.allsprites.add(mt)
        data.allmeteors.add(mt)
    pygame.time.Clock().tick(fps)
    data.screen.fill((10, 7, 1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    data.cursor = pygame.mouse.get_pos()
    data.allsprites.update()
    data.allsprites.draw(data.screen)
    player.update()
    data.screen.blit(player.image, player.rect)
    pygame.display.update()
pygame.quit()
