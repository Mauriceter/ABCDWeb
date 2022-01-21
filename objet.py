import pygame
class Rectangle:
    def __init__(self,x,y):
        self.rectangle = pygame.rect.Rect(random.randint(100,800), random.randint(100,800), 200, 200)
        self.rectangle_draging = False
        liste.append(self)

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

