#adaptive thresholding
import cv2
import numpy as np


img=cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\2.jpeg",0)

#threshold A(x,y) t(x,y) B(x,y)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("Image",img)
cv2.imshow("TH1",th1)
cv2.imshow("TH2",th2)



cv2.waitKey(0)
cv2.destroyAllWindows()




















