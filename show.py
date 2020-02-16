import sys
print("sys: ", sys.executable)
import cv2 as cv
import os
import numpy as np

mat = np.random.random((300,400))
s = np.sqrt(1+3+2*49+2**4) - 190*21
filepath = "../../Pictures/p2180350656.jpg"
imgpath = "../../Pictures/honor 5c/"
print("what")
cv.namedWindow("img")
img = (255*mat).astype(np.uint8)
cv.imshow("img", img)  
cv.waitKey(-1)