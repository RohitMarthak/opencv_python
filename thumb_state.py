import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success,img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            cx4, cy4, cx5, cy5 = 0, 0, 0, 0
            for id,lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 4:
                    cy4 = cy

                if id == 5:
                    cy5 = cy

                if id == 8:
                    cy8 = cy

            threshold = cy8 - cy4
            if threshold > 80:
                cv.putText(img, "UP", (200, 70), cv.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)
            else:
                cv.putText(img, "DOWN", (200, 70), cv.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_DUPLEX, 3, (255, 0, 255), 3)

    cv.imshow("image", img)
    if cv.waitKey(1) == ord('q'):
        break
