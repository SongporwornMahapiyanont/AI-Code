import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.flip(img,1) 

    key = cv2.waitKey(1)
    if (key == ord('q')) or (ret == False):
        break

    cv2.line(img,(50,50),(200,200),(0,255,0),5)         #color(BGR)
    cv2.rectangle(img,(200,50),(250,150),(0,0,255),10)
    cv2.circle(img,(300,300),50,(255,0,255),3)
    cv2.circle(img,(50,150),30,(0,255,255),-1) #ใส่ -1 ทึบ
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"Hello",(20,300),font,1.5,(255,255,0),3)
    
    cv2.imshow('img',img)
         
cv2.destroyAllWindows()
cap.release()
