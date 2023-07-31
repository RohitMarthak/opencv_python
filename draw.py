import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")
#cv.imshow("Blank",blank)
img = cv.imread("images/download.jpg")
#cv.imshow("Starry_night",img)

#1.paint image a certain color
#blank[200:300,300:400] = 255,0,0
#cv.imshow("Blue",blank)

#2.draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1] // 2,blank.shape[0] // 2),(0,255,0),thickness=-1)
cv.imshow("Rectangle",blank)

#3.draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255),thickness=-1)
cv.imshow("Circle",blank)

#4. draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=3)
cv.imshow("Line",blank)

#5.write a text
cv.putText(blank,"Rohit",(300,300),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0))
cv.imshow("Text",blank)


cv.waitKey(0)
cv.destroyAllWindows()