import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import mediapipe as mp

face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)
drawing_spec = mp.solutions.drawing_utils.DrawingSpec(thickness=1,circle_radius=2)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()        
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(image=img,
                landmark_list=faceLms,
                connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)
            
    cv2.imshow('img', img)        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
cap.release()
cv2.destroyAllWindows()
