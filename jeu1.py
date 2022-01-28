import pygame
import random
from objet import *
# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
NB = 4


#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30

# - init -
pygame.init()

# - objects -
def espace(l_carre,l_fleche):
    x=SCREEN_WIDTH*.9
    return  (x-NB*l_carre-(NB-1)*l_fleche)/(2*(NB-1))

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jeu 1")

    def draw(self):
        self.screen.fill((0,0,255))
        for i in range (NB):
            Emplacement(self.screen, SCREEN_WIDTH*.05+i*(2*espace(200,80)+200+80), 100, 200,i)
        for j in range (NB-1):
            Fleche(self.screen, SCREEN_WIDTH*.05+200+espace(200,80)+j*(2*espace(200,80)+200+80), 180)


sc = Screen()
sc.draw()
for i in range (NB):
    Carre("image/img"+str(i+1)+".png",200+ 200*i,700, 200, i)

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
                for rect in Carre.liste:          
                    if rect.rectangle.collidepoint(event.pos):
                        rect.rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rect.rectangle.x - mouse_x
                        offset_y = rect.rectangle.y - mouse_y
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for rect in Carre.liste:            
                    rect.rectangle_draging = False
                    for i in range (NB):
                        if SCREEN_WIDTH*.05+i*(2*espace(200,80)+200+80) - 50 <rect.rectangle.x < SCREEN_WIDTH*.05+i*(2*espace(200,80)+200+80) + 50 and 50<rect.rectangle.y < 150 :
                            rect.rectangle.x = SCREEN_WIDTH*.05+i*(2*espace(200,80)+200+80)
                            rect.rectangle.y = 100 

        elif event.type == pygame.MOUSEMOTION:
            for rect in Carre.liste:
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
    tot=0
    win = False
    for carre in Carre.liste:
        for i in range(NB):
            if carre.rectangle.x == int(SCREEN_WIDTH*.05+i*(2*espace(200,80)+200+80)) and carre.rectangle.y == 100 and carre.value == i:
                tot+=1
    if tot == NB:
        win = True
    # - draws (without updates) -
    sc.draw()
    for rect in Carre.liste:
        sc.screen.blit(rect.image, rect.rectangle)
        #pygame.draw.rect(sc.screen, RED, rect.rectangle)
    if win == True:
        pygame.draw.rect(sc.screen, (255,0,255), pygame.rect.Rect(400,400, 300, 300))
    pygame.display.flip()
    
    # - constant game speed / FPS -
    clock.tick(FPS)

pygame.quit()