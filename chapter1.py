import cv2
import numpy as np

#Read image
'''
print("package imported")

img = cv2.imread("Resources/nyny.jfif")

cv2.imshow("output",img)
cv2.waitKey(0)
'''

#Read Video
'''cap = cv2.VideoCapture("Resources/q1.mkv")

while True :
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break'''

#Read Webcam
'''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)  
cap.set(10,10)

while True :
    success, img = cap.read()
    cv2.imshow("Cam",img)
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break
'''



