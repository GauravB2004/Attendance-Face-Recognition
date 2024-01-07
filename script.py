import cv2
import numpy as np

# Read the image
image_path = '/Users/gaurav/Documents/Tech Projects/WiDS-Face-Recognition/four-coin.jpeg'  # Make sure to update this path
original_image = cv2.imread(image_path)
image = original_image.copy()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to smoothen the image
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# Edge detection
edged = cv2.Canny(blurred, 30, 150)

# Find contours in the edged image
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours by size (adjust the area threshold as needed)
min_area_threshold = 115  # Start with a smaller threshold to see if smaller contours are detected
coins = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area_threshold]

# Draw contours on the original image for visualization
cv2.drawContours(original_image, coins, -1, (0, 255, 0), 2)

# Display images
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale', gray)
cv2.imshow('Blurred', blurred)
cv2.imshow('Edged', edged)

print("Number of coins detected: ", len(coins))

cv2.waitKey(0)
cv2.destroyAllWindows()
