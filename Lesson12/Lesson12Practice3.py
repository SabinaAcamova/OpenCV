import matplotlib.pylab as plt 
import cv2
import numpy as np 

def region_of_interest(img,vertices):
    mask= np.zeros_like(img)
    #channel_count= img.shape[2]
    match_mask_color= (255)
    print(match_mask_color)
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image= cv2.bitwise_and(img,mask)
    return masked_image


def draw_the_lines(img,lines):
    img=np.copy(img)
    blank_image= np.zeros_like(img)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),10)

    img= cv2.addWeighted(img,0.8,blank_image,1,0.0)

    return img



def process(image):

    print(image.shape)
    height= image.shape[0]
    width= image.shape[1]


    gray_image= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    canny_image= cv2.Canny(gray_image,100,120)
    region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)] #vertices-küncler(köşeler)
    cropped_img=region_of_interest(canny_image,np.array([region_of_interest_vertices],np.int32))
    lines= cv2.HoughLinesP(cropped_img,rho=6,theta=np.pi/60,threshold=100,lines=np.array([]),minLineLength=40,maxLineGap=25)

    image_with_lines =draw_the_lines(image,lines)

    return image_with_lines

cap = cv2.VideoCapture(r"C:\Users\User\Desktop\Artificial Intelligence\road_2.mp4")

while True:

    ret,frame= cap.read()
    frame = process(frame)
    cv2.imshow("Video",frame)

    if cv2.waitKey(1)==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

