import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import pygame
import cv2

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello WebCam")

BLACK = (0,0,0)
display_surface.fill(BLACK)

# font
font = pygame.font.Font('THSarabunNew.ttf',80)

text = font.render("สวัสดี Pygame",True,(0,255,255)) #RGB
text_rect = text.get_rect()
text_rect.topleft = (30,10)

SnowMan = pygame.image.load("SnowMan.png")
#SnowMan = pygame.transform.scale(SnowMan, (84,130))
SnowMan_rect = SnowMan.get_rect()
SnowMan_rect.topleft = (350,200)

Tree = pygame.image.load("Tree_2.png")
#Tree = pygame.transform.scale(Tree, (64,64))
Tree_rect = Tree.get_rect()
Tree_rect.topleft = (80,130)

# The main loop
cap = cv2.VideoCapture(0)

running = True
while running and cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img,1)
   
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    #print(img.shape[1::-1]) #(640,480)
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        

    display_surface.blit(bg,bg_rect)     
    display_surface.blit(SnowMan,SnowMan_rect)
    display_surface.blit(Tree,Tree_rect)    
    display_surface.blit(text,text_rect)    
        
    pygame.display.update()
    
pygame.quit()
