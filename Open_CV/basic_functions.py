import cv2
#orginal image
img=cv2.imread('resources/images/cat.jpg')
cv2.imshow("org",img)
#Gray image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
#blur image
blur=cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow("blur",blur)
#edges image
edges=cv2.Canny(blur,80,80)
cv2.imshow("edges",edges)
# dilation image
dilation=cv2.dilate(edges,(7,7),iterations=5)
cv2.imshow("dilation",dilation)
#erosion
erosion=cv2.erode(dilation,(7,7),iterations=5)
cv2.imshow("erosion",erosion)
#crop image
crop=img[0:600,200:900]
cv2.imshow("crop",crop)
cv2.waitKey(0)