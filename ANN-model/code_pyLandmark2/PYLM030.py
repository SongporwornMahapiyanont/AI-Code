import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import pygame
import cv2
import mediapipe as mp

pose = mp.solutions.pose.Pose()

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

BLACK = (0,0,0)
display_surface.fill(BLACK)

font = pygame.font.Font('THSarabunNewBold.ttf',120)

text = font.render("???",True,(0,255,0)) #RGB
text_rect = text.get_rect()
text_rect.topleft = (30,10)

cap = cv2.VideoCapture(0)

running = True
while running and cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img,1)
        
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    h, w, c = img.shape

    if results.pose_landmarks:
        poseLms = results.pose_landmarks

        point0 = poseLms.landmark[0]
        cx0, cy0 = int(point0.x*w), int(point0.y*h)
        cv2.circle(img,(cx0,cy0),15,(0,0,255),-1)

        point19 = poseLms.landmark[19]
        cx19, cy19 = int(point19.x*w), int(point19.y*h)
        cv2.circle(img,(cx19,cy19),15,(0,255,0),-1)

        point20 = poseLms.landmark[20]
        cx20, cy20 = int(point20.x*w), int(point20.y*h)
        cv2.circle(img,(cx20,cy20),15,(0,255,255),-1)

        if (cy20 < cy0) and (cy19 > cy0):
            text = font.render("ซ้าย",True,(255,255,0)) #RGB
        elif (cy19 < cy0) and (cy20 > cy0):
            text = font.render("ขวา",True,(0,255,0)) #RGB
        else:
            text = font.render("???",True,(0,255,255)) #RGB        
                
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
    display_surface.blit(bg,bg_rect)
    display_surface.blit(text,text_rect)    
            
    pygame.display.update()
    
pygame.quit()

