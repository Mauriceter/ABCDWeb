import pygame

class Carre:
    liste = []
    def __init__(self,x,y,heigh, value):
        self.rectangle = pygame.rect.Rect(x,y, heigh, heigh)
        self.heigh=heigh
        self.value = value
        self.rectangle_draging = False
        Carre.liste.append(self)

    def getx(self):
        return self.rectangle.x

    def gety(self):
        return self.rectangle.y
    
    def getheigh(self):
        return self.heigh
    
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
        self.rectangle = pygame.rect.Rect(self.x,self.y, self.heigh, self.heigh)

class Emplacement:
    def __init__(self, can, x,y,heigh, color = (23, 250, 59)):
        self.rectangle = pygame.rect.Rect(x,y, heigh, heigh)
        pygame.draw.rect(can, color, self.rectangle)


class image:
    def __init__(self,carre,path):
        self.carre=carre
        self.path=path

class Fleche:
    def __init__(self, can, x, y, color=(255,255,255)):
        pygame.draw.polygon(can, color,
        [(x,10+y),
        (60+x,10+y),
        (60+x,+y),
        (80+x,20+y),
        (60+x,40+y),
        (60+x,30+y),
        (x,30+y)])

