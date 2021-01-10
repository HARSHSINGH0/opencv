import cv2 as cv
import numpy as np
img1=cv.imread("photos/cat.jpg")
img=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(img,127,255,0)
contours,hierarchy=cv.findContours(thresh,cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)
print("number of contours= "+str(len(contours)))
print(contours[0:-1])
cv.drawContours(img1,contours,-1,(13, 221, 223),2)#if we give -1 in contourindex then it will show all contours
cv.imshow("Image",img1)
cv.imshow("Image Gray",img)
cv.waitKey(0)
cv.destroyAllWindows()