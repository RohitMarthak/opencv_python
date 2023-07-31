import cv2 as cv
import numpy as np

blank = np.zeros((1000,1000,3),dtype="uint8")
circle = cv.circle(blank.copy(),(200,200), 100,255,-1)

def circle_movement(i,j,img):
    new_img = cv.circle(blank.copy(),(i,j), 100,255,-1)
    return new_img

for i in range(200,801):
    for j in range(200,801):
        img = circle_movement(i,j,circle)
        cv.imshow("Circle",img)

cv.waitKey(0)