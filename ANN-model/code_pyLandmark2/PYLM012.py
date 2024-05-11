import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

hands = mp.solutions.hands.Hands(max_num_hands=3)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):    
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks: #พบมือในภาพรึเปล่า
        #print(len(results.multi_hand_landmarks))
        for handLms in results.multi_hand_landmarks:
            #print(handLms)
            mp.solutions.drawing_utils.draw_landmarks(img,handLms,mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow("img", img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
