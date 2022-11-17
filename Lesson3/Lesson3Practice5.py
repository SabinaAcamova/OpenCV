import numpy as np
import cv2

#img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\jesse.jpg",1)
img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\walterskyler.jpg",1)
#print(img.shape)  (494, 500, 3)

#jessehead = img[139:228,165:281] #y-89 x-116
#janehead = img[103:211,34:134] #y-108 x-100

#skylerhead = img[74:199,392:487] #y-125 x-95
walterhead = img[79:216,821:909] #y-137 x-88

#img[103:192,34:150] = jessehead
#img[139:247,165:265] = janehead

#img[79:204,821:916] = skylerhead
img[74:211,392:480] = walterhead

cv2.imshow("Window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


