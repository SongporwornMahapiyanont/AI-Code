import cv2
import mediapipe as mp

pose = mp.solutions.pose.Pose()

cap = cv2.VideoCapture('jump.mp4')

while True:
    ret, img = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or (ret == False):
        break
    
    img = cv2.flip(img,1)
        
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        poseLms = results.pose_landmarks
        mp.solutions.drawing_utils.draw_landmarks(img,poseLms,mp.solutions.pose.POSE_CONNECTIONS)
        
    cv2.imshow('img', img)
            

    
cap.release()
cv2.destroyAllWindows()
