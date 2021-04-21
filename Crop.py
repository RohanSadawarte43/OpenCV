import cv2
import numpy as np

img = cv2.imread("Resources/nyny.jfif")
width, height = 100,400
pts1 = np.float32([[452,222],[520,222],[452,483],[520,483]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("NY",img)
cv2.imshow("Cropped",imgOutput)
cv2.waitKey(0)
