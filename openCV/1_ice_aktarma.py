#!/usr/bin/env python3

import cv2
######################## READ IMAGE ############################
def ImageRead():
    # # LOAD AN IMAGE USING 'IMREAD'
    img = cv2.imread("/home/ilyas/openCV/Learn-OpenCV-in-3-hours/Resources/lena.png")
    # DISPLAY
    cv2.imshow("Lena Soderberg",img)
    cv2.waitKey(0)

######################### READ VIDEO #############################

width = 640
height = 480
def VideoRead():
    cap = cv2.VideoCapture("/home/ilyas/openCV/Learn-OpenCV-in-3-hours/Resources/test_video.mp4")
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (width, height))
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
######################### READ WEBCAM  ############################

def VideoCap():
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    cap.set(10,150)
    while True:
        success, img = cap.read()
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#ImageRead()
VideoRead()
#VideoCap()