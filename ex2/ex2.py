#Ex2 Converting Between Color-spaces

import cv2
 
image = cv2.imread("258-2581180_doraemon-only-doraemon-hd-wallpaper-1080p.jpg")
 
# converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
# converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
 
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
