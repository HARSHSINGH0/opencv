import cv2 as cv
import numpy as np
img=cv.imread('photos/cat.jpg',0)
#here ret is return value sometime it is placed as "_"
ret, thresh1 = cv.threshold(img,50,255,cv.THRESH_BINARY) 
ret, thresh2 = cv.threshold(img,50,255,cv.THRESH_BINARY_INV) 
ret, thresh3 = cv.threshold(img,50,255,cv.THRESH_TRUNC) 
ret, thresh4 = cv.threshold(img,50,255,cv.THRESH_TOZERO) # here if the pixel value is less then 50 then the pixel assigned will be zero
ret, thresh5 = cv.threshold(img,50,255,cv.THRESH_TOZERO_INV) #here if the pixel value is more than 50 then it will be set as zero
  
 
cv.imshow('Binary Threshold', thresh1) 
cv.imshow('Binary Threshold Inverted', thresh2) 
cv.imshow('Truncated Threshold', thresh3) 
cv.imshow('Set to 0', thresh4) 
cv.imshow('Set to 0 Inverted', thresh5) 

cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()