import cv2 as cv

img = cv.imread("images/cat2.jpg")
cv.imshow("Cat",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("LSV",lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

#HSV to BGR
bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV-->BGR",bgr)


cv.waitKey(0)