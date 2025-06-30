import cv2

image = cv2.imread('sample.jpg')

if image is None:
    print("Error: Image not found or path is incorrect.")
else:
    resized_image = cv2.resize(image, (620, 440))

    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Small Original Image', resized_image)
    cv2.imshow('Small Grayscale Image', gray_image)

    cv2.imwrite('gray_sample.jpg', gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
