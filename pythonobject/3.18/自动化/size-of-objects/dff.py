import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone
import random
import time

# Webcam
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand Detecter
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Find Function
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

# Game Variables
cx, cy = 250, 250
color = (255, 0, 255)
counter = 0
score = 0
timeStart = time.time()

totalTime = 30
# Loop
while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    hands, img = detector.findHands(img)
    # hands = detector.findHands(img,draw=False)
    if totalTime > time.time() - timeStart:
        if hands:
            lmlist = hands[0]['lmList']
            x, y, w, h = hands[0]['bbox']
            print(lmlist)
            x1, y1 = lmlist[5]
            x2, y2 = lmlist[18]

            distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
            A, B, C = coff
            distanceCM = A * distance ** 2 + B * distance + C

            cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 55, y - 30), scale=2)
            # print(distanceCM,distance)
            # cv.rectangle(img, (x,y), (x+w,y+h),(255,0,255), 3)

            if distanceCM < 40:
                if x < cx < x + w and y < cy < y + h:
                    counter = 1

        if counter:
            counter += 1
            color = (0, 255, 0)
            if counter == 3:
                score += 1
                cx = random.randint(100, 1100)
                cy = random.randint(100, 600)
                color = (255, 0, 255)
                counter = 0

        # Draw Bubtton
        cv.circle(img, (cx, cy), 30, color, cv.FILLED)
        cv.circle(img, (cx, cy), 10, (255, 255, 255), cv.FILLED)
        cv.circle(img, (cx, cy), 10, (255, 255, 255), 2)
        cv.circle(img, (cx, cy), 30, (50, 50, 50), 2)

        # Game HUB
        cvzone.putTextRect(img, f"Time: {int(totalTime - (time.time() - timeStart))}", (1100, 70), scale=2, offset=20)
        cvzone.putTextRect(img, f"Score: {str(score).zfill(2)}", (50, 70), scale=2, offset=20)
    else:
        cvzone.putTextRect(img, f"your Score is: {str(score).zfill(2)}", (500, 460), scale=2, offset=20)
        cvzone.putTextRect(img, "Game Over", (400, 400), scale=5, offset=30, thickness=7)
        cvzone.putTextRect(img, "Press R to restart", (500, 460), scale=2, offset=20)

    cv.imshow("Image", img)
    Key = cv.waitKey(1)

    if Key == ord('r'):
        timeStart = time.time()
        score = 0
