import cv2 as cv
import numpy as np

img = cv.imread("images/cat4.jpg")
cv.imshow("Cat",img)

img2 = cv.imread("images/cat2.jpg")

blank = np.zeros(img.shape[:2],dtype = "uint8")
cv.imshow("Blank",blank)

circle = cv.circle(blank.copy(),(blank.shape[1] // 2,blank.shape[0] // 2),100,255,-1)
cv.imshow("Circle",circle)

rectangle = cv.rectangle(blank.copy(),(blank.shape[0] // 4,blank.shape[1] // 4),(3*blank.shape[0] // 4, 3*blank.shape[1] // 4),255,-1)
cv.imshow("rectangle",rectangle)

masked_img = cv.bitwise_and(img,img,mask=circle)
cv.imshow("Masked Image",masked_img)

cv.waitKey(0)