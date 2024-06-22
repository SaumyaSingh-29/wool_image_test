import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\hp\Saumya\1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Canny edge detection to find fiber boundaries
edges = cv2.Canny(blurred, 50, 150)

# Find contours of the fibers
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and extract features
for contour in contours:
    # Calculate fiber diameter (based on contour area)
    area = cv2.contourArea(contour)
    diameter = np.sqrt(4 * area / np.pi)
    
    # Calculate fiber length (based on contour arc length)
    length = cv2.arcLength(contour, True)
    
    # Extract the bounding box of the fiber
    x, y, w, h = cv2.boundingRect(contour)
    
    # Draw bounding box and label
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, f"Diameter: {diameter:.2f} Length: {length:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the results
cv2.imshow('Wool Grading', image)
cv2.waitKey(0)
cv2.destroyAllWindows()