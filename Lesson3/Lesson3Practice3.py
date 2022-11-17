import numpy as np
import cv2

img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\skyler.jpg",1)

print(img.shape) #setirlerin,sutunlarin ve reng kanallarinin sayini return edir
print(img.size) #sekildeki butun pixellerin sayini verir
print(img.dtype) #foto/sekil data tipini return edir

b,g,r =cv2.split(img)   #split 3 deger return edir

img1=cv2.merge((b,g,r)) #birlesdirir

cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)

cv2.imshow("Merge",img1)
#cv2.imshow("Window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



