import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

count = 801
play = 0

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)
   
    x = 300
    y = 100
    w = 250
    h = 250      
    
    if play == 1:
        filesave = str(count)+".jpg"
        imgcut = img.copy()[y:y+h,x:x+w]
        cv2.imwrite('dataset_06_raw\\'+filesave,imgcut)
        print(filesave)
        count = count + 1
        
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)    
    cv2.imshow("img",img)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        play = 1
    if cv2.waitKey(1) & 0xFF == ord('e'):
        play = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


