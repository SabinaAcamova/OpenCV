#simple thresholding
import cv2
import numpy as np


img=cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\1.jpeg")

#threshold A(x,y) t(x,y) B(x,y)

_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("Image",img)
cv2.imshow("TH1",th1)
cv2.imshow("TH2",th2)
cv2.imshow("TH3",th3)
cv2.imshow("TH4",th4)
cv2.imshow("TH5",th5)


cv2.waitKey(0)
cv2.destroyAllWindows()





