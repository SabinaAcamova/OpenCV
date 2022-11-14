import cv2
import numpy as np


def click_event(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY= str(x) + ","+ str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,255),2)
        
        
        cv2.imshow("Window", img)
    elif event==cv2.EVENT_RBUTTONDOWN:
        print(x,", ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY= str(x) + ","+ str(y)
        cv2.putText(img,strXY,(x,y),font,1,(0,0,255),2)

        cv2.imshow("Window", img)
         

img= np.zeros((512,512,3))
cv2.imshow("Window",img)
cv2.setMouseCallback("Window",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()



