import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp
import numpy as np

selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = selfie_segmentation.process(img)
    mask = results.segmentation_mask
    condition = np.stack((mask,) * 3, axis=-1) > 0.7

    bg_image = np.zeros(img.shape, dtype=np.uint8)
    bg_image[:] = (192, 192, 192) # gray
    output_image = np.where(condition, img, bg_image)

    cv2.imshow('input_image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('output_image', output_image)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
