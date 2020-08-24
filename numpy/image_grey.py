import cv2
import os

im_g = cv2.imread("smallgray.png",0)
img = cv2.imread(os.path.expanduser( "~/Downloads/smallgray.png"), 0)
#im = cv2.cv.LoadImage("smallgray.png", 0)

print (f'{img}')
#print (im)
