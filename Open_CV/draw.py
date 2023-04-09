import cv2
import numpy as np
#draw rectangle
img=cv2.imread('/home/ibrahim/projects/Computer-Vision/Open_CV/resources/images/cat.jpg')
rect=cv2.rectangle(img,(150,150),(450,450),(60,255,100),thickness=2)
cv2.imshow('rectangle',rect)
cv2.waitKey(0)

#blank image

blank=np.zeros((500,500,3),dtype="uint8")
cv2.rectangle(blank,(0,0),(150,150),(0,255,0),thickness=-1)#-1 means fill rectangle
cv2.circle(blank,(250,250),50,(0,255,0),thickness=-1)
cv2.putText(blank,"7mada",(0,250),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255))
cv2.imshow('blank',blank)
cv2.waitKey(0)
