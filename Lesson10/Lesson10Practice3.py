import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg")

b,g,r=cv2.split(img)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
