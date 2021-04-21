import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/rohan.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces :
    cv2.rectangle(imgGray,(x,y),(x+w,y+h),(255,0,0),1)

cv2.imshow("face",img)
cv2.waitKey(0)
