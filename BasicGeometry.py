import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:] = 200,200,0

cv2.line(img,(0,0),(400,400),(0,1000,0))
cv2.rectangle(img,(0,0),(200,200),(0,0,1000),cv2.FILLED)
cv2.circle(img,(200,200),50,(256,0,0),5)
cv2.putText(img, "Hello World", (250,250),cv2.FONT_ITALIC,1,(230,230,0))

cv2.imshow("image",img)
cv2.waitKey(0)
