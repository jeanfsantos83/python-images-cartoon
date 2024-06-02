# pip install opencv-python #
# pip install numpy #
from cv2 import cv2
import numpy as np

# Upload Image #
img = cv2.imread(r'dog.jpg')

# Pass parameters to Lib #
gray = cv2.cvtColor(img, cv2.COLOR_BRG2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_TRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Cartoon the Image #
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Show Images #
cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(8)
cv2.destroyAllWindows()
