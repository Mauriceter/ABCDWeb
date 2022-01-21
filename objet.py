import pygame
class Carre:
    def __init__(self,x,y,heigh):
        self.rectangle = pygame.rect.Rect(x,y, heigh, heigh)
        self.x=x
        self.y=y
        self.heigh=heigh
        self.rectangle_draging = False

    def getx(self):
        return self.x

    def gety(self):
        return self.y
    
    def getheigh(self):
        return self.heigh
    
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
        self.rectangle = pygame.rect.Rect(self.x,self.y, self.heigh, self.heigh)

class image:
    def __init__(self,carre,path):
        self.carre=carre
        self.path=path
