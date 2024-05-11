import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model

#-----------------------------------------------
faceLms_model_filename = 'faceLms_model.h5'
#-----------------------------------------------

model = load_model(faceLms_model_filename)

model.summary()

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)
drawing_spec = mp.solutions.drawing_utils.DrawingSpec(thickness=1,circle_radius=2)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)
    
    h, w, c = img.shape
    
    if results.multi_face_landmarks: #พบใบหน้าในภาพ
        faceLms = results.multi_face_landmarks[0]
        mp.solutions.drawing_utils.draw_landmarks(image=img,
            landmark_list=faceLms,
            connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)        
        faceLms_x = [i.x for i in faceLms.landmark]
        faceLms_y = [i.y for i in faceLms.landmark]

        center_x = int(np.sum(faceLms_x)/468*w)
        center_y = int(np.sum(faceLms_y)/468*h)
 
        for i in range(0,468):
            faceLms_x[i] = int(faceLms_x[i]*w)
            faceLms_y[i] = int(faceLms_y[i]*h)

            faceLms_x[i] = faceLms_x[i] - center_x + 250
            faceLms_y[i] = faceLms_y[i] - center_y + 250           
          
        min_x = np.min(faceLms_x)
        max_x = np.max(faceLms_x)
        min_y = np.min(faceLms_y)
        max_y = np.max(faceLms_y)       

        for i in range(0,468):
            faceLms_x[i] = int(faceLms_x[i] * (250/(max_y-min_y)))
            faceLms_y[i] = int(faceLms_y[i] * (250/(max_y-min_y)))

        center_x = int(np.sum(faceLms_x)/468)
        center_y = int(np.sum(faceLms_y)/468)
        
        for i in range(0,468):
            faceLms_x[i] = faceLms_x[i] - center_x + 250
            faceLms_y[i] = faceLms_y[i] - center_y + 250

        faceLms_xy = faceLms_x + faceLms_y
        
        y_pred = model.predict([faceLms_xy],verbose=0)
        
        y_pred_class = np.argmax(y_pred,axis=1)
        y_pred_val = int(np.max(y_pred)*100)
        #print(y_pred_class)
        if y_pred_class == 0:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'normal ' + str(y_pred_val) + '%',(100,100),font,2,(0,200,200),5)
        elif y_pred_class == 1:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'shock ' + str(y_pred_val) + '%',(100,100),font,2,(0,200,200),5)
        elif y_pred_class == 2:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'smile ' + str(y_pred_val) + '%',(100,100),font,2,(0,200,200),5)
            
    cv2.imshow("img", img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
