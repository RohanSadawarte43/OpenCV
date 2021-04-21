import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        if peri > 300:
            area = cv2.contourArea(cnt)
            print(area)
            cv2.drawContours(imgContour,cnt,-1,(256,0,0),3)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect((approx))

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0.255,0),1)
            cv2.putText(imgContour,"Shape",(x+(w//2)-10,y+(h//2)-10),cv2.FONT_ITALIC,0.5,(0,0,0))




img = cv2.imread("Resources/shape2.jpg")
img = cv2.resize(img,(600,500))
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

imgBlank = np.zeros_like(img)

'''cv2.imshow("Shapes",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Blank",imgBlank)'''
getContours(imgCanny)
cv2.imshow("Contour",imgContour)
cv2.waitKey(0)
