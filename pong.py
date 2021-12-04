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

rightpaddlekeys = {K_UP:-3, K_DOWN:3}
leftpaddlekeys = {K_w:-3, K_s:3}
ballmovement = [random.choice([-2, 2]), random.choice([-2, 2])]
leftpaddlemovement = 0
rightpaddlemovement = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == KEYDOWN:
            if event.key in rightpaddlekeys:
                rightpaddlemovement = rightpaddlekeys[event.key]
            if event.key in leftpaddlekeys:
                leftpaddlemovement = leftpaddlekeys[event.key]
        if event.type == KEYUP:
            if event.key in rightpaddlekeys:
                rightpaddlemovement = 0
            if event.key in leftpaddlekeys:
                leftpaddlemovement = 0
                
    if rightpaddle.top < 0:
        rightpaddlemovement = 0
        rightpaddle.y = 0
    if rightpaddle.bottom > height:
        rightpaddlemovement = 0
        rightpaddle.y = height - height/5

    if leftpaddle.top < 0:
        leftpaddlemovement = 0
        leftpaddle.y = 0
    if leftpaddle.bottom > height:
        leftpaddlemovement = 0
        leftpaddle.y = height - height/5

    if ball.bottom > height:
        ballmovement[1] = -ballmovement[1]
    if ball.top < 0:
        ballmovement[1] = -ballmovement[1]
    if ball.left < 0:
        ball.x = width/2
        ball.y = height/2
        ballmovement[0] = 0
        ballmovement[1] = 0
        wait(300)
        ballmovement = [random.choice([-2, 2]), random.choice([-2, 2])]
    if ball.right > width:
        ball.x = width/2
        ball.y = height/2
        ballmovement[0] = 0
        ballmovement[1] = 0
        wait(300)
        ballmovement = [random.choice([-2, 2]), random.choice([-2, 2])]
    if ball.left < leftpaddle.right and ball.bottom > leftpaddle.top and ball.top < leftpaddle.bottom:
        ballmovement[0] = -ballmovement[0]
    if ball.right > rightpaddle.left and ball.bottom > rightpaddle.top and ball.top < rightpaddle.bottom:
        ballmovement[0] = -ballmovement[0]
    
    ball.x += ballmovement[0]
    ball.y += ballmovement[1]
    rightpaddle.y += rightpaddlemovement
    leftpaddle.y += leftpaddlemovement

    clock.tick(60)
    screen.fill (background)
    pygame.draw.rect(screen, (100, 100, 100), (width/2, 0, 10, height))
    pygame.draw.ellipse(screen, GREEN, ball)
    pygame.draw.rect(screen,WHITE, leftpaddle)
    pygame.draw.rect(screen,WHITE, rightpaddle)
    pygame.display.update()