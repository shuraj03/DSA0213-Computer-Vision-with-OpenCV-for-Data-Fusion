import cv2

# Read the video
video_capture = cv2.VideoCapture(r"/Users/sunilshurajnthiyanandan/Documents/sunil_clg/OpenCV/OpenCV_Class/imax.mp4")

# Get the frame rate of the video
fps = int(video_capture.get(cv2.CAP_PROP_FPS))

# Create a VideoWriter object to write the output videos
output_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
output_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc_slow = cv2.VideoWriter_fourcc(*'mp4v')
fourcc_fast = cv2.VideoWriter_fourcc(*'mp4v')
output_video_slow = cv2.VideoWriter('output_video_slow.mp4', fourcc_slow, fps / 2,
                                    (output_width, output_height))  # Adjusted FPS for slow motion
output_video_fast = cv2.VideoWriter('output_video_fast.mp4', fourcc_fast, fps * 2,
                                    (output_width, output_height))  # Adjusted FPS for fast motion

# Read and process each frame
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Write the same frame twice for slow motion
    output_video_slow.write(frame)
    output_video_slow.write(frame)

    # Write the same frame for fast motion
    output_video_fast.write(frame)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
output_video_slow.release()
output_video_fast.release()
cv2.destroyAllWindows()
