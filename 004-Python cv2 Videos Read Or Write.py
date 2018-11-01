import cv2
import numpy as np

cap = cv2.VideoCapture('11.mp4')
# Write video
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi',fourcc , 20.0 ,(640,280))

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Write videos
    out.write(frame)

    # Show videos
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
