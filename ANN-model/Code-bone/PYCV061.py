import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
  
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            print("Ignoring empty camera frame.")
            continue
          
        img = cv2.flip(img,1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        img.flags.writeable = False
        results = pose.process(img)

        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        cv2.imshow('img', img)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()
