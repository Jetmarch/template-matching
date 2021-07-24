import cv2
import numpy as np

farm_img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
template_img = cv2.imread('template.JPG', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(farm_img, template_img, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#width on 1
w = template_img.shape[1]
#height on 0
h = template_img.shape[0]

threshold = .60

yloc, xloc = np.where(result >= threshold)

rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

for (x, y, w, h) in rectangles:
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)


cv2.imshow('Farm', farm_img)
cv2.waitKey()
cv2.destroyAllWindows()