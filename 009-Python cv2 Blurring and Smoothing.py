import cv2
import numpy as np

cap= cv2.VideoCapture('yaar.mp4')

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue sat value
    lower_red = np.array([120,110,40])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)
    blur = cv2.GaussianBlur(res, (15,15),0)
    median = cv2.medianBlur(res,15)
    bailateral = cv2.bilateralFilter(res,15,75,75)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.imshow('smoothed',smoothed)
    #cv2.imshow('blur',blur)
    cv2.imshow("medias",median)
    #cv2.imshow('bailateral',bailateral)



    k = cv2.waitKey(0) & 0xFF
    if k== 27:
        break

cv2.destroyAllWindows()
cap.release()
