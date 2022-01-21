class Rectangle:
    def __init__(self,x,y):
        self.rectangle = pygame.rect.Rect(random.randint(100,800), random.randint(100,800), 200, 200)
        self.rectangle_draging = False
        liste.append(self)