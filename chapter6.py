import cv2
import numpy as np

img = cv2.imread("Resources/nyny.jfif")
imgResize = cv2.resize(img,(400,350))

imgHor = np.hstack([imgResize,imgResize])
imgVer = np.vstack([imgResize,imgResize])

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)