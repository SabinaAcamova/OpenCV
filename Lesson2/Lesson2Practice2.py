import cv2
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,400)
print(cap.get(3))#3 ID DEMEKDIR
print(cap.get(4))#4 ID DEMEKDIR

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow("window",frame)
        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break    


cap.release()
cv2.destroyAllWindows()


