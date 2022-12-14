import cv2
import numpy as np

img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\logo.jpeg")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,200,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours"+str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,0),2)





cv2.imshow("Img",img)
cv2.imshow("Imgray",imgray)
cv2.imshow("Thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()