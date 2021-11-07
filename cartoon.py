#-----------------------GENERAL IMPORTS----------------------
import cv2
import cvzone
import numpy as np
import os

#SETTING GENERAL WINDOW SETTINGS
cap = cv2.VideoCapture(0)
cap.set(3, 640) #640 is for width
cap.set(4, 480) #480 is for height
fpsReader = cvzone.FPS() #gets the FPS of the current frames displayed

#WRITING VIDEO/OUTPUT
frame_width = int(cap.get(3))
print(frame_width)
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
result = cv2.VideoWriter('output_final.mp4', fourcc, 20.0, (frame_width,frame_height))

#-----------------------MAIN WHILE LOOP----------------------

while True:

    #GETTING FRAMES AND ROI
    success, img = cap.read()
    img = cv2.resize(img, (640, 480))
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = cv2.medianBlur(grey, 5) #blurring image
    edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9) #threshold value is calculated for smaller regions

    # cartoonize
    color = cv2.bilateralFilter(img, 9, 250, 250) #noise-reducing smoothing filter
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imshow("image", cartoon)
    result.write(cartoon)

    #ESCAPE CRITERIA
    k = cv2.waitKey(33)
    if k == 27:  # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue

cap.release()
result.release()
cv2.destroyAllWindows()

'''
#TESTING ON SINGLE IMAGE

import cv2
import cvzone
import numpy as np
from tkinter.filedialog import *

#photo = askopenfilename()
img = cv2.imread('C:/Users/Tarun/Desktop/comp/pycharm/cartoon-effect/20200726_120449-1.jpg')
img=cv2.resize(img,(480,480))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)
imgStack = cvzone.stackImages([img, cartoon], 2,1)
cv2.imshow("Stack", imgStack)
#cv2.imshow("Cartoon", cartoon)

#save
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()'''