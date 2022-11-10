import cv2

camera=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter(r"C:\Users\User\Desktop\Artificial Intelligence\Lesson1\output.mp4",fourcc,20.0,(640,480))
print(camera.isOpened())

while camera.isOpened():
    ret,frame=camera.read()

    if ret==True:
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow("Window", gray)
        K=cv2.waitKey(1)


        if K==ord("q"):
            break
    else:
        break
camera.release()
out.release()
cv2.destroyAllWindows()

