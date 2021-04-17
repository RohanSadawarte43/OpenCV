import cv2
import numpy as np

img = cv2.imread('Resources/nyny.jfif')
imgResize = cv2.resize(img,(300,200))
imgCropped = img[:500,200:800]

print(img.shape)
print(imgResize.shape)
print(imgCropped.shape)

cv2.imshow("Original", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)