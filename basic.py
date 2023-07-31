import cv2 as cv

img = cv.imread("images/cat2.jpg")
cv.imshow("Cat",img)

#1.converting to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#2.blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#3.Edge Cascade
canny = cv.Canny(blur,125,175)
cv.imshow("Canny",canny)

#4.dilating the image
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow("Dilated",dilated)

#5.Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("Eroded",eroded)

#6.Resize
resized = cv.resize(img,(225,225),interpolation=cv.INTER_CUBIC)
cv.imshow("Resize",resized)

#7.Crop
cropped = img[0:500,200:800]
cv.imshow("cropped",cropped)

cv.waitKey(0)
cv.destroyAllWindows()
