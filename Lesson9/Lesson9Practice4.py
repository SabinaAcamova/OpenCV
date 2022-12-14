import cv2
import numpy as np

apple=cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\apple.jpeg")
orange = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\orange.jpeg")

print(apple.shape)
print(orange.shape)

apple_orange=np.hstack((apple[:,:256],orange[:,256:]))

cv2.imshow("Apple",apple)
cv2.imshow("Orange",orange)
cv2.imshow("MIX",apple_orange)

cv2.waitKey(0)
cv2.destroyAllWindows()


