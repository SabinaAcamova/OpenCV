import numpy as np
import cv2

def callback(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("image")
cv2.createTrackbar("Blue","image",0,255,callback)
cv2.createTrackbar("Green","image",0,255,callback)
cv2.createTrackbar("Red","image",0,255,callback)


cv2.createTrackbar("0:OFF\n 1:ON","image",0,1,callback)

while(1):

    cv2.imshow("image",img)

    k=cv2.waitKey(1)
    
    if k==27:
        break

    b=cv2.getTrackbarPos("Blue","image")
    g=cv2.getTrackbarPos("Green","image")
    r=cv2.getTrackbarPos("Red","image")
    s=cv2.getTrackbarPos("0:OFF\n 1:ON","image")

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv2.destroyAllWindows()


