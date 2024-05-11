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

box = pygame.image.load("box2.png")
box = pygame.transform.scale(box, (80,80))
box_rect = box.get_rect()
box_rect.topleft = (320,240)

# The main loop
cap = cv2.VideoCapture(0)

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
            box_rect.center = (cx8,cy8)
   
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        

    display_surface.blit(bg,bg_rect)     
    display_surface.blit(box,box_rect)   
        
    pygame.display.update()
    
pygame.quit()
