import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

# (R,G,B)
BLACK = (0,0,0)
GRAY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
display_surface.fill(GRAY)

#See all available system fonts
#fonts = pygame.font.get_fonts()
#for font in fonts:
#    print(font)

#Load my fonts
font1 = pygame.font.SysFont('calibri',64)
font2 = pygame.font.Font('AttackGraffiti.ttf',32)
font3 = pygame.font.Font('MNThapthimKrop.ttf',100)
font4 = pygame.font.Font('THSarabunNew.ttf',100)

text1 = font1.render("Hello pygame",True,WHITE)
text1_rect = text1.get_rect()
text1_rect.center = (200,50)

text2 = font2.render("python pygame",True,BLUE,RED)
text2_rect = text2.get_rect()
text2_rect.center = (200,110)

text3 = font3.render("สวัสดี SU",True,GREEN)
text3_rect = text3.get_rect()
text3_rect.center = (200,180)

text4 = font4.render("ยินดีต้อนรับ",True,(255,255,0))
text4_rect = text4.get_rect()
text4_rect.center = (200,300)

# The main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(text1,text1_rect) 
    display_surface.blit(text2,text2_rect)
    display_surface.blit(text3,text3_rect)
    display_surface.blit(text4,text4_rect)
    
    pygame.display.update()

pygame.quit()
