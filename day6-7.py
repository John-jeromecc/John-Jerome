import cv2

# Load the image
image = cv2.imread('sample.jpg')
if image is None:
    print("Image not found.")
    exit()

# 1. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('outputs/gray.jpg', gray)

# 2. Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imwrite('outputs/blurred.jpg', blurred)

# 3. Apply Canny Edge Detection
edges = cv2.Canny(blurred, 50, 150)
cv2.imwrite('outputs/edges.jpg', edges)

# 4. Binary Thresholding (optional extra)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('outputs/threshold.jpg', thresh)

# Show results (optional)
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('Blurred', blurred)
cv2.imshow('Edges', edges)
cv2.imshow('Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
