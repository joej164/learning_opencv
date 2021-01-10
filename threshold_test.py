import cv2
import numpy as np

img = cv2.imread('iron_qty.png')
retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#cv2.imshow('original', img)
cv2.imwrite('iron_qty_thresh.png', threshold)
