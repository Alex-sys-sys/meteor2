import pygame
import data
import random

planet1 = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/background/planet1.png')
planet2 = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/background/planet2.png')
planet3 = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/background/planet3.png')
planet4 = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/background/planet4.png')
met1 = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/background/meteor1.png')
star = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/background/star.png')


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice([planet1, planet2, planet3, planet4])
        self.rect = self.image.get_rect()
        self.rect.y = 1522
        self.rect.x = 15
        self.rect.center = (random.randrange(0, data.screen.get_size()[0]), -self.image.get_size()[1])
        self.vel = random.randrange(1, 4)
        self.spin = random.randrange(40, 50)

    def update(self):
        self.rect.y += self.vel
        if self.rect.bottom > 1000:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(met1, random.randrange(0, 360))
        self.rect = self.image.get_rect()
        self.rect.y = 15
        self.rect.x = 15
        self.rect.center = (random.randrange(0, data.screen.get_size()[1]), -self.image.get_size()[1])
        self.mask = pygame.mask.from_surface(self.image)
        self.count = 0
        self.killed = False

    def update(self):
        if self.killed is False:
            self.rect.y += 4
            if self.rect.bottom > 1000:
                self.kill()
        else:
            self.count += 1
            if self.count < 5:
                self.image = pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/explosion.png')
            elif (5 < self.count) and (self.count < 13):
                self.image = pygame.transform.flip(
                    pygame.image.load('/Users/aleksejerofeev/venv/pythonProject/meteor2/images/explosion.png'),
                    flip_x=False, flip_y=True)
            elif self.count > 13:
                self.kill()


class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(star, random.randrange(0, 360))
        self.rect = self.image.get_rect()
        self.rect.y = 15
        self.rect.x = 15
        self.rect.center = (random.randrange(0, data.screen.get_size()[0]), -self.image.get_size()[1])
        self.vel = random.randrange(1, 3)

    def update(self):
        self.rect.y += self.vel
        if self.rect.bottom > 1000:
            self.kill()
