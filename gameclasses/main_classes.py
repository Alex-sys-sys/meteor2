import pygame
import data
import random

pl = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/player.png')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pl
        self.rect = self.image.get_rect()
        self.rect.center = (data.screen.get_width() // 2, data.screen.get_height() - self.image.get_height() - 50)
        self.animation_count = 0
        self.animation_spis = [pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/'
                                                 'meteor2/images/player 2.png')]
        self.animation_spis.append(pygame.transform.flip(self.animation_spis[0], True, False))
        self.mask = pygame.mask.from_surface(self.image)
        self.cooldown = 0

    def update(self):
        if self.cooldown >= 1:
            self.cooldown -= 1
        self.mask = pygame.mask.from_surface(self.image)
        key = pygame.key.get_pressed()
        if len(pygame.sprite.spritecollide(self, data.allmeteors, False)) > 0:
            exit()
        if key[pygame.K_UP] or key[pygame.K_w]:
            if data.count < 5:
                self.image = self.animation_spis[0]
            elif data.count % 5 == 0:
                self.image = self.animation_spis[self.animation_count]
                self.animation_count = (self.animation_count + 1) % 2
            self.rect.y -= 6
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += 6
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 6
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 6
        if not (key[pygame.K_UP] or key[pygame.K_w]):
            self.image = pl
        if key[pygame.K_k] and self.cooldown == 0:
            bull = Bullet(9, (self.rect.x+30, self.rect.y))
            data.allsprites.add(bull)
            self.cooldown = 12


class Bullet(pygame.sprite.Sprite):
    def __init__(self, vel, coords):
        super().__init__()
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()
        self.velocity = vel
        self.rect.x, self.rect.y = coords[0], coords[1]

    def update(self):
        a = pygame.sprite.spritecollide(self, data.allmeteors, False)
        if len(a) >= 1:
            self.kill()
            pygame.sprite.spritecollide(self, data.allmeteors, False)
            a[0].killed = True
        self.rect.y -= self.velocity
        if self.rect.y < 0:
            self.kill()
