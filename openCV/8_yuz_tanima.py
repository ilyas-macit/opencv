#!/usr/bin/env python3
import cv2

faceCascade= cv2.CascadeClassifier("/home/ilyas/openCV/Learn-OpenCV-in-3-hours/Resources/haarcascade_frontalface_default.xml")
#img = cv2.imread('/home/ilyas/openCV/Learn-OpenCV-in-3-hours/Resources/lena.png')

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Result", frame)
    if cv2.waitKey(1) == ord("q"): break
    

