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

def randomTupleSumOne():
    while True:
        num1 = rd.randint(3,18)
        num2 = rd.randint(3,18)
        if num1+num2 == 25:
            return (num1/100,num2/100)


class Ball:
    xs,ys = randomTupleSumOne()
    def __init__(self, xPos,yPos,rad):
        self.xPos = xPos
        self.yPos = yPos
        self.rad = rad
        self.xSpeed = self.xs
        self.ySpeed = self.ys
    
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

while (rightPaddle.points<10 and leftPaddle.points <10):
    ball = Ball(300,300,10)
    if rd.randint(0,10) > 5:
        ball.xSpeed = -ball.xSpeed
    fortsett = True
    while fortsett:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
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
            newXSpeed, newYSpeed = randomTupleSumOne()
            if ball.xPos>300:
                ball.xSpeed = -newXSpeed
                ball.ySpeed = newYSpeed
            else:
                ball.xSpeed = newXSpeed
                ball.ySpeed = newYSpeed
        
        if ball.xPos > 600:
            leftPaddle.points+=1
            fortsett = False
        elif ball.xPos < 0:
            rightPaddle.points+=1
            fortsett = False


        pg.display.flip()
