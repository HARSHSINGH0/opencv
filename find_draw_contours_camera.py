import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
cv2=cv
def maskandcontours():
    while 1:
        _,frame=cap.read()
        blurred_frame=cv.GaussianBlur(frame,(5,5),0)
        hsv=cv.cvtColor(blurred_frame,cv.COLOR_BGR2HSV)
        # lower_shade=np.array([1,86,38])
        # upper_shade=np.array([255,255,121])
        lower_shade=np.array([38,86,0])
        upper_shade=np.array([121,255,255])
        mask=cv.inRange(hsv,lower_shade,upper_shade)
        contours,hierachy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        cv.drawContours(frame,contours,-1,(0,255,0),3)
        cv.imshow("Frame",frame)
        cv.imshow("Mask",mask)
        key=cv.waitKey(1)
        if(key==27):
            break
maskandcontours()
cap.release()
cv.destroyAllWindows()

#this program will only work for given rgb 
#in this program i have given lower and upper range for green and blue
