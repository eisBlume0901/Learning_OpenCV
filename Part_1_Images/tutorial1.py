import cv2


# Images can be loaded as grayscale, true color (BGR), or unchanged
# cv2.IMREAD_COLOR (1) - loads color image (default)
# cv2.IMREAD_GRAYSCALE (0) - loads image as grayscale
# cv2.IMREAD_UNCHANGED (-1) - loads image including alpha channel
img = cv2.imread('Part_1_Images/assets/Huntrix.jpeg', -1)
# img = cv2.imread('Part_1_Images/assets/Huntrix.jpeg', cv2.IMREAD_UNCHANGED)

# To resize the image
# using pixel sizing
# img = cv2.resize(img, (600,338)) 
# using fx (shrinking or increasing the image dependent on the fx, fy values)
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# To rotate the IMAGE
# cv2.ROTATE_180
# cv2.ROTATE_90_CLOCKWISE
# cv2.ROTATE_90_COUNTERCLOCKWISE
img = cv2.rotate(img, cv2.ROTATE_180)

# To rename the image
cv2.imwrite('Part_1_Images/assets/Huntrix_KPop_Demon_Hunters.jpeg', img)

# To display the image
cv2.imshow('Image', img)

# To close the image window
cv2.waitKey(0) # Infinite time 
cv2.destroyAllWindows()

