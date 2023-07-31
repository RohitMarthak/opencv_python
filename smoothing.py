import cv2 as cv

img = cv.imread("images/cat2.jpg")
cv.imshow("Cat",img)

#Averaging
average = cv.blur(img,(7,7))
cv.imshow("Average Blur",average)

#Gaussian Blur
blur = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian Blur",blur)

#median blur
median = cv.medianBlur(img,3)
cv.imshow("Median blur",median)

#bilateral
bilateral = cv.bilateralFilter(img,5,35,25)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)