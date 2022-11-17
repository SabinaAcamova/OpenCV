import numpy as np
import cv2

img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\jesse.jpg",1)
img1 =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\skyler.jpg",1)

img =cv2.resize(img,(520,520))
img1=cv2.resize(img1,(520,520))
#dst=cv2.add(img,img1)

dst=cv2.addWeighted(img,.9,img1,.4,0)

cv2.imshow("Window",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
