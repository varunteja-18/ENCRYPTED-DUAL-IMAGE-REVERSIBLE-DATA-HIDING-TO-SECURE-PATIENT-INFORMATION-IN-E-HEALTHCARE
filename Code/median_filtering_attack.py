## Import Required Packages
import cv2
import numpy as np

## Load the Image
img = cv2.imread('watermark_256_8bit.jpg')
image = cv2.imread('watermark_256_8bit.jpg')

## Apply Median Filtering Attack with Kernel Size 5x5
noisy_img = cv2.medianBlur(img, 5)

## Display the Original and Noisy Images
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()