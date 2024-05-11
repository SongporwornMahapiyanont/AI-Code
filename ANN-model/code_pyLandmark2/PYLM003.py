import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

cap = cv2.VideoCapture(0)

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print('frame_width = ',frame_width)
print('frame_height = ',frame_height)
print('fps = ',fps)

while True:
    ret, img = cap.read()
    img = cv2.flip(img,1) 

    key = cv2.waitKey(1)
    if (key == ord('q')) or (ret == False):
        break

    cv2.imshow('img',img)
    
print(img.shape) #(h,w,channel)

cv2.destroyAllWindows()
cap.release()
