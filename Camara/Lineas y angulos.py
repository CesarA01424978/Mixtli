import cv2
import numpy as np

# Load the input image
image = cv2.imread('perrito.jpg')

# Define the coordinates of the region of interest (ROI)
# Format: (x1, y1) = top-left corner, (x2, y2) = bottom-right corner
height, width, _ = image.shape
roi_x1 = 0  # Left edge of the image
roi_x2 = width // 4  # 1/4 of the image width
roi_y1 = height * 3// 4  # 3/4 of the image height
roi_y2 = height  # Full height of the image

# Extract the ROI from the input image
roi = image[roi_y1:roi_y2, roi_x1:roi_x2]

# Apply Canny edge detection to the ROI
edges = cv2.Canny(roi, threshold1=100, threshold2=200)

# Apply the Hough Transform to detect lines in the ROI
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Create a copy of the original ROI to draw lines on
roi_with_lines = roi.copy()

# Draw the detected lines on the ROI and store their angles
angles_degrees = []
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(roi_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Draw red lines

        # Calculate and store the angle in degrees
        angle_degrees = np.degrees(theta)
        angles_degrees.append(angle_degrees)

# Overlay the ROI with detected lines onto the original image
image_with_lines = image.copy()
image_with_lines[roi_y1:roi_y2, roi_x1:roi_x2] = roi_with_lines

# Define the coordinates of the horizontal line (in the middle of the image)
horizontal_line_y = height * 7 // 8  # Middle of the image
horizontal_line_x1 = 0  # Start from the left edge
horizontal_line_x2 = width  # Extend to the right edge

# Draw the horizontal line on the original image
cv2.line(image_with_lines, (horizontal_line_x1, horizontal_line_y), (horizontal_line_x2, horizontal_line_y), (0, 255, 0), 2)  # Draw green line

# Display the angles in the upper left corner
font = cv2.FONT_HERSHEY_SIMPLEX
for i, angle in enumerate(angles_degrees):
    text = f"Angle {i+1}: {angle:.2f} degrees"
    cv2.putText(image_with_lines, text, (10, 30 + i * 30), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

# Display the original image with detected lines and the horizontal line
cv2.imshow('Image with Detected Lines and Angles', image_with_lines)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

