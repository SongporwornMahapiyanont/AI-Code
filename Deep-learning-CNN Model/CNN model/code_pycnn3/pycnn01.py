import cv2

img = cv2.imread("dog.jpg") #BGR

print(img.shape)     #(h,w,channel)

cv2.imshow("input",img)

cv2.waitKey()

cv2.destroyAllWindows()
