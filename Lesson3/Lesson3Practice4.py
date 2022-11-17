import cv2
import numpy as np


def click_event(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY= str(x) + ","+ str(y)
        cv2.circle(img,(x,y),1,(0,0,255),-1)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,255),2)
        cv2.imshow("Window", img)
    
         

#img= img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\jesse.jpg",1)
img= img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\walterskyler.jpg",1)
cv2.imshow("Window",img)
cv2.setMouseCallback("Window",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
















