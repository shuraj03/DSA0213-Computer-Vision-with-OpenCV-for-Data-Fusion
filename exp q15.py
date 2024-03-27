import cv2
import numpy as np

# Load the images
image1 = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg')
image2 = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh1.jpg')

# Define corresponding points in both images
pts_image1 = np.array([[141, 131], [480, 159], [493, 630], [64, 601]], dtype=np.float32)
pts_image2 = np.array([[318, 256], [534, 372], [316, 670], [73, 473]], dtype=np.float32)

# Prepare homogeneous coordinates
pts_image1_homogeneous = np.concatenate([pts_image1, np.ones((4, 1))], axis=1)
pts_image2_homogeneous = np.concatenate([pts_image2, np.ones((4, 1))], axis=1)

# Perform Direct Linear Transformation (DLT) to estimate the transformation matrix
transformation_matrix, _ = cv2.findHomography(pts_image1, pts_image2)

# Apply perspective transformation using the estimated transformation matrix
transformed_image = cv2.warpPerspective(image1, transformation_matrix, (image2.shape[1], image2.shape[0]))

# Display the original and transformed images
cv2.imshow('Image 1', image1)
cv2.imshow('Transformed Image', transformed_image)
cv2.imshow('Image 2', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
