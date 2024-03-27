import cv2

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg')

# Get the dimensions of the image
height, width = image.shape[:2]

# Define the scaling factors for bigger and smaller sizes
bigger_scale = 1.5  # Scale factor for bigger size (increase by 50%)
smaller_scale = 0.5  # Scale factor for smaller size (decrease by 50%)

# Scale the image to its bigger size
bigger_image = cv2.resize(image, (int(width * bigger_scale), int(height * bigger_scale)))

# Scale the image to its smaller size
smaller_image = cv2.resize(image, (int(width * smaller_scale), int(height * smaller_scale)))

# Display the original image, bigger image, and smaller image
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
