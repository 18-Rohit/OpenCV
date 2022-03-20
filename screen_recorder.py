import cv2
import pyautogui as pag
import numpy as np
import time
rs = pag.size()
fn = "Record.avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(fn, fourcc, 20, rs)
cv2.namedWindow("Recording...",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording...",(1000,700))
time.sleep(2)
while True:
    ss = pag.screenshot()
    frame = np.array(ss)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    cv2.imshow("Recording...",frame)
    if cv2.waitKey(1) == ord('e'):
        break
output.release()    
cv2.destroyAllWindows()