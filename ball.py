import pygame
import sys

pygame.init()
size=width,height=640,480

screen=pygame.display.set_mode(size)
ball=pygame.image.load('ball.jpg')
ballrect=ball.get_rect()
speed=[5,5]
Clock=pygame.time.Clock()
color=(0,0,0)

while True:
    Clock.tick(60)#每秒执行60次
    
    #添加检测事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    ballrect=ballrect.move(speed)
    #碰撞检测
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]

    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]

    screen.fill(color)
    screen.blit(ball,ballrect)
    pygame.display.flip()
    
    
pygame.quit()
