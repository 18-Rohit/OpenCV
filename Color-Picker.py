import cv2 
import numpy as np
def Passer(x):
    pass
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("ColorPicker")
cv2.createTrackbar("ON/OFF","ColorPicker",0,1,Passer)
cv2.createTrackbar("r", "ColorPicker", 0, 255,Passer)
cv2.createTrackbar("g", "ColorPicker", 0, 255,Passer)
cv2.createTrackbar("b", "ColorPicker", 0, 255,Passer)
while True:
    cv2.imshow("ColorPicker",img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    switch = cv2.getTrackbarPos("ON/OFF","ColorPicker")
    r = cv2.getTrackbarPos("r","ColorPicker")
    g = cv2.getTrackbarPos("g","ColorPicker")
    b = cv2.getTrackbarPos("b","ColorPicker")
    if switch == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()