import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
cv2=cv
def maskandcontours():
    while 1:
        _,frame=cap.read()
        blurred_frame=cv.GaussianBlur(frame,(5,5),0)
        hsv=cv.cvtColor(blurred_frame,cv.COLOR_BGR2HSV)
        lower_shade=np.array([0,50,50])#in opencv RGB is not concept
        upper_shade=np.array([10,255,255])#we use BGR
        mask0 = cv2.inRange(hsv, lower_shade, upper_shade)

        # upper mask (170-180)
        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        # join my masks
        mask = mask0+mask1
        # mask=cv.inRange(hsv,lower_shade,upper_shade)
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
#in this program i have given lower and upper range for red
