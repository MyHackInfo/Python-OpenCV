import cv2
import numpy as np

cap = cv2.VideoCapture('11.mp4')

while True:
    # Simple video read 
    ret , frame = cap.read()
    # Some view change
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Show videos
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
