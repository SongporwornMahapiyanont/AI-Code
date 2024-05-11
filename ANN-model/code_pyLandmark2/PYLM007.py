import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

# (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

display_surface.fill(BLACK)

#Line(surface,color,starting point,ending point,thickness)
pygame.draw.line(display_surface,RED,(0,0),(200,150),5)
pygame.draw.line(display_surface,GREEN,(200,200),(500,300),3)

#Circle(surface,color,center,radius,thickness or 0 for fill)
pygame.draw.circle(display_surface,GREEN,(150,80),20,3)
pygame.draw.circle(display_surface,YELLOW,(250,300),30,0) # pygame 0 ทึบ , OpenCV -1 ทึบ

#Rectangle(surface,color,(x,y,w,h),thickness or 0 for fill)
pygame.draw.rect(display_surface,CYAN,(50,50,100,120),3)
pygame.draw.rect(display_surface,MAGENTA,(200,10,120,80),0) #ทึบ

# The main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
