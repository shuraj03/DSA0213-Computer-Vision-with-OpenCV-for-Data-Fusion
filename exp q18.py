import cv2

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection along the Y-axis
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Convert the result to 8-bit unsigned integer
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display the original and Sobel edge-detected images along Y-axis
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection (Y-axis)', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
