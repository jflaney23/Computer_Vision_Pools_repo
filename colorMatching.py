import numpy as np
import cv2


img = cv2.imread('/Users/jflaney23/Developer/OpenCV Project/assets/Screen Shot 2022-10-08 at 12.02.13 PM.png')

#Convers to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#ranges of blue in HSV
#Lightest HSV hsv(85, 40, 40)
#Darkest HSV hsv(100,255,255)


mask = cv2.inRange(hsv, (85, 40, 40), (100,255,255))
 
#slices the blue
imask = mask>0
blue = np.zeros_like(img, np.uint8)
blue[imask] = img[imask]

#saves the image
cv2.imwrite("blue2.png", blue)