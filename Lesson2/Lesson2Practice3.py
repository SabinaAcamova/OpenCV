import cv2
import datetime
camera = cv2.VideoCapture(0)

print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

camera.set(3,600)
camera.set(4,444)

print(camera.get(3))
print(camera.get(4))

while(camera.isOpened()):
    ret,frame = camera.read()

    if ret == True:
        text = "Width: "+ str(camera.get(3))+"Height: "+str(camera.get(4))
        print(text)
        date=str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame=cv2.putText(frame,text,(10,50),font,1,(255,255,255),2,cv2.LINE_AA)
        frame=cv2.putText(frame,date,(10,100),font,1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow("window",frame)

        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break

camera.release()
cv2.destroyAllWindows()



