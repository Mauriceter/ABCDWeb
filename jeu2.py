import pygame
from random import randint
from objet import *
from math import sqrt

# --- constants --- (UPPER_CASE names)
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
FPS = 30

# - init -
pygame.init()

# - objects -
class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jeu 2")
    def draw(self):
        self.screen.fill((0,0,255))
sc = Screen()
sc.draw()

Circle = [] #Creation des cercles
for i in range(2):
    Circle.append([[randint(300,800),randint(300,800)],[0,0]]) #uplet 1 pour le centre uplet 2 pour la vitesse

# - function -
def collision(events):
    global running
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            for circle in Circle:
                if sqrt((circle[0][0]-mouse_x)**2 + (circle[0][1]-mouse_y)**2) < 100:
                    
                    circle[1] = [60,0]

def vitesse():
    for circle in Circle:
        if circle[1][0] > 0:
            circle[1][0] -= 10
        circle[0][0] += circle[1][0]

# - mainloop -
clock = pygame.time.Clock()
running = True
while running:
    # - events -
    events = pygame.event.get()
    collision(events)
    # - updates (without draws) -
    vitesse()
    # - draws (without updates) -
    sc.draw()
    for circle in Circle:
        pygame.draw.circle(sc.screen, (10,10,10), circle[0], 100)
    pygame.display.flip()    
    # - constant game speed / FPS -
    clock.tick(FPS)

pygame.quit()