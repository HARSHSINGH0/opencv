import cv2
image = cv2.imread("photos/cat.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(gray_image, 127, 255, 0)
cv2.imread(threshold_image, "Black & White doggo")