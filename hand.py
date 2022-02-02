import cv2
import mediapy as mp


camera = cv2.VideoCapture(0)

#mpHands= mp.solutiond.hands
#hands = mpHands.hands()
#mpDraw = mp.solutiond.drawing_utils

while True:
    good, img = camera.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    cv2.imshow("image", img)


    if cv2.waitKey(1) == ord('q'):
        break


