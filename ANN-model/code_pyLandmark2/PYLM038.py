import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp
import numpy as np

hands = mp.solutions.hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):    
    ret, img = cap.read()
    img = cv2.flip(img,1)

    img2 = np.zeros(img.shape)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    h, w, c = img.shape
    
    if results.multi_hand_landmarks: #พบมือในภาพ
        handLms = results.multi_hand_landmarks[0]
        
        handLms_x = [i.x for i in handLms.landmark]
        handLms_y = [i.y for i in handLms.landmark] 

        center_x = int(np.sum(handLms_x)/21*w)
        center_y = int(np.sum(handLms_y)/21*h)
        cv2.circle(img,(center_x,center_y),8,(0,255,255),-1)

        
        for i in range(0,21):
            handLms_x[i] = int(handLms_x[i]*w)
            handLms_y[i] = int(handLms_y[i]*h)
            
            cv2.circle(img,(handLms_x[i],handLms_y[i]),5,(255,255,255),-1)

            handLms_x[i] = handLms_x[i] - center_x + 320
            handLms_y[i] = handLms_y[i] - center_y + 240
            
            cv2.circle(img2,(handLms_x[i],handLms_y[i]),5,(255,255,255),-1)
            cv2.circle(img2,(320,240),8,(0,255,255),-1)
            
    key = cv2.waitKey(1) & 0xFF              
    cv2.imshow("img", img)
    cv2.imshow("img2", img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
