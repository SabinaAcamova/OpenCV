import numpy as np
import cv2

#bitwise op and or xor not

img1=np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(384,0),(510,123),(255,255,255),-1)
img2 =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\forpractice7_1.png",1)
img1 =cv2.resize(img1,(520,520))
img2=cv2.resize(img2,(520,520))
#bitAnd=cv2.bitwise_and(img1,img2)
#bitOr=cv2.bitwise_or(img1,img2)
#bitXor=cv2.bitwise_xor(img1,img2)
bitNot1=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)

cv2.imshow("W1",img1)
cv2.imshow("W2",img2)
#cv2.imshow("Window",bitAnd)
#cv2.imshow("Window",bitOr)
#cv2.imshow("Window",bitXor)
cv2.imshow("bitnot1",bitNot1)
cv2.imshow("bitnot2",bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()

