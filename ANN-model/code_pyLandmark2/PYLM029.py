import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

pose = mp.solutions.pose.Pose()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img,1)
        
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    h, w, c = img.shape

    if results.pose_landmarks:
        poseLms = results.pose_landmarks

        point12 = poseLms.landmark[12]
        cx12, cy12 = int(point12.x*w), int(point12.y*h)
        cv2.circle(img,(cx12,cy12),15,(0,0,255),-1)

        point11 = poseLms.landmark[11]
        cx11, cy11 = int(point11.x*w), int(point11.y*h)
        cv2.circle(img,(cx11,cy11),15,(0,255,255),-1)

        cv2.line(img,(cx12,cy12),(cx11,cy11),(0,255,0),8)
        
    cv2.imshow('img', img)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
