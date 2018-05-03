import sys, pygame
from pygame.locals import *
pygame.init()
size = width, height = 320, 240
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

speedX = 5
speedY = 5
speed = 10
fired = False
paddle = pygame.image.load("paddle.png").convert_alpha()
paddlerect = paddle.get_rect()
ball = pygame.image.load("ball.png").convert_alpha()
ballrect = ball.get_rect()
ballrect.center = (200,200-10)
paddlerect.center = (200,200)
pygame.key.set_repeat(10)
font1 = pygame.font.SysFont("calibri",40)
font2 = pygame.font.SysFont("calibri",20)

while True:
    if fired:
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
            elif event.key==K_f:
                fired = True
            elif event.key==K_p:
                fired = False
            elif event.key==K_KP_PLUS:
                fps += 5
            elif event.key==K_KP_MINUS:
                if fps > 5:
                    fps -= 5
            elif event.key==K_q:
                sys.exit()

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle, paddlerect)
    text = font1.render("Life is short", True,(255,255,255))
    screen.blit(text,(0,0))

    text = font2.render("I use Python", True,(255,255,255))
    screen.blit(text,(50,50))
    pygame.display.update()
    clock.tick(fps)
