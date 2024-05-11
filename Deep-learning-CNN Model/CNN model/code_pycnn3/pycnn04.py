import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)

    x = 300
    y = 100
    w = 250
    h = 250
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    
    cv2.imshow("img",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


