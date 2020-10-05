import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path of the image file")

args=vars(ap.parse_args())
image=cv2.imread(args["image"])

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayimage,(5,5),0)
cv2.imshow("Image", image)
ret, im_th = cv2.threshold(grayimage, 90, 255, cv2.THRESH_BINARY_INV)
#edged = cv2.Canny(blurred, 30, 150)
#cv2.imshow("Edges", edged)
(_, cnts, _) = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


print(len(cnts))

cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key =lambda x: x[1])
for (c, _) in cnts:
	(x, y, w, h) = cv2.boundingRect(c)
	if w >= 6 and h >= 20:
		cv2.rectangle(image, (x-6, y-6), (x + w+6, y + h+6),(0, 255, 0), 1)
cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
