# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:14:30 2020

@author: zhang
"""
import cv2 as cv
import time
pnts = [[0, 0], [0, 0]]
times = 0

img1 = cv.imread("nx.png", -1)
rep = cv.imread("rep.png", -1)
img1[536:613, :] = rep
cv.imwrite("test.png", img1)
