import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import pygame
import cv2
import mediapipe as mp

hands = mp.solutions.hands.Hands(max_num_hands=1)

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

BLACK = (0,0,0)
display_surface.fill(BLACK)

font = pygame.font.Font('THSarabunNewBold.ttf',100)

text1 = font.render("ก",True,(255,120,0))
text1_rect = text1.get_rect()
text1_rect.center = (88,88)

text2 = font.render("ข",True,(255,120,0))
text2_rect = text2.get_rect()
text2_rect.center = (244,88)

text3 = font.render("ค",True,(255,120,0))
text3_rect = text3.get_rect()
text3_rect.center = (400,88)

text4 = font.render("ง",True,(255,120,0))
text4_rect = text4.get_rect()
text4_rect.center = (556,88)

# The main loop
cap = cv2.VideoCapture(0)
cx8, cy8 = 0,0
running = True
while running and cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img,1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    h, w, c = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            point8 = handLms.landmark[8]                   
            cx8, cy8 = int(point8.x*w), int(point8.y*h)
            cv2.circle(img,(cx8,cy8),15,(0,255,255),-1)
   
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        

    display_surface.blit(bg,bg_rect)
    
    box1 = pygame.draw.rect(display_surface,(0,255,0),(20,20,135,135),6)
    box2 = pygame.draw.rect(display_surface,(0,255,0),(175,20,135,135),6)
    box3 = pygame.draw.rect(display_surface,(0,255,0),(330,20,135,135),6)
    box4 = pygame.draw.rect(display_surface,(0,255,0),(485,20,135,135),6)

    if box1.collidepoint(cx8,cy8):
        pygame.draw.rect(display_surface,(0,150,180),(26,26,123,123),0)
    if box2.collidepoint(cx8,cy8):
        pygame.draw.rect(display_surface,(0,150,180),(181,26,123,123),0)
    if box3.collidepoint(cx8,cy8):
        pygame.draw.rect(display_surface,(0,150,180),(336,26,123,123),0)
    if box4.collidepoint(cx8,cy8):
        pygame.draw.rect(display_surface,(0,150,180),(491,26,123,123),0)
        
    display_surface.blit(text1,text1_rect)
    display_surface.blit(text2,text2_rect)
    display_surface.blit(text3,text3_rect)
    display_surface.blit(text4,text4_rect)

    pygame.display.update()
    
pygame.quit()
