
import cv2 as cv
# img=cv.imread('Photos/cat_large.jpg')
# cv.imshow('cat',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)#frame.shape[1] is width of image
    height=int(frame.shape[0]*scale)#frame.shape[0] is height of image
    
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
# this is for video

capture= cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame= capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
