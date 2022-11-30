import cv2
import numpy as np
from matplotlib import pyplot as plt


img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\smarties.png",0)
_,mask = cv2.threshold(img, 220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=3)
erosion = cv2.erode(mask,kernal,iterations=3)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) #ilk erosion sora dilation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernal) #dilation, erosion
ng = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)


titles = ["image","binary","dilation","erosion","opening","closing","gradient","tophat"]
images = [img, mask, dilation,erosion,opening,closing,ng,th]



for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])

plt.show()




