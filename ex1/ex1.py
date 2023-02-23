#ex1

import cv2

#Input image
input = cv2.imread('pexels-photo.jpg')
 
#Get input size
height, width = input.shape[:2]

#Desired "pixelated" size for 8,4,1 bit
w, h = (256, 256)
a, b = (16, 16)
c, d = (2, 2)
 
#Resize input to "8 bit" size
#Resize input to "4 bit" size
#Resize input to "1 bit" size

temp = cv2.resize(input, (w, h), cv2.INTER_LINEAR) 
temp1 = cv2.resize(input, (a, b), cv2.INTER_LINEAR)
temp2 = cv2.resize(input, (c, d), cv2.INTER_LINEAR)

#Initialize output image
output1 = cv2.resize(temp, (width, height), cv2.INTER_NEAREST) 
output2 = cv2.resize(temp1, (width, height), cv2.INTER_NEAREST)
output3 = cv2.resize(temp2, (width, height), cv2.INTER_NEAREST)
cv2.imshow("tiger_8.jpg",output1)
cv2.imshow("tiger_4",output2)
cv2.imshow("tiger_1",output3)
cv2.imshow("tiger.jpg",input)

#24 Bit to 8 Bit
import cv2
#Input image
input = cv2.imread('tiger.jpg')
#Get input size
height, width = input.shape[:2]
w, h = (256, 256)
temp = cv2.resize(input, (w, h), cv2.INTER_LINEAR) 
output1 = cv2.resize(temp, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("tiger_8.jpg",output1)
cv2.imshow("tiger.jpg",input)

#24 Bit to 4 Bit
import cv2
#Input image
input = cv2.imread('tiger.jpg')
#Get input size
height, width = input.shape[:2]
a, b = (16, 16)
temp1 = cv2.resize(input, (a, b), cv2.INTER_LINEAR) 
output2 = cv2.resize(temp1, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("tiger_4.jpg",output2)
cv2.imshow("tiger.jpg",input)

#24 Bit to 1 Bit
import cv2
#Input image
input = cv2.imread('tiger.jpg')
#Get input size
height, width = input.shape[:2]
c, d = (2, 2)
temp2 = cv2.resize(input, (c, d), cv2.INTER_LINEAR) 
output3 = cv2.resize(temp2, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("tiger_1.jpg",output3)
cv2.imshow("tiger.jpg",input)


