import cv2 as cv
import numpy as np

blank = np.zeros((400,400,3),dtype="uint8")
circle = cv.circle(blank.copy(),(200,200), 200,255,-1)

cv.imshow("Circle",circle)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv.imshow("Rectangle",rectangle)

#bitwise AND
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("AND",bitwise_and)

#bitwise or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("OR",bitwise_or)

#bitwise xor
bitwise_xor =  cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",bitwise_xor)

#bitwise not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Rectangle NOT",bitwise_not)



cv.waitKey(0)