import cv2
import numpy as np


img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg")
layer=img.copy()

gp=[layer] # gaussianin neticeleri

for i in range(2):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

layer = gp[2]
lp =[layer]

for i in range(2,0,-1):
    gaussian_ex=cv2.pyrUp(gp[i])
    cv2.imshow("Gaussian Ex"+str(i),gaussian_ex)
    laplacian = cv2.subtract(gp[i-1],gaussian_ex)
    cv2.imshow("Lap Pyr Level"+str(i),laplacian)


cv2.imshow("Original",img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()