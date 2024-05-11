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

    img2 = np.zeros(img.shape)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)
    
    h, w, c = img.shape
    
    if results.multi_face_landmarks: #พบใบหน้าในภาพ
        faceLms = results.multi_face_landmarks[0]
        
        faceLms_x = [i.x for i in faceLms.landmark]
        faceLms_y = [i.y for i in faceLms.landmark] 

        center_x = int(np.sum(faceLms_x)/468*w)
        center_y = int(np.sum(faceLms_y)/468*h)
        cv2.circle(img,(center_x,center_y),5,(0,255,255),-1)

        
        for i in range(0,468):
            faceLms_x[i] = int(faceLms_x[i]*w)
            faceLms_y[i] = int(faceLms_y[i]*h)
            
            cv2.circle(img,(faceLms_x[i],faceLms_y[i]),2,(255,255,255),-1)

            faceLms_x[i] = faceLms_x[i] - center_x + 320
            faceLms_y[i] = faceLms_y[i] - center_y + 240
            
            cv2.circle(img2,(faceLms_x[i],faceLms_y[i]),2,(255,255,255),-1)
            cv2.circle(img2,(320,240),5,(0,255,255),-1)
            
    key = cv2.waitKey(1) & 0xFF              
    cv2.imshow("img", img)
    cv2.imshow("img2", img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
