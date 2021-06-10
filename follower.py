import pygame
from random import randrange
import sys
pygame.init()

# display config
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Stalk')
clock = pygame.time.Clock()

class player(object):
    def __init__(self):
        self.x, self.y = randrange(0, 500, 20), randrange(0, 500, 20)

    def win_limit(self):
        if self.x >= 500:
            self.x = 0
        elif self.x <= 0:
            self.x = 500
        elif self.y >= 500:
            self.y = 0
        elif self.y <= 0:
            self.y = 500

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, 20, 20))

class stalk(object):
    def __init__(self):
        self.x, self.y = randrange(0, 500, 20), randrange(0, 500, 20)
        self.speed = 10

    def follow(self, px, py):
        if self.y > py: self.y -= self.speed
        elif self.y < py: self.y += self.speed
        elif self.x > px: self.x -= self.speed
        elif self.x < px: self.x += self.speed
        else: print("hit")

    def follow1(self, px, py):
        if self.x != px and self.y != py:
            self.x += 1

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 20, 20))

user = player()
stalks = stalk()
move = (0, 0)

while 1:
    clock.tick(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP: user.y -= 20
            elif events.key == pygame.K_DOWN: user.y += 20
            elif events.key == pygame.K_LEFT: user.x -= 20
            elif events.key == pygame.K_RIGHT: user.x += 20

    stalks.follow(user.x, user.y)
    user.win_limit()

    pygame.display.update()
    win.fill((0, 0, 0))

    user.draw()
    stalks.draw()