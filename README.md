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


02 Basic Image Manipulation

img[row, column] - to access pixel in a numpy matrix

img[start_row:end_row, start_col, end_col] - more efficient for accessing multiple pixels, end is excluded, can be used for cropping

Resizing Images (interpolation default value is LINEAR)

Method 1: Scaling factor using fx, fy

cv2.resize(src_image, desired_image_size, fx=[x-value], fy=[y-value])

positive values - increase image size

negative values - decrease image size

Method 2: Specifying exact size (desired height and width in pixels)

cv2.resize(src_image, dsize=desired_image_size, interpolation)

Interpolation Codes

For enlarging an image, use INTER_LINEAR and INTER_CUBIC

For shrinking an image, use INTER_AREA

INTER_LINEAR is default option for resize which combines good visual results and time performance

Method 3: Maintaining aspect ratio (using dsize)

Formula:
shape[height, width]

desired_width / cropped_region.shape[1] (width) multipled to cropped_regiion.shape[0] (height)

Method 4: User Selective Cropping with ROI

roi = cv2.selectROI("Select Region of Interest", img, False)

cropped_img = img[int(roi[1]):int(roi[1]+roi[3]), 
                    int(roi[0]):int(roi[0]+roi[2])]


Flipping Images

cv.flip(src_image, flipCode)

flipCode
1. 0 - flipping around the x-axis and positive value (vertically)
2. 1 - flipping around the y-axis (horizontally)
3. -1 - flipping around both axes (both flipped)

