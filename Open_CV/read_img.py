import cv2
# read imge
img=cv2.imread("/home/ibrahim/projects/Computer-Vision/Open_CV/resources/images/cat.jpg")
cv2.imshow("Image",img)
cv2.waitKey(0)


# read video

capture=cv2.VideoCapture('/home/ibrahim/projects/Computer-Vision/Open_CV/resources/videos/kitten.mp4')


while True:
    ret,frame=capture.read()
    cv2.imshow("Video",frame)
    if ret:
        if cv2.waitKey(40) & 0xFF==ord('c'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()