import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    ret, img = cap.read()        
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    h, w, c = img.shape

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            
            point13 = faceLms.landmark[13]   
            cx13, cy13 = int(point13.x*w), int(point13.y*h)
            cv2.circle(img,(cx13,cy13),10,(0,0,255),-1)

            point14 = faceLms.landmark[14]   
            cx14, cy14 = int(point14.x*w), int(point14.y*h)
            cv2.circle(img,(cx14,cy14),10,(255,0,0),-1)

            dist = int((point14.y-point13.y)*100)
            cv2.line(img,(cx13,cy13),(cx14,cy14),(0,255,0),5)
            
            if dist > 5:
            	cv2.putText(img,"Open",(50,100),font,2,(0,180,100),8)
            else:
            	cv2.putText(img,"Close",(50,100),font,2,(0,100,255),8)
            	
    cv2.imshow('img', img)        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
cap.release()
cv2.destroyAllWindows()
