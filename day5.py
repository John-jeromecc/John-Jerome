import cv2
import numpy as np

# Load and convert image
image = cv2.imread('sample.jpg')
if image is None:
    print("Image not found.")
    exit()

# Show and save the original image
cv2.imshow("Original Image", image)
cv2.imwrite('outputs/original_image.jpg', image)

# Convert to grayscale and back to BGR
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Get dimensions
height, width = gray_bgr.shape[:2]
center_x, center_y = width // 2, height // 2

# 1. Draw crossing lines
cv2.line(gray_bgr, (0, 0), (width, height), (0, 0, 255), 2)  # Red
cv2.line(gray_bgr, (width, 0), (0, height), (0, 255, 0), 2)  # Green

# 2. Draw centered filled circle
cv2.circle(gray_bgr, (center_x, center_y), 50, (255, 0, 0), -1)  # Blue

# 3. Yellow triangle above center
triangle_top = center_y - 120
triangle_pts = np.array([
    [center_x - 50, triangle_top + 60],
    [center_x, triangle_top],
    [center_x + 50, triangle_top + 60]
], np.int32)
triangle_pts = triangle_pts.reshape((-1, 1, 2))
cv2.fillPoly(gray_bgr, [triangle_pts], (0, 255, 255))  # Yellow

# 4. Bottom-centered colorful text
font = cv2.FONT_HERSHEY_DUPLEX
scale = 1
thickness = 2

# First line
text1 = "JOHN JEROME"
(text_width1, _), _ = cv2.getTextSize(text1, font, scale, thickness)
x1 = (width - text_width1) // 2
y1 = height - 60
cv2.putText(gray_bgr, text1, (x1, y1), font, scale, (255, 0, 255), thickness)

# Second line
text2 = "C. CASTILLO"
(text_width2, _), _ = cv2.getTextSize(text2, font, scale, thickness)
x2 = (width - text_width2) // 2
y2 = height - 20
cv2.putText(gray_bgr, text2, (x2, y2), font, scale, (0, 165, 255), thickness)  

# 5. Save and show final result
cv2.imwrite('outputs/annotated_image.jpg', gray_bgr)
cv2.imshow("Annotated Image", gray_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
