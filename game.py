import sys, pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)
speedX = 5
speedY = 5
speed = 10
paddle = pygame.image.load("paddle.png").convert_alpha()
paddlerect = paddle.get_rect()
ball = pygame.image.load("ball.png").convert_alpha()
ballrect = ball.get_rect()
ballrect.center = (200,200-10)
paddlerect.center = (200,200)
pygame.key.set_repeat(10)
while True:
    if ballrect.x <= 0 or ballrect.x > 320:
        speedX = -speedX

    if ballrect.y <= 0 or ballrect.y > 240:
        speedY = -speedY
    ballrect.x += speedX
    ballrect.y += speedY
    if (ballrect.y + ballrect.height) > paddlerect.y:
        if (ballrect.x > paddlerect.x and ballrect.x < paddlerect.x + paddlerect.width):
            speedY = -speedY
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_a:
                paddlerect.x -= speed
                #固定小球位置
                #ballrect.x = paddlerect.x+25
            elif event.key==K_d:
                paddlerect.x += speed
                #ballrect.x = paddlerect.x+25
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle, paddlerect)
    pygame.display.update()
    clock.tick(60)
