import cv2

img = cv2.imread('beach.jpg') #BGR

print(img.shape) #(h,w,channel)
print(img.shape[0:2]) #(h,w) 0 1
print(img.shape[::-1]) #(channel,w,h)
print(img.shape[::-1][1:3]) #(w,h) 1 2
print(img.shape[1::-1]) #(w,h)

cv2.imshow('input',img)

cv2.waitKey()

cv2.destroyAllWindows()
