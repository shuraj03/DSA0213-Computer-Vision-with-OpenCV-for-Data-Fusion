import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the Laplacian mask
laplacian_mask = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]], dtype=np.float32)

# Apply the filter
sharpened_image = cv2.filter2D(gray_image, -1, laplacian_mask)

# Add the sharpened image to the original to enhance the edges
sharpened_image = cv2.addWeighted(gray_image, 1, sharpened_image, 1, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
