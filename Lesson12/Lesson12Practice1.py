import matplotlib.pylab as plt 
import cv2
import numpy as np 

def region_of_interest(img,vertices):
    mask= np.zeros_like(img)
    channel_count= img.shape[2]
    match_mask_color= (255,)*channel_count
    print(match_mask_color)
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image= cv2.bitwise_and(img,mask)
    return masked_image

image = cv2.imread(r"C:\Users\User\Desktop\Artificial Intelligence\road.png")
image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)




print(image.shape)
height= image.shape[0]
width= image.shape[1]

region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)] 
cropped_img=region_of_interest(image,np.array([region_of_interest_vertices],np.int32))

plt.imshow(cropped_img)

plt.show()

