import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, img = cap.read()
    img = cv2.flip(img,1)

    cv2.imshow("img",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("testsave.jpg",img)
        print(img.shape)
        break

cap.release()
cv2.destroyAllWindows()


