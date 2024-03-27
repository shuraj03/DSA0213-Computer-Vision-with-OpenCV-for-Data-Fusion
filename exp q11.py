import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg')

# Define the transformation matrix
# We'll perform a translation and rotation in this example
# Translation matrix:
# [1 0 Tx]
# [0 1 Ty]
tx = 50  # Translation in x direction (move right by 50 pixels)
ty = 30  # Translation in y direction (move down by 30 pixels)
translation_matrix = np.float32([[1, 0, tx],
                                 [0, 1, ty]])

# Rotation angle in degrees
angle = 30

# Get the height and width of the image
height, width = image.shape[:2]

# Define the center of rotation (center of the image)
center = (width // 2, height // 2)

# Get the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# Combine the translation and rotation matrices into a single 3x3 matrix
combined_matrix = np.vstack([rotation_matrix, [0, 0, 1]])

# Perform affine transformation
transformed_image = cv2.warpAffine(image, combined_matrix[:2], (width, height))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
