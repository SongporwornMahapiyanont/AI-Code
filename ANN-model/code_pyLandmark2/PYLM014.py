import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

hands = mp.solutions.hands.Hands(max_num_hands=2)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):    
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
                    
    cv2.imshow("img", img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
