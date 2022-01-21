import pygame

class Carre:
    liste = []
    def __init__(self,x,y,heigh):
        self.rectangle = pygame.rect.Rect(x,y, heigh, heigh)
        self.x=x
        self.y=y
        self.heigh=heigh
        self.rectangle_draging = False
        Carre.liste.append(self)

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

class Fleche:
    def __init__(self, can, x, y, color=(255,255,255)):
        pygame.draw.polygon(can, color,
        [(20+x,20+y),
        (80+x,20+y),
        (80+x,10+y),
        (100+x,30+y),
        (80+x,50+y),
        (80+x,40+y),
        (20+x,40+y)])

