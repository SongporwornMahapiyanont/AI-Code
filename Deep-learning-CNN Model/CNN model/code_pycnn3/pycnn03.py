import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(img,"Sopon",(20,200),font,3,(255,255,0),5)

    a = 20
    cv2.putText(img,str(a),(80,300),font,2,(0,255,255),5)
    
    b = 31.56
    textout = "Dist = " + str(b) + " cm"
    cv2.putText(img,textout,(50,400),font,2,(0,255,0),5)
    
    cv2.imshow("img",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


