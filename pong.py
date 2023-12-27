import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)
import random as rd

pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE  = 600
vindu=pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])

font = pg.font.SysFont("Arial", 24)

class Paddle:
    def __init__(self,xPos, yPos, rightPaddle:bool):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = 0.2
        self.rightPaddle = rightPaddle
        self.width = 10
        self.length = 70
        self.points = 0
    
    def movePaddle(self,keysPressed):
        if self.yPos < 0:
            self.yPos = 1
        elif self.yPos+self.length > 600:
            self.yPos = 599-self.length

        if self.rightPaddle:
            if keysPressed[K_UP]:
                self.yPos-=self.speed
            elif keysPressed[K_DOWN]:
                self.yPos+=self.speed
        else:
            if keysPressed[K_w]:
                self.yPos-=self.speed
            elif keysPressed[K_s]:
                self.yPos+=self.speed
        
        self.drawPaddle()
    
    def drawPaddle(self):
        pg.draw.rect(vindu, (0,0,0), (self.xPos,self.yPos, self.width,self.length))
    
    def getRect(self):
        return pg.Rect(self.xPos,self.yPos,self.width,self.length)


class Ball:
    def __init__(self, xPos,yPos,rad):
        self.xPos = xPos
        self.yPos = yPos
        self.rad = rad
        self.xSpeed = 0.1
        self.ySpeed = 0.1
    
    def drawBall(self):
        pg.draw.rect(vindu, (0,0,0), (self.xPos,self.yPos, self.rad,self.rad))
    
    def getRect(self):
        return pg.Rect(self.xPos,self.yPos,self.rad,self.rad)
    
    def moveBall(self):
        if self.yPos <=0 or self.yPos >= 600:
            self.ySpeed = -self.ySpeed
        self.xPos += self.xSpeed
        self.yPos += self.ySpeed
        self.drawBall()

rightPaddle = Paddle(580,270,True)
leftPaddle = Paddle(10,270,False)
ball = Ball(300,300,10)


fortsett = True

while rightPaddle.points<=10 or leftPaddle.points <=10:
    while fortsett:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fortsett = False
        vindu.fill((255,255,255))

        trykkedeTaster = pg.key.get_pressed()
        rightPaddle.movePaddle(trykkedeTaster)
        leftPaddle.movePaddle(trykkedeTaster)

        rightPoints = font.render(str(rightPaddle.points), True, (0,0,0))
        vindu.blit(rightPoints, (320,20))

        leftPoints = font.render(str(leftPaddle.points), True, (0,0,0))
        vindu.blit(leftPoints, (280,20))

        ball.moveBall()

        if rightPaddle.getRect().colliderect(ball.getRect()) or leftPaddle.getRect().colliderect(ball.getRect()):
            ball.xSpeed = -ball.xSpeed
        
        if ball.xPos > 600:
            leftPaddle.points+=1
            break
        elif ball.xPos < 0:
            rightPaddle.points+=1
            break

        pg.display.flip()
