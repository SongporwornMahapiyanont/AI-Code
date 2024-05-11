import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import numpy as np
import cv2

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

from tensorflow.keras.applications.inception_v3 import preprocess_input

model = load_model('best_model_ws06.h5',compile=False)

target_img_shape=(128,128)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img,1)
   
    x = 300
    y = 100
    w = 250
    h = 250      
    
    imgcut = img.copy()[y:y+h,x:x+w]

    img_input = cv2.resize(imgcut,target_img_shape)

    img_input = img_to_array(img_input)
    img_input = preprocess_input(img_input)

    img_input = np.expand_dims(img_input,axis=0) # (1, 128, 128, 3)

    result = model.predict(img_input)
    #print(result)

    class_answer = np.argmax(result,axis=1)
    if class_answer == 0:
        predict = 'bear'
    elif class_answer == 1:
        predict = 'car'
    elif class_answer == 2:
        predict = 'milk'

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

    conf = int(np.max(result)*100)
    if conf >= 75:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,predict + ' ' + str(conf) + '%',(160,80),font,2,(0,200,200),5)

    cv2.imshow("img",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
