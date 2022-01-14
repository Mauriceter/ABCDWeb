import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30


# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0,0,255))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -

rectangle = pygame.rect.Rect(176, 134, 200, 200)
rectangle_draging = False

# - function -

# - mainloop -

clock = pygame.time.Clock()
running = True
while running:

    # - events -
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y

    # - updates (without draws) -

    # - draws (without updates) -
    screen.fill((0,0,255))
    pygame.draw.rect(screen, RED, rectangle)
    pygame.display.flip()

    # - constant game speed / FPS -
    clock.tick(FPS)

pygame.quit()