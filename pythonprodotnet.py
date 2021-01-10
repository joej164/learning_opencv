# https://pythonprogramming.net/loading-images-python-opencv-tutorial/
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('iron_qty.png', cv2.IMREAD_GRAYSCALE)

# Show in image program
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Show in matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
# plt.show()

cv2.imwrite('iron_qty_grey.png', img)
exit()

# cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
# cv2.rectangle(img, (15, 25), (200, 150), (0, 0, 255), 15)

# cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0, 130), font,
            1, (200, 255, 155), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
