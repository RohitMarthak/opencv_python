import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_cascades/frontal_face.xml')
cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(grayFrame,scaleFactor=1.1,minNeighbors=3)

    print(f'number of faces found in this image = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow('Detected face',frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()