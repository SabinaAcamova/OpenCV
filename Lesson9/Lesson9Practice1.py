import cv2
import numpy as np


img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg")

lr1= cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)

hr=cv2.pyrUp(img)



cv2.imshow("Orginal",img)
cv2.imshow("Layer1",lr1)
cv2.imshow("Layer2",lr2)

cv2.imshow("Higher",hr)




  
cv2.waitKey(0)
cv2.destroyAllWindows()


