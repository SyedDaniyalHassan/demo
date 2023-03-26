import cv2
import numpy as np
image = cv2.imread("GreenScreen.jpg")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


green_lower = np.array([40, 50, 50])
green_upper = np.array([80, 255, 255])


mask = cv2.inRange(hsv_image, green_lower, green_upper)


green_pixels = cv2.bitwise_and(image, image, mask=mask)

cv2.imwrite("image.jpg",green_pixels)
