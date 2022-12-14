import cv2
import numpy as np


img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg")
layer=img.copy()

gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

cv2.imshow("Original",img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()













