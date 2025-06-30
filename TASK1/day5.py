import cv2
import numpy as np

image = cv2.imread('sample.jpg')
if image is None:
    print("Image not found.")
    exit()

resized_image = cv2.resize(image, (620, 440))

cv2.imshow("Original Image", resized_image)
cv2.imwrite('outputs/original_image.jpg', resized_image)

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

height, width = gray_bgr.shape[:2]
center_x, center_y = width // 2, height // 2

cv2.circle(gray_bgr, (center_x, center_y), 30, (255, 0, 0), 2)

triangle_top = center_y - 70
triangle_pts = np.array([
    [center_x - 30, triangle_top + 40],
    [center_x, triangle_top],
    [center_x + 30, triangle_top + 40]
], np.int32)
triangle_pts = triangle_pts.reshape((-1, 1, 2))
cv2.polylines(gray_bgr, [triangle_pts], isClosed=True, color=(0, 255, 255), thickness=2)

font = cv2.FONT_HERSHEY_DUPLEX
scale = 0.5  
thickness = 1

text1 = "JOHN JEROME"
(text_width1, _), _ = cv2.getTextSize(text1, font, scale, thickness)
x1 = (width - text_width1) // 2
y1 = height - 40
cv2.putText(gray_bgr, text1, (x1, y1), font, scale, (255, 0, 255), thickness)

text2 = "C. CASTILLO"
(text_width2, _), _ = cv2.getTextSize(text2, font, scale, thickness)
x2 = (width - text_width2) // 2
y2 = height - 15
cv2.putText(gray_bgr, text2, (x2, y2), font, scale, (0, 165, 255), thickness)

cv2.imwrite('outputs/annotated_image.jpg', gray_bgr)
cv2.imshow("Annotated Image", gray_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
