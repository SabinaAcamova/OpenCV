import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\1.jpeg")

_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)

titles = ["Original image", "BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()

