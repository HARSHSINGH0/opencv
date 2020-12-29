import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
#np.unit8 gives value form 0 to 255 and 
# comma 3 gives three channels for colors(rgb)
#print(img.shape)
#img[:]=255,0,0 this will color full matrix to blue
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
cv.rectangle(img,(0,0),(250,350),(0,255,0),thickness=1)
cv.circle(img,(400,50),30,(255,0,0),thickness=2)
cv.putText(img," OPENCV BY HARSH ",(300,210),cv.FONT_HERSHEY_PLAIN,1.1,(255,255,255),thickness=1)
cv.imshow("Matrix image",img)


cv.waitKey(0)