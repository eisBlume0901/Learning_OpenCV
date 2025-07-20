01 Getting Started with Images

OpenCV

cv2.imread(filename[, flags]) - displays an image in grayscale, color images (transparent is disregarded), Alpha channel

Flags
1. cv2.IMREAD_GRAYSCALE or 0
2. cv2.IMREAD_COLOR or 1
3. cv2.IMREAD_UNCHANGED or -1

Image data - pixel values, element of a 2D numpy array

Pixel value - 8 bits ranging from 0 to 255

cv2.imshow()


Matplotlib 

plt.imshow(filename) - displays the image in a plot

plt.imshow(filename, cmap="gray") - displays the image in grayscale


Matplotlib uses RGB format, OpenCV uses BGR format, so reverse the channels of the image so that Matplotlib can display the actual color