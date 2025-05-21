import cv2

# Load the image
image = cv2.imread('sample.jpg')

# Check if image was loaded properly
if image is None:
    print("Error: Image not found or path is incorrect.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)

    # Save the grayscale image
    cv2.imwrite('gray_sample.jpg', gray_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
