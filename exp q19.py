import cv2

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection along the X-axis
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel edge detection along the Y-axis
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine the results to get edges along both X and Y axes
sobel_xy = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

# Display the original image and the Sobel edge-detected image along XY axis
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection (XY axis)', sobel_xy)
cv2.waitKey(0)
cv2.destroyAllWindows()
