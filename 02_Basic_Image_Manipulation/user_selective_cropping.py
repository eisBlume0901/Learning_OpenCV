import cv2
img = cv2.imread("02_Basic_Image_Manipulation/New_Zealand_Boat.jpg")

# region of interest
roi = cv2.selectROI("Select Region of Interest", img, False)

cropped_img = img[int(roi[1]):int(roi[1]+roi[3]), 
                    int(roi[0]):int(roi[0]+roi[2])]

# selectROI returns a tuple (row, column, width, height)

cv2.imshow("Cropped_Image", cropped_img)

while True:
    key = cv2.waitKey(0)
    if key == ord('q') or key == 13:
        break

cv2.destroyAllWindows()