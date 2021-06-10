import pygame
import sys
from random import randrange

pygame.init()
# display config
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Bot")

clock = pygame.time.Clock()

class player(object):
    def __init__(self):
        self.width, self.height = 20, 20
        self.x, self.y = None, None
        self.body, self.hit = [(randrange(1, 500, 20), randrange(1, 500, 20))], []
        self.point = 0
        self.font = pygame.font.SysFont('futura', 30, False, False)
        self.died = 0

    def draw(self):
        for (x, y) in self.body:
            pygame.draw.rect(win, (255, 255, 255), (x, y, self.width, self.height))

    def win_limit(self):
        if self.body[0][0] >= 500: self.body[0] = ((self.body[0][0] % 500) - 20, self.y)
        elif self.body[0][0] <= 0: self.body[0] = ((self.body[0][0] + 500) + 20, self.y)
        elif self.body[0][1] >= 500: self.body[0] = (self.x, self.body[0][1] % 500 - 20)
        elif self.body[0][1] <= 0: self.body[0] = (self.x, (self.body[0][1] + 500) + 20)

    def die(self):
        self.point = 0
        self.body.clear()
        self.body = [(randrange(1, 500, 20), randrange(1, 500, 20))]

class Food(object):
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y
        self.width, self.height = 20, 20

    def win_limit(self):
        if self.x >= 500: self.x, self.y = ((self.x % 500) - 20, self.y)
        elif self.x <= 0: self.x, self.y = ((self.x + 500) + 20, self.y)
        elif self.y >= 500: self.x, self.y = (self.x, self.y % 500 - 20)
        elif self.y <= 0: self.x, self.y = (self.x, (self.y + 500) + 20)

    def new_position(self):
        self.x, self.y = randrange(1, 500, 20), randrange(1, 500, 20)

    def draw(self):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))

snake = player()
food = Food()
food.new_position()
move = (0, 0)
food_move = (0, 0)

def redraw():
    win.fill((0, 0, 0))  # filling all of the previous movements

    food.draw()
    snake.draw()
    win.blit(snake.font.render('Points: ' + str(snake.point), True, (150, 150, 150)), (350, 0))

    pygame.display.update()

while 1:  # mainloop
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN: # processing user input
            snake.restart = True
            if event.key == pygame.K_UP: food_move = (0, -20)
            elif event.key == pygame.K_DOWN: food_move = (0, 20)
            elif event.key == pygame.K_LEFT: food_move = (-20, 0)
            elif event.key == pygame.K_RIGHT: food_move = (20, 0)

    if snake.body[0][1] > food.y: move = (0, -20)
    elif snake.body[0][1] < food.y: move = (0, 20)
    elif snake.body[0][0] > food.x: move = (-20, 0)
    elif snake.body[0][0] < food.x: move = (20, 0)

    snake.body[0] = (snake.body[0][0] + move[0], snake.body[0][1] + move[1])  # getting movements
    food.x, food.y = food.x + food_move[0], food.y + food_move[1]
    snake.body.insert(0, snake.body[0])  # constantly add more body
    snake.x, snake.y = snake.body[0][0], snake.body[0][1]

    if snake.body[0] == (food.x, food.y) or snake.body[0] == (food.x + 20, food.y) or snake.body[0] == (food.x, food.y + 20):
        food.new_position()
        if len(snake.body) >= 5:
            snake.point += 1
    else:
        if len(snake.body) >= 5:
            snake.body.pop()  # constantly deleting body, so its not visible

    snake.hit = snake.body[2:]  # separating the head and the body
    for i in range(len(snake.hit)):
        if snake.body[0] == snake.hit[i]:
            snake.died += 1

    snake.win_limit()
    food.win_limit()

    redraw()