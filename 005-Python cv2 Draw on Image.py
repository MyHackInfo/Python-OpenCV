import numpy as np
import cv2

img = cv2.imread('Koala.jpg',cv2.IMREAD_COLOR)

# Draw show thing
# line
cv2.line(img,(0,0),(150,150),(255,255,255),15)
# Rectangle
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
# Circle
cv2.circle(img , (100,63),55, (0,0,255),1) # use -1 for fill and use 1 without fill
# Polylines
pts = np.array([[100,55],[230,330],[720,220],[520,140]],np.int32)
cv2.polylines(img,[pts],False,(0,252,125),5)

# Put Text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Open CV ',(110,400),font,6,(20,21,111),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
