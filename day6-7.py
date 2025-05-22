import cv2
import os

# Create output directory
os.makedirs('outputs', exist_ok=True)

# Load the image
image = cv2.imread('sample.jpg')
if image is None:
    print("Image not found.")
    exit()

# Save original image
cv2.imwrite('outputs/original.jpg', image)

# 1. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('outputs/gray.jpg', gray)

# 2. Apply stronger Gaussian Blur for more visible smoothening
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
cv2.imwrite('outputs/blurred.jpg', blurred)

# 3. Apply Canny Edge Detection with lower threshold for more edges
edges = cv2.Canny(blurred, 30, 100)
cv2.imwrite('outputs/edges.jpg', edges)

# 4. Binary Thresholding with a lower threshold value
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imwrite('outputs/threshold.jpg', thresh)

# Show results
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('Blurred (Stronger)', blurred)
cv2.imshow('Edges (More Visible)', edges)
cv2.imshow('Threshold (Lower Value)', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
