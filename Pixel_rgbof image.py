import cv2
import numpy as np
#addrs = input("Enter image address")
img =  np.zeros((700,700,3),np.uint8) #img = cv2.imread(addrs) 
def Mouse_events(event,x,y,flag, p):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        s = '.'+str(img[x,y,2])+','+str(img[x,y,1])+','+str(img[x,y,0])
        cv2.putText(img,s,(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(200,100,50),1)
cv2.namedWindow("BGR")
cv2.setMouseCallback("BGR",Mouse_events)
while True:
    cv2.imshow("BGR", img)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()
    
