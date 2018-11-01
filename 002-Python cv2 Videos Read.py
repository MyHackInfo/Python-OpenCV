import cv2
import numpy as np

# Here you do two thing first capture videos with webcam and play put video(file name )
# We will put some image all so .
cap = cv2.VideoCapture('Koala.jpg')

while True:
    ret , frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
