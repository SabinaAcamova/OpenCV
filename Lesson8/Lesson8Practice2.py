import cv2
import numpy as np


cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    canny=cv2.Canny(frame,30,200)
    cv2.imshow("Canny Edge Detector", canny)

    if cv2.waitKey(1)==27:
        break

cap.release
cv2.destroyAllWindows()














