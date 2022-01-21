import pygame
import random
from objet import *
# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
NB = 2

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30



# - init -
pygame.init()

# - objects -
class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jeu 1")

    def draw(self):
        self.screen.fill((0,0,255))
        for i in range (NB):
            pygame.draw.rect(self.screen, (255,0,255), pygame.rect.Rect(100 + 400*i, 100, 200, 200))
            Fleche(self.screen, 350 + 400*i, 180)


c

sc = Screen()
sc.draw()
liste = []

rect1=Rectangle()
rect2=Rectangle()

# - function -


def drag(events):
    global running
    global rectangle_draging
    global offset_x
    global offset_y
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                for rect in liste:          
                    if rect.rectangle.collidepoint(event.pos):
                        rect.rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rect.rectangle.x - mouse_x
                        offset_y = rect.rectangle.y - mouse_y
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for rect in liste:            
                    rect.rectangle_draging = False
                    if 50<rect.rectangle.x < 150 and 50<rect.rectangle.y < 150:
                        rect.rectangle.x = 100
                        rect.rectangle.y = 100

        elif event.type == pygame.MOUSEMOTION:
            for rect in liste:
                if rect.rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rect.rectangle.x = mouse_x + offset_x
                    rect.rectangle.y = mouse_y + offset_y
# - mainloop -

clock = pygame.time.Clock()
running = True
while running:
    # - events -
    events = pygame.event.get()
    drag(events)

    # - updates (without draws) -

    # - draws (without updates) -
    sc.draw()
    for rect in liste:
        pygame.draw.rect(sc.screen, RED, rect.rectangle)
    pygame.display.flip()

    # - constant game speed / FPS -
    clock.tick(FPS)

pygame.quit()