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

plt.subplot(rowcolumnsubplot)

plt.subplot(141) = 1 row, 4 columns, subplot 1

plt.figure(figsize=[width, height])
 
Rule for setting properly figsize for subplots
1. For a 2x2 grid (4 subplots), try figsize=[8, 8] (square ratio).
2. For a 3x2 grid (6 subplots, 3 rows, 2 columns), try figsize=[12, 12] or figsize=[12, 8] (taller if you want more vertical space).
3. For a 1x3 grid (3 subplots, 1 row and 3 columns), try figsize=[12, 4] (wider for more horizontal space).

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


03_Image_Annotation

Drawing a Line

img = cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

pt1 = (x1, y1)

pt2 = (x2, y2)

color = rgb format

lineType

1. FILLED
2. LINE_4 (4-connected line) - (horizontal and vertical neighbors)
3. LINE_8 (8-connected line) - (includes diagonal neighbors for smoother lines)
4. LINE_AA (anti-aliased line) - best for reduced jagged edges


Drawing a Circle

img = cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])

thickness - positive value create a thick border, negative value will fill the circle

Drawing a Rectangle

img = cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

pt1 = top left (x1, y1) y down 

pt2 = bottom right (x2, y2) y up

Adding Text

img = cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

fontScale - positive values will be seen in a positive axis, negative values will be seen in negative axis
org - bottom left corner of the text string in the image

04 Basic Image Enhacement using Mathematical Operations

type() - overall type of an object

.dtype - data type of the elements inside the array

Add (brighten), subtract (darken) - increasing / decreasing value of each pixel by the same amount 

cv2.add(img_rgb, np.ones(img_rgb.shape, dtype="uint8") * numberToAdd)

cv2.subtract(img_rgb, np.ones(img_rgb.shape, dtype="uint8") * numberToSubtract)


np.ones - creates an array that has value of one

Multiply - contrast, multiply constant values to intensify values of the pixel (larger = darker, smaler = brighter contrast [should be < 1])

img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb), np.ones(img_rgb.shape) * factorSmallerThan1 ))

img_rgb_brighter = np.uint8(np.clip (cv2.multiply(np.float64(img_rgb), np.ones(img_rgb.shape) * factorGreaterThan1 ), 0, 255))


Binary Image

Thresholding - process used to create Binary Images from grayscale images

Best Explanation: https://youtu.be/BA00xTv5-Z4

Best Visualization: https://youtu.be/En2mqnNkX8g

retval, img_thresh = cv2.threshold( img_in_grayscale, thresh, maxval, type[, dst] )

Threshold Types

1. THRESH_BINARY
2. THRESH_BINARY_INV
3. THRESH_TRUNC
4. THRESH_TOZERO
5. THRESH_TOZERO_INV
6. THRESH_MASK
7. THRESH_OTSU
8. THRESH_TRIANGLE

Suggested to use adaptive thresholding for optimization and to capture the image outline well.

dst = cv.adaptiveThreshold( img, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst] )

maxValue - non-zero value asigned tot he pixels for which the condition is satisfied

adaptiveMethod - ADAPTIVE_THRESH_MEAN_C, ADAPTATIVE_THRESH_GAUSSIAN_C

thresholdType - referenced above (8 types of Thresh Types)

blockSize - size of a pixel neighborhood used to calculate a threshold value for the pixel (odd values, 3, 5, 7, and so forth)

c - constant subtracted from mean or weighted mean (normally, positive but can be zero or negative)


Image Masking with Bitwise Operators

dst = cv2.bitwise_and( img_21, img_2[, dst[, mask]] )

- 0 AND 0 → 0 (black)
- 0 AND 255 → 0 (black)
- 255 AND 0 → 0 (black)
- 255 AND 255 → 255 (white)

dst = cv2.bitwise_or( img_21, img_2[, dst[, mask]] )

- 0 OR 0 → 0 (black)
- 0 OR 255 → 255 (white)
- 255 OR 0 → 255 (white)
- 255 OR 255 → 255 (white)

dst = cv2.bitwise_xor( img_21, img_2[, dst[, mask]] )

(opposite of and results)
- 0 XOR 0 → 0 (black)
- 0 XOR 255 → 255 (white)
- 255 XOR 0 → 255 (white)
- 255 XOR 255 → 0 (black)

Bitwise Operators and Thresholding can be combined for Image Masking

05 Accessing the Camera

Go to Folder 05_Accessing_the_Camera for details

06 Video Writing

cap = cv2.VideoCapture(source) - source can accept mp4, YouTube Video, camera

cap.isOpened() - returns true if video capturing has been initialized already

retval, image = cap.read() - grabs, decodes and returns the next video frame (retval = returns boolean if a frame has successfully read, image = returns actual image data)

VideoWriter object = cv.VideoWriter(filename, fourcc, fps, frameSize )

FourCC (Four Character Code) - helps the device or platform understand which codec to use to play the video.

FourCC codes
- PIM1 - MPEG-1 codec - 
- MJPG - Motion-JPEG codec - High compression ratio, good quality for still imaegs, can be slow for video
- XVID - Xvid codec - Good compression ratio, high quality, wide platform compatibility
- DIVX - DivX codec - High compression ratio, good quality, wide platform compatibility
- WMV3 - Windows Media Video 3 codec - Good compression ratio, high quality, specific to windows media player

fps - frame rates per second

framesize - size of the video frames
