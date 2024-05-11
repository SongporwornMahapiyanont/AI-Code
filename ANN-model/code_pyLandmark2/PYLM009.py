import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

BLACK = (0,0,0)
display_surface.fill(BLACK)

bg = pygame.image.load("mountains.jpg")
bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT)) #ปรับขนาดภาพให้เป็น w=800 h=600
bg_rect = bg.get_rect() #ขอบเขตสีเหลี่ยมของรูปภาพ
bg_rect.topleft = (0,0)

# The main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(bg,bg_rect)
    
    pygame.display.update()

pygame.quit()
