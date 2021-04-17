import cv2
import numpy as np

#Gray Scale-Blur-Canny-Dilate-Erode
img = cv2.imread("Resources/nyny.jfif")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation   ,kernel,iterations=1)

cv2.imshow("Output",imgGray)
cv2.imshow("Output2",imgBlur)
cv2.imshow("Output3",imgCanny)
cv2.imshow("Output4",imgDilation)
cv2.imshow("Output5",imgEroded)

cv2.waitKey(0)