import numpy as np
import cv2

img = np.zeros([512,512,3]) # 0-dan ibaret bir 1 array emele getirir



#img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg",1)

img = cv2.line(img,(0,0),(255,255),(0,255,0),5)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,0,0),15 )
img = cv2.rectangle(img,(384,0),(510,123),(255,255,255),-1)
img = cv2.circle(img,(333,444),63,(0,0,0),5)

font=cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"openCV",(10,300),font,4,(255,255,0),10,cv2.LINE_AA)

cv2.imshow("Window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

