01 Getting Started with Images

OpenCV

cv2.imread(filename[, flags]) - displays an image in grayscale, color images (transparent is disregarded), Alpha channel

Flags
1. cv2.IMREAD_GRAYSCALE or 0
2. cv2.IMREAD_COLOR or 1
3. cv2.IMREAD_UNCHANGED or -1

Image data - pixel values, element of a 2D numpy array

Pixel value - 8 bits ranging from 0 to 255

cv2.split(image) - divides multi-channel array into several single-channel arrays

cv2.merge(image) - merges several arrays to make a single-multi channel array (ALL THE INPUT MATRICES MUST HAVE THE SAME SIZE)

cv2.cvtColor(image, code) - converts input image (8-bit/16-bit/single-precision floating point) from one color space to another (for instance, BGR format to RGB format)

code
1. BGR2RGB (blue, green, red to red, green, blue)
2. BGR2HSV (blue, green, red to hue - type of color [red, green, blue], saturation - intensity/purity of a color, value - relative lightness/darkness of a color)
3. HSV2BGR

Go to hue-saturation-value.jpeg to see the visual representation

cv2.namedWindow(name) - create a window with the given name

cv2.imshow(cv2.namedWindow(name), image) - display the image in a named window

cv2.waitKey(0) - waiting for a key press in indefinite time

cv2.destroyWindow(cv2.namedWindow(name)) - to close the window


Matplotlib 

plt.imshow(filename) - displays the image in a plot

plt.imshow(filename, cmap="gray") - displays the image in grayscale


Matplotlib uses RGB format, OpenCV uses BGR format, so reverse the channels of the image so that Matplotlib can display the actual color