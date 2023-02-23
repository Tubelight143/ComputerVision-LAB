#Averaging
import cv2
import numpy as np
# Reading the image
image = cv2.imread('vr.jpg')
cv2.imshow('Original', image)

#Average blur
averageBlur = cv2.blur(image, (5, 5))
cv2.imshow('Average blur', averageBlur)

#Gaussian Blur
gaussian = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imshow('Gaussian blur', gaussian)

#Median Blur
median = cv2.medianBlur(image,5)
cv2.imshow('Median Blur', median)

#Bilateral Filter
blur = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral Filter', blur)
cv2.waitKey()
cv2.destroyAllWindows()


