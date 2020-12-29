import cv2 as cv
import numpy as np
img=cv.imread("Photos/cards.png")
width,height=250,350
#361,82   265,285  403,385  500 148
pts1=np.float32([[361,82],[265,285],[403,385],[500,148]])
pts2=np.float32([[0,0],[height,0],[0,width],[height,width]])
matrix=cv.getPerspectiveTransform(pts1,pts2)
imgOutput=cv.warpPerspective(img,matrix,(width,height))
cv.imshow("cards image",img)
cv.imshow("Ouput",imgOutput)
cv.waitKey(0)