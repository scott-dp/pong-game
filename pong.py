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
        self.fart = 0.2
        self.rightPaddle = rightPaddle
        self.width = 10
        self.length = 70
        self.points = 0
    
    def movePaddle(self,tasterTrykket):
        if self.yPos < 0:
            self.yPos = 1
        elif self.yPos+self.length > 600:
            self.yPos = 599-self.length

        if self.rightPaddle:
            if tasterTrykket[K_UP]:
                self.yPos-=self.fart
            elif tasterTrykket[K_DOWN]:
                self.yPos+=self.fart
        else:
            if tasterTrykket[K_w]:
                self.yPos-=self.fart
            elif tasterTrykket[K_s]:
                self.yPos+=self.fart
        
        self.drawPaddle()
    
    def drawPaddle(self):
        pg.draw.rect(vindu, (0,0,0), (self.xPos,self.yPos, self.width,self.length))
    
    def getRect(self):
        return pg.Rect(self.xPos,self.yPos,self.width,self.length)



rightPaddle = Paddle(580,0,True)
leftPaddle = Paddle(10,0,False)
fortsett = True
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


    pg.display.flip()
