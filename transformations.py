import cv2 as cv
import numpy as np

img = cv.imread("images/cat2.jpg")

cv.imshow("Cat",img)

def tranlate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    print(transMat)
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2 , height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)


# -x --> Left
# -y -->Up
# x --> Right
# y --> Down

#translate
translated = tranlate(img,100,0)
cv.imshow("Translated",translated)

#rotating
rotated = rotate(img,-45)
cv.imshow("Rotated",rotated)

#resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

#flipping
flipped = cv.flip(img,0)

#cropping
cropped = img[200:400,300:400]
cv.imshow("Cropped",cropped)


cv.imshow("Flipped",flipped)



cv.waitKey(0)
cv.destroyAllWindows()
