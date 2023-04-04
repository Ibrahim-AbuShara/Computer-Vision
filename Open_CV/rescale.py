import cv2
def resizer(frame,scale):
    l=int (frame.shape[0]*scale)
    w=int (frame.shape[1]*scale)
    return cv2.resize(frame,(w,l),interpolation=cv2.INTER_AREA)
    
img=cv2.imread('/home/ibrahim/projects/Computer-Vision/Open_CV/resources/images/cat.jpg')
img_resized=resizer(img,.9)
cv2.imshow("img",img)
cv2.imshow("resized",img_resized)
cv2.waitKey(0)
cap=cv2.VideoCapture('/home/ibrahim/projects/Computer-Vision/Open_CV/resources/videos/dog.mp4')
while True:
    ret,frame=cap.read()
    if ret==True:
        reframe=resizer(frame,.75)
        cv2.imshow("frame",frame)
        cv2.imshow("reframe",reframe)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()