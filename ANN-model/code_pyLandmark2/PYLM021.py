import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

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
            
            point159 = faceLms.landmark[159]   
            cx159, cy159 = int(point159.x*w), int(point159.y*h)
            cv2.circle(img,(cx159,cy159),5,(0,255,0),-1)
            
            point145 = faceLms.landmark[145]   
            cx145, cy145 = int(point145.x*w), int(point145.y*h)
            cv2.circle(img,(cx145,cy145),5,(0,255,0),-1)

            point386 = faceLms.landmark[386]   
            cx386, cy386 = int(point386.x*w), int(point386.y*h)
            cv2.circle(img,(cx386,cy386),5,(0,0,255),-1)

            point374 = faceLms.landmark[374]   
            cx374, cy374 = int(point374.x*w), int(point374.y*h)
            cv2.circle(img,(cx374,cy374),5,(0,0,255),-1)
            
    cv2.imshow('img', img)        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
cap.release()
cv2.destroyAllWindows()
