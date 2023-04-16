#INITIAL SETUP
#----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os
folderPath='frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0] # read frames\img 1 in the intro variable
kill = graphic[1] # read frames\img 2 in the kill variable
winner = graphic[2]  # read frames\img 3 in the winner variable
cam = cv2.VideoCapture(0) #read the camera
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
#sets the minimum confidence threshold for the detection

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
sqr_img = cv2.imread('img/sqr(2).png') # read img\sqr (1) in the sqr_img variable
mlsa = cv2.imread('img/mlsa.png')  # read img\mlsa in the mlsa variable
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       #show the loss screen from the kill image read before
       cv2.imshow('Dalgona Cookie Cut', cv2.resize(kill, (0,0), fx=0.75, fy=0.75))
    while True:
        #show the loss screen from the kill image read before and end it after we press q
        cv2.imshow('Dalgona Cookie Cut', cv2.resize(kill, (0, 0), fx=0.75, fy=0.75))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

else:
#WIN SCREEN
#show the win screen from the winner image read before
    cv2.imshow('Dalgona Cookie Cut', cv2.resize(winner, (0, 0), fx=0.75, fy=0.75))

    while True:
        #show the win screen from the winner image read before and end it after we press q
        cv2.imshow('Dalgona Cookie Cut', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

#destroy all the windows
cv2.destroyAllWindows()
