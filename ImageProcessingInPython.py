import cv2 
import numpy as np 

# Load the image 
image = cv2.imread('path/to/your/image.jpg') 

width = 500  # Desired width 
height = 500  # Desired height 
dimensions = (width, height) 
resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR) 

cv2.imwrite('SupportingFiles/resized_image.jpg', resized_image) 
