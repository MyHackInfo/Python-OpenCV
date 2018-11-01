import cv2
import numpy as np
import matplotlib.pyplot as plt

# This cv2.imread function use for image read    
img = cv2.imread('Koala.jpg',cv2.IMREAD_GRAYSCALE)

# imshow() use for show image 
cv2.imshow('image',img)
cv2.witKey(0)
cv2.destroyAllWindows()

# Show on matplotlib using plt.imshow
##plt.imshow(img , cmap='gray',interpolation='bicubic')
##plt.show()

# Image write
#cv2.imwrite('animal.png',img)
