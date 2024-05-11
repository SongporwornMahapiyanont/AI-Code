import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model

#----------------------------------------------
handLms_model_filename = 'handLms_model.h5'
#----------------------------------------------

model = load_model(handLms_model_filename)

model.summary()

hands = mp.solutions.hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    h, w, c = img.shape
    
    if results.multi_hand_landmarks: #พบมือในภาพ
        handLms = results.multi_hand_landmarks[0]
        mp.solutions.drawing_utils.draw_landmarks(img,handLms,mp.solutions.hands.HAND_CONNECTIONS)
        
        handLms_x = [i.x for i in handLms.landmark]
        handLms_y = [i.y for i in handLms.landmark] 

        center_x = int(np.sum(handLms_x)/21*w)
        center_y = int(np.sum(handLms_y)/21*h)
 
        for i in range(0,21):
            handLms_x[i] = int(handLms_x[i]*w)
            handLms_y[i] = int(handLms_y[i]*h)

            handLms_x[i] = handLms_x[i] - center_x + 250
            handLms_y[i] = handLms_y[i] - center_y + 250            
          
        min_x = np.min(handLms_x)
        max_x = np.max(handLms_x)
        min_y = np.min(handLms_y)
        max_y = np.max(handLms_y)        

        for i in range(0,21):
            handLms_x[i] = int(handLms_x[i] * (250/(max_y-min_y)))
            handLms_y[i] = int(handLms_y[i] * (250/(max_y-min_y)))

        center_x = int(np.sum(handLms_x)/21)
        center_y = int(np.sum(handLms_y)/21)
        
        for i in range(0,21):
            handLms_x[i] = handLms_x[i] - center_x + 250
            handLms_y[i] = handLms_y[i] - center_y + 250

        handLms_xy = handLms_x + handLms_y
        
        y_pred = model.predict([handLms_xy],verbose=0)
        
        y_pred_class = np.argmax(y_pred,axis=1)
        y_pred_val = int(np.max(y_pred)*100)
        #print(y_pred_class)
        if y_pred_class == 0:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'like ' + str(y_pred_val) + '%',(100,100),font,2,(50,200,0),5)
        elif y_pred_class == 1:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'love ' + str(y_pred_val) + '%',(100,100),font,2,(50,200,0),5)
        elif y_pred_class == 2:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'ok ' + str(y_pred_val) + '%',(100,100),font,2,(50,200,0),5)
        elif y_pred_class == 3:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'two ' + str(y_pred_val) + '%',(100,100),font,2,(50,200,0),5)
            
    cv2.imshow("img", img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
