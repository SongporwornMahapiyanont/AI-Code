import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

hands = mp.solutions.hands.Hands(max_num_hands=1)

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

while(cap.isOpened()):    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    h, w, c = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            point8 = handLms.landmark[8]
            
            cv2.putText(img,"x={:.4f}".format(point8.x),(20,100),font,1.5,(255,120,0),3)
            cv2.putText(img,"y={:.4f}".format(point8.y),(20,150),font,1.5,(255,120,0),3)
            cv2.putText(img,"z={:.4f}".format(point8.z),(20,200),font,1.5,(255,120,0),3)                 

            cx8, cy8 = int(point8.x*w), int(point8.y*h)
            cv2.circle(img,(cx8,cy8),15,(0,255,255),-1)
                    
    cv2.imshow("img", img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
