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
pygame.display.set_caption("Hello WebCam")

BLACK = (0,0,0)
display_surface.fill(BLACK)

font = pygame.font.Font('THSarabunNewBold.ttf',80)

text = font.render("ปรับขนาดวัตถุ",True,(0,255,255)) #RGB
text_rect = text.get_rect()
text_rect.topleft = (30,10)

apple = pygame.image.load("apple.png")
apple_rect = apple.get_rect()
apple_rect.center = (150,200)

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
            point4 = handLms.landmark[4]
            point8 = handLms.landmark[8]
            
            cx4, cy4 = int(point4.x*w), int(point4.y*h)
            cv2.circle(img,(cx4,cy4),15,(0,255,0),-1)

            cx8, cy8 = int(point8.x*w), int(point8.y*h)
            cv2.circle(img,(cx8,cy8),15,(0,0,255),-1)
                    
            if cx4>0 and cy4>0 and cx8>0 and cy8>0: #พบทั้ง 2 นิ้ว
                cv2.line(img,(cx4,cy4),(cx8,cy8),(0,255,255),10) 
                apple = pygame.image.load("apple.png")
                apple = pygame.transform.scale(apple, (abs(cy4-cy8),abs(cy4-cy8)))
                apple_rect = apple.get_rect()
                apple_rect.center = (150,200)
                    
    bg = pygame.image.frombuffer(img.tobytes(),img.shape[1::-1],"BGR")
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        

    display_surface.blit(bg,bg_rect)     
    display_surface.blit(apple,apple_rect)    
    display_surface.blit(text,text_rect)    
        
    pygame.display.update()
    
pygame.quit()
