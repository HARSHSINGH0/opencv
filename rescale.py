import cv2 as cv
img=cv.imread('Photos/cat_large.jpg')
cv.imshow('cat',img)
#capture= cv.VideoCapture(0,cv.CAP_DSHOW) this is for capturing live camera
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)#frame.shape[1] is width of image
    height=int(frame.shape[0]*scale)#frame.shape[0] is height of image
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
cv.waitKey(0)#it will wait for infinite amount of time before click i think
