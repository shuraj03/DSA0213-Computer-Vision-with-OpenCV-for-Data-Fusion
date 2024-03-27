import cv2

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh.jpg'
                   )

# Get the height and width of the image
height, width = image.shape[:2]

# Define the angle of rotation in degrees
angle_clockwise = 45  # Rotate clockwise by 45 degrees
angle_counterclockwise = -45  # Rotate counterclockwise by 45 degrees

# Perform clockwise rotation
rotated_clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Perform counterclockwise rotation
rotated_counterclockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the original image and the rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Clockwise', rotated_clockwise)
cv2.imshow('Rotated Counterclockwise', rotated_counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
