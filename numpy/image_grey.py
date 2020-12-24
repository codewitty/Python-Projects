import cv2
import os

im_g = cv2.imread("smallgray.png",0)
img = cv2.imread(os.path.expanduser( "~/Downloads/smallgray.png"), 0)

print (f'{img}')

new_array = img[0:2,2:4]
print(new_array)
