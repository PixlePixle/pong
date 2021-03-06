import pygame, sys, random #imports stuff
from pygame.event import wait
from pygame.locals import *
from pygame.constants import QUIT
#initalizes pygame
pygame.init()
#Creates the screen
size = width, height = 600, 550
screen = pygame.display.set_mode(size)
#Clock, updates per second?
clock = pygame.time.Clock()
#Window title
pygame.display.set_caption("Pong ❤️")

#colours
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (86, 232, 125)
WHITE = (255, 255, 255)
background = BLACK

#creating the objects
leftpaddle = Rect(10, height//3, 15, height//5)
rightpaddle = Rect(width-25, height//3, 15, height//5)
ball = Rect(width//2, height//2, 20, 20)

leftScore = 0
rightScore = 0
font = pygame.font.Font("freesansbold.ttf", 32)

speedMult = 1.02

#dictionaries for movement
rightpaddlekeys = {K_UP:-4, K_DOWN:4}
leftpaddlekeys = {K_w:-4, K_s:4}

#velocity stuff
ballmovement = [random.choice([-2, 2]), random.choice([-2, 2])]
leftpaddlemovement = 0
rightpaddlemovement = 0

#Game Loop
while True:
    #Input chunk
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
    #Stops right paddle from going beyond screen
    if rightpaddle.top < 0:
        rightpaddlemovement = 0
        rightpaddle.y = 0
    if rightpaddle.bottom > height:
        rightpaddlemovement = 0
        rightpaddle.y = height - height/5
    #Stops left paddle from going beyond screen
    if leftpaddle.top < 0:
        leftpaddlemovement = 0
        leftpaddle.y = 0
    if leftpaddle.bottom > height:
        leftpaddlemovement = 0
        leftpaddle.y = height - height/5
    #If the ball hits the top or bottom of the screen, inverse the y velocity
    if ball.bottom > height:
        ballmovement[1] = -ballmovement[1]
    if ball.top < 0:
        ballmovement[1] = -ballmovement[1]
    #If the ball hits the left or right side of the screen, reset
    if ball.left < 0:
        ball.x = width/2
        ball.y = height/2
        ballmovement[0] = 0
        ballmovement[1] = 0
        wait(300)
        rightScore += 1
        ballmovement = [random.choice([-2, 2]), random.choice([-2, 2])]
    if ball.right > width:
        ball.x = width/2
        ball.y = height/2
        ballmovement[0] = 0
        ballmovement[1] = 0
        wait(300)
        leftScore += 1
        ballmovement = [random.choice([-2, 2]), random.choice([-2, 2])]
    #If the ball hits the paddle, bounce off
    if ball.left < leftpaddle.right and ball.bottom > leftpaddle.top and ball.top < leftpaddle.bottom:
        ballmovement[0] = -(ballmovement[0] * speedMult)
        ball.x += 2
    if ball.right > rightpaddle.left and ball.bottom > rightpaddle.top and ball.top < rightpaddle.bottom:
        ballmovement[0] = -(ballmovement[0] * speedMult)
        ball.x -= 2
    #Moves the ball/Paddles
    ball.x += ballmovement[0]
    ball.y += ballmovement[1]
    rightpaddle.y += rightpaddlemovement
    leftpaddle.y += leftpaddlemovement

    #Score stuff
    score = font.render((str(leftScore) + " : " + str(rightScore)), True, WHITE)
    scoreRect = score.get_rect()
    scoreRect.center = ((width//2) + 5, 20)

    #Draws stuff to the screen
    clock.tick(60)
    screen.fill (background)
    pygame.draw.rect(screen, (80, 80, 80), (width/2, 0, 10, height))
    pygame.draw.ellipse(screen, GREEN, ball)
    pygame.draw.rect(screen,WHITE, leftpaddle)
    pygame.draw.rect(screen,WHITE, rightpaddle)
    screen.blit(score, scoreRect)
    pygame.display.update() #Updates the screen