import cv2
import numpy as np

img=cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\starwars.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\who.png",0)
w,h=template.shape[::-1]


result = cv2.matchTemplate(grey,template,cv2.TM_CCOEFF_NORMED)
print(result)

threshold=0.7
location=np.where(result>=threshold)
print(location)

for i in zip(*location[::-1]):
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)

cv2.imshow("Result",result)
cv2.imshow("Template",template)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
