import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg",0)
"""
img=np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255,255,255),-1)
"""
cv2.imshow("lena",img)

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()











