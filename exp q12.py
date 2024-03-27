import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg')

# Define the four source points (coordinates of a rectangle)
source_points = np.float32([[50, 50], [300, 50], [300, 200], [50, 200]])

# Define the four destination points (where the corners of the rectangle will be mapped)
# For demonstration, let's make a perspective transformation (simulate tilting the rectangle)
destination_points = np.float32([[100, 100], [250, 50], [200, 300], [50, 250]])

# Compute the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Perform perspective transformation
transformed_image = cv2.warpPerspective(image, perspective_matrix, (image.shape[1], image.shape[0]))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
