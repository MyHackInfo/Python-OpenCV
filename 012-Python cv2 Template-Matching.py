import cv2
import numpy as np

img1 = cv2.imread('Peng.jpg')
img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

template = cv2.imread('match.png')
w, h,v = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)
threshold = 0.90
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_gray,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

cv2.imshow('detected',img1)
