import cv2 as cv
import numpy as np
kernel =np.ones((5,5),np.uint8)
img2=cv.imread('Photos/park.jpg')
img=cv.resize(img2,(384,216))
imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur=cv.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv.Canny(img,100,100)
imgDialation=cv.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv.erode(imgDialation,kernel,iterations=1)
imgCropped=img[0:216,50:300]#value of y axis first then x



cv.imshow("Normal image",img)
cv.imshow("Gray image",imgGray)
cv.imshow("Blur image",imgBlur)
cv.imshow("Canny image",imgCanny)
cv.imshow("Dialation image",imgDialation)
cv.imshow("Eroded image",imgEroded)
cv.imshow("Cropped image",imgCropped)
cv.waitKey(0)
# cap=cv.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     success, img=cap.read()
#     cv.imshow('Video',img)
#     if cv.waitKey(1) & 0xFF==ord('q'):
#         break# 
# while True:
#     success, img=cap.read()
#     imgBlur=cv.imshow(img)
#     cv.imshow('Video',imgBlur)
#     if cv.waitKey(1) & 0xFF==ord('q'):
#         break