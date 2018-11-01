import cv2
import numpy as np

im1 = cv2.imread('98.png')
retval , threshold = cv2.threshold(im1 , 12 ,255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(im1 ,cv2.COLOR_BGR2GRAY)
retval2 ,threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) # good for low light image
retval2,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Bad

cv2.imshow("ori",im1)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('GAUS',gaus)
cv2.imshow('otsu',otsu)


cv2.waitKey(0)
cv2.destroyAllWindwo()
