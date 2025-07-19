import cv2
import random

img = cv2.imread('Part_2_Image_Fundamentals_and_Manipulation/assets/eisblume0901-high-resolution-logo.png', -1)
print(img) # Extract pixels and store them in an array, returns 3 color channels (blue green red, for instance 255 255 255 is white)
print(type(img)) # <class 'numpy.ndarray'>
print(img.shape) # (2000, 2000, 3), represents height, width, and channels


# Changing color in a specific pixel
# for i in range(100):
#     for j in range(img.shape[1]):
#         # more blue and more red but random
#         img[i][j] = [255, random.randint(0, 255), 255]

# Image coordinates is row, column or y,x
# Displacing pixels 
tag = img[500:750, 600:900] #750-500 = 250, 900-600=300
img[100:350, 650:950] = tag # 350-100=250, 950-650=300, note that displacement region should be the same

cv2.imshow('Image', img)


cv2.waitKey(0)

cv2.destroyAllWindows()