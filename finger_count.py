import cv2 as cv
import mediapipe as mp
import numpy as np

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpdraw = mp.solutions.drawing_utils

finger_tips = [8,12,16,20]

while True:
    success,img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    heights = np.zeros((21,), dtype=int)
    widths = np.zeros((21),dtype=int)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                finger_count = []
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                mpdraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
                # cv.putText(img,str(id),(cx,cy),cv.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0),1)
                heights[id] = cy
                widths[id] = cx
                # print(heights)
            for i in range(0,4):
                if(heights[finger_tips[i]-2]>heights[finger_tips[i]]):
                    finger_count.append(1)

                else:
                    finger_count.append(0)

            if(widths[4]-widths[2] > 30):
                finger_count.append(1)
            else:
                finger_count.append(0)

            print(finger_count)
            count = finger_count.count(1)
            cv.putText(img,"Fingers count:"+str(count),(img.shape[0]-200,50),cv.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2)

    cv.imshow("Image",img)
    if cv.waitKey(1) == ord("q"):
        break