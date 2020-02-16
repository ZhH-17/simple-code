import cv2 as cv
import time
pnts = [[0, 0], [0, 0]]
times = 0

img1 = cv.imread("s1.png", -1)
img2 = cv.imread("zh.png", -1)

img1_copy = img1.copy()
img2_copy = img2.copy()

def onMouse(event, x, y, flags, param):
    global pnts, times
    global img2_copy
    if event == cv.EVENT_LBUTTONDOWN and times == 0:
        pnts[0][0] = x
        pnts[0][1] = y
        times += 1
    elif event == cv.EVENT_LBUTTONDOWN and times == 1:
        pnts[1][0] = x
        pnts[1][1] = y
        times += 1
    elif event == cv.EVENT_RBUTTONDOWN:
        if times>=1:
            times -= 1

    img2_copy = img2.copy()
    for i in range(times):
        cv.drawMarker(img2_copy, tuple(pnts[i]), [0, 0, 255], 1, 10, 1)

windowname = "img"
cv.namedWindow(windowname, cv.WINDOW_AUTOSIZE)

cv.setMouseCallback(windowname, onMouse)

while True:
    cv.imshow(windowname, img2_copy)
    key = cv.waitKey(10)
    if key == ord("s"):
        print(pnts[0][1], pnts[1][1])
        cv.imwrite("%d.png" %time.time(), img2[pnts[0][1]:pnts[1][1], :])
    elif key == 27:
        break
cv.destroyAllWindows()