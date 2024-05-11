import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import pygame
import cv2
import mediapipe as mp

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello WebCam")

BLACK = (0,0,0)
display_surface.fill(BLACK)

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
            
            point130 = faceLms.landmark[130]   
            cx130, cy130 = int(point130.x*w), int(point130.y*h)
            #cv2.circle(img,(cx130,cy130),5,(0,0,255),-1)

            point359 = faceLms.landmark[359]   
            cx359, cy359 = int(point359.x*w), int(point359.y*h)
            #cv2.circle(img,(cx359,cy359),5,(0,0,255),-1)
            
            point6 = faceLms.landmark[6]   
            cx6, cy6 = int(point6.x*w), int(point6.y*h)
            #cv2.circle(img,(cx6,cy6),5,(0,255,255),-1)

            eyes = pygame.image.load("eyes.png")
            eyes = pygame.transform.scale(eyes, (cx359-cx130+5,50))
            eyes_rect = eyes.get_rect()
            eyes_rect.center = (cx6,cy6)
            
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        

    display_surface.blit(bg,bg_rect)     
    display_surface.blit(eyes,eyes_rect)    
        
    pygame.display.update()
    
pygame.quit()
