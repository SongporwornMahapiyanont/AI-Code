import cv2
import mediapipe as mp

pose = mp.solutions.pose.Pose()

img = cv2.imread('sitdown.png')
#img = cv2.imread('standup.png')

font = cv2.FONT_HERSHEY_SIMPLEX

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = pose.process(imgRGB)

h, w, c = img.shape

if results.pose_landmarks:
    poseLms = results.pose_landmarks
    mp.solutions.drawing_utils.draw_landmarks(img,poseLms,mp.solutions.pose.POSE_CONNECTIONS)

    point24 = poseLms.landmark[24]
    cx24, cy24 = int(point24.x*w), int(point24.y*h)

    point26 = poseLms.landmark[26]
    cx26, cy26 = int(point26.x*w), int(point26.y*h)

    cv2.line(img,(cx24,cy24),(cx26,cy26),(0,255,0),8)
    
    cv2.circle(img,(cx24,cy24),8,(0,255,255),-1)
    cv2.circle(img,(cx26,cy26),8,(255,0,0),-1)

    dt_24_26 = abs(point24.y-point26.y)*100
    print(dt_24_26)

    if dt_24_26 < 10:
        cv2.putText(img,"Sit down",(50,50),font,1.5,(0,180,100),5)
    else:
        cv2.putText(img,"Stand up",(50,50),font,1.5,(0,200,255),5)
        
    
cv2.imshow('img', img)
  
cv2.waitKey()
cv2.destroyAllWindows()
