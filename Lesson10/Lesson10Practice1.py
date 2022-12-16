import cv2
import numpy as np

img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\shapes.jpeg")
imgGrey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,threshold=cv2.threshold(imgGrey,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,255,0),5)
    
    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx)==3:
        cv2.putText(img,"triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectRatio=float(w)/h
        print(aspectRatio)
        
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img,"4b",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        else:
            cv2.putText(img,"duzb",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    elif len(approx)==5:
        cv2.putText(img,"5b",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
    else:
        cv2.putText(img,"daire",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)



cv2.imshow("Shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


