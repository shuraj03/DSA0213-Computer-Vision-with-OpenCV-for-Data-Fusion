import cv2

# Load the image
image = cv2.imread('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/mh1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
