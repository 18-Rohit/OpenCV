import cv2
import numpy as np
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def Passer(x):
    pass
cv2.namedWindow("ColorDetection")
cv2.createTrackbar("Lower_HUE","ColorDetection",0,255,Passer)
cv2.createTrackbar("Lower_Sat","ColorDetection",0,255,Passer)
cv2.createTrackbar("Lower_Value","ColorDetection", 0,255,Passer)

cv2.createTrackbar("Upper_HUE","ColorDetection", 255,255,Passer)
cv2.createTrackbar("Upper_Sat","ColorDetection", 255,255,Passer)
cv2.createTrackbar("Upper_Value","ColorDetection", 255,255,Passer)
while True:
    _,frame = cam.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("Lower_HUE","ColorDetection")
    ls = cv2.getTrackbarPos("Lower_Sat","ColorDetection")
    lv = cv2.getTrackbarPos("Lower_Value","ColorDetection")
    uh = cv2.getTrackbarPos("Upper_HUE","ColorDetection")
    us = cv2.getTrackbarPos("Upper_Sat","ColorDetection")
    uv = cv2.getTrackbarPos("Upper_Value","ColorDetection")
    lhsv = np.array([lh,ls,lv])
    uhsv = np.array([uh,us,uv])
    mask = cv2.inRange(hsv, lhsv, uhsv)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Cam",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result", result)
    k = cv2.waitKey(1)
    if k == 27:break
cam.release()
cv2.destroyAllWindows()