import cv2 #python-opencv
import numpy as np
import mediapipe as mp
import time
import os
import math
import keyboard
import pyautogui
import numpy as np




# Подключаем камеру
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Lenght
cap.set(10, 100)  # Brightness

mpHands = mp.solutions.hands
hands = mpHands.Hands(False)
npDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
i=0
p=0


# Зацикливаем получение кадров от камеры
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror flip

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, lm)
                if id == 4 :
                    cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
                    id8x= lm.x *w
                    id8y= lm.y* w

                if id==8:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 0), cv2.FILLED)
                    id12x= lm.x* w
                    id12y= lm.y*w




            res_x= id12x-id8x
            res_y = id12y - id8y
            ras=int(math.sqrt(res_x**2+res_y**2))
            #cel_ras= int(ras)


            # print("x", abs(res_x))
            # print("y", abs(res_y))
            #print(ras)

            if ras<=50:
                if i==1:
                    break
                else:
                    p=p+1
                    print(p)
                    keyboard.write("a")

                    i = 1
            else:
                i=0





    cv2.putText(img, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  # ФреймРейт

    cv2.imshow('python', img)
    if cv2.waitKey(20) == 27:  # exit on ESC
        break

cv2.destroyWindow("python")
cap.release()
cv2.waitKey(1)