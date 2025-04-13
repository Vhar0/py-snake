import pygame
import random
import os.path
import math
from pygame.locals import *
from Options import selection_loop as select


pygame.init()
clk = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 20)


class SnakeHead:
    X = 0
    Y = 0
    heads = []

    def __init__(self):
        self.n = pygame.image.load(os.path.join("res", "snake head N.png"))
        self.s = pygame.image.load(os.path.join("res", "snake head S.png"))
        self.w = pygame.image.load(os.path.join("res", "snake head W.png"))
        self.o = pygame.image.load(os.path.join("res", "snake head O.png"))
        self.last = 0
        self.heads = [self.n, self.o, self.s, self.w]
        self.c = (1, 1)

    def position(self, speed):
        if self.last == 0:
            return
        match self.last:                                                    # controllo quale tasto è stato premuto per ultimo
            case 1:
                self.Y -= speed                                             # se per es è stato premuto il pulsante W la funzione display assegnerà a last 1 e nel case 1 aumenterà la posizione del player
            case 2:
                self.X -= speed
            case 3:
                self.Y += speed
            case 4:
                self.X += speed

    def display(self, w, a, s, d, screen):                                  # (w a s d keys that have been pressed), (screen current screen), (x y current position where to display head)
        screen.blit(self.heads[self.last-1], (self.X, self.Y))

        if w:
            self.last = 1
        if a:
            self.last = 2
        if s:
            self.last = 3
        if d:
            self.last = 4

        return self.last

    def hit_box(self):
        self.rect = (self.X, self.Y, 100, 100)                              # just to print the hitbox as a rectangle
        return self.rect

    def collision(self):
        match self.last:
            case 1:                                                         # if the last button pressed was W (case 1) the starting point of the hitbox (hitbox_s) will be player pos X and player pos Y - 100 (100 = img lenght)
                self.c = (self.X+50, self.Y)
            case 2:
                self.c = (self.X, self.Y+50)
            case 3:
                self.c = (self.X+50, self.Y+100)
            case 4:
                self.c = (self.X+100, self.Y+50)
        return self.c

    def collision_detect(self, start, end):                                                     # detects collision based on last pressed button (hitbox self start(starting point of snake hitbox), start(starting point of apple hitbox)
        if (start[0] <= self.c[0] <= end[0]) and (start[1] <= self.c[1] <= end[1]):             # controls if the n point of the snake head is between the two collision points of the fruit
            return True
        else:
            return False

class Food:

    def __init__(self):
        self.image = pygame.image.load(os.path.join("res", "fruit.png"))       # load food
        self.hitbox_s = (0, 0)
        self.hitbox_e = (0, 0)

    def hit_box(self, x, y):
        self.rect = (x, y, 100, 100)

        return self.rect

    def collision(self, x, y, key):                                         # custom collision detection (obj pos x & y, last pressed key)
        match key:                                                          # the collision points on the fruit will be tho opposite of the snake head becous the
            case 1:
                self.hitbox_s = (x, y+100)
                self.hitbox_e = (x+100, y+100)
            case 2:
                self.hitbox_s = (x+100, y)
                self.hitbox_e = (x+100, y+100)
            case 3:
                self.hitbox_s = (x, y)
                self.hitbox_e = (x+100, y)
            case 4:
                self.hitbox_s = (x, y)
                self.hitbox_e = (x, y+100)
        return self.hitbox_s, self.hitbox_e


def main_game_loop():
    select()

    snake = SnakeHead()

    pygame.font.init()
    # keyW = font.render("W Key was pressed", False, (0, 0, 0))
    # keyA = font.render("A Key was pressed", False, (0, 0, 0))
    # keyS = font.render("S Key was pressed", False, (0, 0, 0))
    # keyD = font.render("D Key was pressed", False, (0, 0, 0))

    X = select()[0]
    Y = select()[1]

    color = (255, 255, 255)                                                 # red colour for the hitbox square

    random.seed()
    obj_X = random.randint(0, X)                                            # genera un numero pseudo-randomico nel range da 0 a X o Y (screen limit)
    obj_Y = random.randint(0, Y)                                            # ||
    #obj_Y *= 100
    #obj_X *= 100
    counter = 0
    speed = 1

    playerX = X/2                                                           # faccio partire il p dal centro
    playerY = Y/2

    screen = pygame.display.set_mode((X, Y))
    pygame.display.init()
    pygame.display.set_caption("SNAKE GAME")

    test = pygame.image.load(os.path.join("res", "snake.jpg"))

    apple = Food()

    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True
            w = pygame.key.get_pressed()[K_w]                               # w key
            a = pygame.key.get_pressed()[K_a]                               # a key
            s = pygame.key.get_pressed()[K_s]                               # s key
            d = pygame.key.get_pressed()[K_d]                               # d key
            back = pygame.key.get_pressed()[K_BACKSPACE]                    # backspace key for spawn reset

        screen.fill((255, 255, 255))                                        # coloro il background di bianco

        # screen.blit(snake_head_N, (playerX, playerY))                     # img test

        snake.display(w, a, s, d, screen=screen)

        snake.position(speed=speed)

        pygame.draw.rect(screen, color, apple.hit_box(obj_X, obj_Y), 5)     # initialize apple hitbox
        pygame.draw.rect(screen, color, snake.hit_box(), 5)                 # initialize snake hitbox

        playerX = snake.X
        playerY = snake.Y

        pos = font.render("(" + str(round(obj_X)) + ";" + str(round(obj_Y)) + ")", False, (0, 0, 0))
        screen.blit(pos, (X-100, 0))

        Ppos = font.render("(" + str(playerX) + ";" + str(playerY) + ")", False, (0, 0, 0))
        screen.blit(Ppos, (X-100, 50))

        hit = font.render("snake hitpoints: (" + str(round(snake.collision()[0])) + " ; " + str(round(snake.collision()[1])) + ")", False, (0, 0, 0))
        screen.blit(hit, (0, 0))

        hit2 = font.render("Food hitpoints: (" + str(apple.collision(obj_X, obj_Y, snake.last)[0]) + " ; " + str(apple.collision(obj_X, obj_Y, snake.last)[1]) + ")", False, (0, 0, 0))
        screen.blit(hit2, (0, 50))

        stats = font.render("POINTS: " + str(counter), False, (0, 0, 0))
        screen.blit(stats, (X/2-50, 0))
        # logica gioco

        screen.blit(apple.image, (obj_X, obj_Y))

        if back:
            obj_X = X/2
            obj_Y = Y/2

        if snake.collision_detect(apple.collision(obj_X, obj_Y, snake.last)[0], apple.collision(obj_X, obj_Y, snake.last)[1]):                     # controls if two rects are colliding (ref -> snake.collision_detect)
            counter += 1
            #speed += counter
            snake.position(speed)                                                   # conto quando tocca un obj del campo per aumentare la velocità
            obj_X = random.randint(0, X)
            obj_Y = random.randint(0, Y)
        # snake rotation

        #pacman effect:
        if snake.X > X:
            snake.X = 0
        if snake.Y > Y:
            snake.Y = 0
        if snake.X < 0:
            snake.X = X
        if snake.Y < 0:
            snake.Y = Y


        pygame.display.flip()

        clk.tick(60)
