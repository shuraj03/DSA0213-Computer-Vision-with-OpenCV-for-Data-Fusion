import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg')

# Define the translation (movement) in pixels
x_translation = 50  # Move 50 pixels to the right
y_translation = 30  # Move 30 pixels down

# Get the height and width of the image
height, width = image.shape[:2]

# Create a blank canvas (image) to paste the original image onto
canvas = np.zeros((height + y_translation, width + x_translation, 3), dtype=np.uint8)

# Paste the original image onto the canvas at the desired position
canvas[y_translation:, x_translation:] = image

# Display the original image and the moved image
cv2.imshow('Original Image', image)
cv2.imshow('Moved Image', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
