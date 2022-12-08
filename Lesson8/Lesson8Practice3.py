import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\Lesson7\aaa.jpg")
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX=cv2.Sobel(img,cv2.CV_64F,dx=1,dy=0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY=cv2.Sobel(img,cv2.CV_64F,dx=0,dy=1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined=cv2.bitwise_or(sobelX,sobelY)

titles = ["image","lap","sobelX","sobelY","Combined"]
images = [img,lap,sobelX,sobelY,sobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.xticks([])
    plt.yticks([])

plt.show()