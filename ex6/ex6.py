import cv2
import numpy as np
original_image=cv2.imread("card.jpg")
cv2.imshow('original image',original_image)
cv2.waitKey(0)
sharpen_filter=np.array([[-1,-1,-1],
                 [-1,9,-1],
                [-1,-1,-1]])
sharp_image=cv2.filter2D(original_image,-1,sharpen_filter)
cv2.imshow('Required image',sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
