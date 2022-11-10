import cv2
img =cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\lena.jpg",0)
cv2.imshow("Window",img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite(r"C:\Users\User\Desktop\Artificial Intelligence\lena_grayscale.jpg",img)
    cv2.destroyAllWindows()
