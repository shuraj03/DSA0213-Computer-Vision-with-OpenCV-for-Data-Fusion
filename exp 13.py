import cv2
import numpy as np

# Load the video
video_capture = cv2.VideoCapture('/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/imax.mp4')

# Get the width and height of the video frames
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the source points (coordinates of a rectangle)
source_points = np.float32([[50, 50], [300, 50], [300, 200], [50, 200]])

# Define the destination points (where the corners of the rectangle will be mapped)
destination_points = np.float32([[100, 100], [250, 50], [200, 300], [50, 250]])

# Compute the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (width, height))

# Process each frame of the video
while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # Break the loop if no more frames are available

    # Perform perspective transformation on the frame
    transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (width, height))

    # Write the transformed frame to the output video
    output_video.write(transformed_frame)

    # Display the transformed frame (optional)
    cv2.imshow('Transformed Frame', transformed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Break the loop if 'q' key is pressed

# Release video capture and writer objects
video_capture.release()
output_video.release()
cv2.destroyAllWindows()
