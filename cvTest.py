import cv2
import numpy as np

# -1 is color, 0 is grayscale, 1 is normal
img = cv2.imread('/Users/jflaney23/Developer/OpenCV Project/assets/Screen Shot 2022-10-07 at 6.18.43 PM.png', 0)
template = cv2.imread('/Users/jflaney23/Developer/OpenCV Project/assets/Screen Shot 2022-10-07 at 6.19.28 PM.png', 0)

im2 = img.copy()

h, w =template.shape
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

#for loops to find which method is best
for method in methods:
    img2 = img.copy()
    
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows