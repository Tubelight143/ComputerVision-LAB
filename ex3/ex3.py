#ex3(s)

import cv2
import numpy as np

img = cv2.imread('pexels-photo.jpg')
original = img.copy()
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
res = np.hstack((original,img))
cv2.imshow("original", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ex3(map&eq)

import cv2
import numpy as np
from matplotlib import pyplot as plt

# read a image using imread
img = cv2.imread('pexels-photo.jpg', 0)

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

#for mapping
h=cv2.calcHist((img), [0], None, [256], [0,256])
h1=cv2.calcHist((equ), [0], None, [256], [0,256])

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv2.imshow('image.jpg', res)
cv2.imshow('lion.jpg',img)
plt.plot(h)
plt.plot(h1)
plt.title("Histogram Mapping & Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.grid()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
