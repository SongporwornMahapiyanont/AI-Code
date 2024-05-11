import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp
import numpy as np
from csv import writer

hands = mp.solutions.hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

csv_filename = 'handLms.csv'

#---------------------------------------------------------
col_name_x = ['x'+str(i) for i in range(0,21)]
col_name_y = ['y'+str(i) for i in range(0,21)]
col_name_xy = col_name_x + col_name_y + ['class_name']
print(col_name_xy)
with open(csv_filename,'w',encoding='UTF8',newline='') as f:
    writer_f = writer(f)
    writer_f.writerow(col_name_xy)
    f.close()
#---------------------------------------------------------
  
count_like = 0
count_love = 0
count_ok = 0
count_two = 0

while(cap.isOpened()):    
    ret, img = cap.read()
    img = cv2.flip(img,1)

    img2 = np.zeros((500,500,3))
    img3 = np.zeros((500,500,3))
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    h, w, c = img.shape
    
    if results.multi_hand_landmarks: #พบมือในภาพ
        handLms = results.multi_hand_landmarks[0]
        
        handLms_x = [i.x for i in handLms.landmark]
        handLms_y = [i.y for i in handLms.landmark] 

        center_x = int(np.sum(handLms_x)/21*w)
        center_y = int(np.sum(handLms_y)/21*h)
        cv2.circle(img,(center_x,center_y),8,(0,255,255),-1)
 
        for i in range(0,21):
            handLms_x[i] = int(handLms_x[i]*w)
            handLms_y[i] = int(handLms_y[i]*h)
            
            cv2.circle(img,(handLms_x[i],handLms_y[i]),5,(255,255,255),-1)

            handLms_x[i] = handLms_x[i] - center_x + 250
            handLms_y[i] = handLms_y[i] - center_y + 250
            
            cv2.circle(img2,(handLms_x[i],handLms_y[i]),5,(255,255,255),-1)
            cv2.circle(img2,(250,250),8,(0,255,255),-1)
            
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
            
            cv2.circle(img3,(handLms_x[i],handLms_y[i]),5,(255,255,255),-1)
            cv2.circle(img3,(250,250),8,(0,255,255),-1)
            
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('l'):
            count_like = count_like + 1
            handLms_xy = handLms_x + handLms_y + ['like']
            with open(csv_filename,'a',encoding='UTF8',newline='') as f:
                writer_f = writer(f)
                writer_f.writerow(handLms_xy)
                f.close()
                print('like '+str(count_like))
                
        if key == ord('v'):
            count_love = count_love + 1
            handLms_xy = handLms_x + handLms_y + ['love']
            with open(csv_filename,'a',encoding='UTF8',newline='') as f:
                writer_f = writer(f)
                writer_f.writerow(handLms_xy)
                f.close()
                print('love '+str(count_love))   

        if key == ord('o'):
            count_ok = count_ok + 1
            handLms_xy = handLms_x + handLms_y + ['ok']
            with open(csv_filename,'a',encoding='UTF8',newline='') as f:
                writer_f = writer(f)
                writer_f.writerow(handLms_xy)
                f.close()
                print('ok '+str(count_ok))
                
        if key == ord('t'):
            count_two = count_two + 1
            handLms_xy = handLms_x + handLms_y + ['two']
            with open(csv_filename,'a',encoding='UTF8',newline='') as f:
                writer_f = writer(f)
                writer_f.writerow(handLms_xy)
                f.close()
                print('two '+str(count_two))
                
    cv2.imshow("img", img)
    #cv2.imshow("img2", img2)
    #cv2.imshow("img3", img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
