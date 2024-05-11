import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp
import numpy as np

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()        
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    h, w, c = img.shape

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            
            point103 = faceLms.landmark[103]   
            cx103, cy103 = int(point103.x*w), int(point103.y*h)
            #cv2.circle(img,(cx103,cy103),10,(0,0,255),-1)

            point332 = faceLms.landmark[332]   
            cx332, cy332 = int(point332.x*w), int(point332.y*h)
            #cv2.circle(img,(cx332,cy332),10,(0,0,255),-1)

            point137 = faceLms.landmark[137]   
            cx137, cy137 = int(point137.x*w), int(point137.y*h)
            #cv2.circle(img,(cx137,cy137),10,(0,0,255),-1)

            point366 = faceLms.landmark[366]   
            cx366, cy366 = int(point366.x*w), int(point366.y*h)
            #cv2.circle(img,(cx366,cy366),10,(0,0,255),-1)

            point150 = faceLms.landmark[150]   
            cx150, cy150 = int(point150.x*w), int(point150.y*h)
            #cv2.circle(img,(cx150,cy150),10,(0,0,255),-1)

            point379 = faceLms.landmark[379]   
            cx379, cy379 = int(point379.x*w), int(point379.y*h)
            #cv2.circle(img,(cx379,cy379),10,(0,0,255),-1)
            
            pointall = np.array([[cx103,cy103],[cx332,cy332],[cx137,cy137],[cx366,cy366],[cx150,cy150],[cx379,cy379]])
            rect = cv2.minAreaRect(pointall)
            box = cv2.boxPoints(rect)
            box = np.int0(box)         
            cv2.drawContours(img,[box],0,(0,255,0),5)
            
    cv2.imshow('img', img)        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
cap.release()
cv2.destroyAllWindows()
