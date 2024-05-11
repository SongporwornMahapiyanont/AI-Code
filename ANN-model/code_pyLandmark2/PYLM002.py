import cv2

cap = cv2.VideoCapture('traffic.mp4')
# 30 fps
# 1s = 1000 ms / 30ภาพ = 33.33333 = 33 ms

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print('frame_width = ',frame_width)
print('frame_height = ',frame_height)
print('fps = ',fps)
print('num_frame = ',num_frame)

while True:
    ret, img = cap.read()
    
    key = cv2.waitKey(33) #ms
    if (key == ord('q')) or (ret == False):
        break
    
    cv2.imshow('img',img) 

cv2.destroyAllWindows()
cap.release()
