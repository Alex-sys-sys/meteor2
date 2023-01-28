import pygame
import data
import random
import math

pl = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/player.png')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pl
        self.rect = self.image.get_rect()
        self.rect.center = (data.screen.get_width() // 2, data.screen.get_height() - self.image.get_height() - 50)
        self.animation_count = 0
        # self.animation_spis = [pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/'
        #                                          'meteor2/images/player 2.png')]
        # self.animation_spis.append(pygame.transform.flip(self.animation_spis[0], True, False))
        # self.mask = pygame.mask.from_surface(self.image)
        self.cooldown = 0

    def update(self):
        self.image = pl
        katx = data.cursor[0] - self.rect.center[0]
        katy = data.cursor[1] - self.rect.center[1]
        angle = math.atan2(katy, katx)

        if self.cooldown >= 1:
            self.cooldown -= 1
        # self.mask = pygame.mask.from_surface(self.image)
        key = pygame.key.get_pressed()
        if len(pygame.sprite.spritecollide(self, data.allmeteors, False)) > 0:
            exit()
        # if key[pygame.K_UP] or key[pygame.K_w]:
        #     if data.count < 5:
        #         self.image = self.animation_spis[0]
        #     elif data.count % 5 == 0:
        #         self.image = self.animation_spis[self.animation_count]
        #         self.animation_count = (self.animation_count + 1) % 2
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += 9
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 9
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 9
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= 9
        if (key[pygame.K_k] and self.cooldown == 0) or (pygame.mouse.get_pressed()[0] is True and self.cooldown == 0):
            bull = Bullet(20, self.rect.center, angle)
            data.allsprites.add(bull)
            self.cooldown = 5
        self.image = pygame.transform.rotate(self.image, 360 - (math.degrees(angle) + 90))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, vel, coords, angle):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('images/bullet.png'), 270 - math.degrees(angle))
        self.rect = self.image.get_rect()
        self.velocity = vel
        self.rect.x, self.rect.y = coords[0], coords[1]
        self.vx = math.cos(angle) * self.velocity
        self.vy = math.sin(angle) * self.velocity

    def update(self):
        a = pygame.sprite.spritecollide(self, data.allmeteors, False)
        if len(a) >= 1:
            self.kill()
            pygame.sprite.spritecollide(self, data.allmeteors, False)
            a[0].killed = True
        self.rect.x += self.vx
        self.rect.y += self.vy
        if data.screen.get_height() < self.rect.y or self.rect.y < 0 or data.screen.get_width() < \
                self.rect.x or self.rect.x < 0:
            self.kill()
