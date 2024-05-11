import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import pygame
import cv2
import mediapipe as mp
import numpy as np

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

BLACK = (0,0,0)
display_surface.fill(BLACK)

font = pygame.font.Font('THSarabunNewBold.ttf',100)


cap = cv2.VideoCapture(0)

running = True
while running and cap.isOpened():
    ret, img = cap.read()        
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    h, w, c = img.shape

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:

            point10 = faceLms.landmark[10]   
            cx10, cy10 = int(point10.x*w), int(point10.y*h)
            cv2.circle(img,(cx10,cy10),5,(0,255,255),-1)
            
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
    display_surface.blit(bg,bg_rect)

    text = font.render("โสภณ",True,(0,200,255))
    text_rect = text.get_rect()
    text_rect.center = (cx10,cy10-20)
    display_surface.blit(text,text_rect)
       
    pygame.display.update()
    
pygame.quit()
