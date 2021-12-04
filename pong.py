import pygame, sys, random
from pygame.event import wait
from pygame.locals import *
from pygame.constants import QUIT

pygame.init()

size = width, height = 600, 550
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.display.set_caption("Test")

BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (86, 232, 125)
WHITE = (255, 255, 255)
background = BLACK

leftpaddle = Rect(10, height/3, 15, height/5)
rightpaddle = Rect(width-25, height/3, 15, height/5)
ball = Rect(width/2, height/2, 20, 20)
ballMovement = (random.randrange(1), random.randrange(1))

dirx = {K_LEFT:-1, K_RIGHT:1}
diry = {K_UP:-1, K_DOWN:1}
v = [0,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
        if event.type == KEYDOWN:
            if event.key in dirx:
                v[0] +=dirx[event.key]
            if event.key in diry:
                v[1] +=diry[event.key]
                
    ball.x += v[0]
    ball.y += v[1]
    
    if ball.bottom > height:
        v[1] = -v[1]
    if ball.top < 0:
        v[1] = -v[1]
    if ball.left < 0:
        ball.x = width/2
        ball.y = height/2
        v[0] = 0
        v[1] = 0
        wait(300)
        v = [random.choice([-1, 1]), random.choice([-1, 1])]
    if ball.right > width:
        ball.x = width/2
        ball.y = height/2
        v[0] = 0
        v[1] = 0
        wait(300)
        v = [random.choice([-1, 1]), random.choice([-1, 1])]
    if ball.left < leftpaddle.right and ball.bottom > leftpaddle.top and ball.top < leftpaddle.bottom:
        v[0] = -v[0]
    if ball.right > rightpaddle.left and ball.bottom > rightpaddle.top and ball.top < rightpaddle.bottom:
        v[0] = -v[0]
    
    clock.tick(60)
    screen.fill (background)
    pygame.draw.ellipse(screen, GREEN, ball)
    pygame.draw.rect(screen,WHITE, leftpaddle)
    pygame.draw.rect(screen,WHITE, rightpaddle)
    pygame.display.update()