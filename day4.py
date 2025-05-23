import cv2

# Load the image
image = cv2.imread('sample.jpg')

# Check if image was loaded properly
if image is None:
    print("Error: Image not found or path is incorrect.")
else:
    # Resize the image to a smaller fixed size: 320x240
    resized_image = cv2.resize(image, (620, 440))

    # Convert to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Display the resized original and grayscale images
    cv2.imshow('Small Original Image', resized_image)
    cv2.imshow('Small Grayscale Image', gray_image)

    # Save the smaller grayscale image
    cv2.imwrite('gray_sample.jpg', gray_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
