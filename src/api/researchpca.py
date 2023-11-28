# Idea
# We have a 3 dimensional space we want mapped to a 2 dimensional spae
# so we use PCA to determine the best angle of the plane on which
# to map the data
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import cv2

# Load an image file using OpenCV
image_path = './test/demo.jpg'  # Replace with the path to your image file
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV loads images in BGR format, convert to RGB

# Reshape the image array to a 2D array of RGB values
points_3d = image.reshape((-1, 3))

# Apply PCA for dimensionality reduction
pca = PCA(n_components=2)
points_2d = pca.fit_transform(points_3d)

# Scale the PCA components to the range [0, 255]
scaled_green = np.interp(points_2d[:, 0], (points_2d[:, 0].min(), points_2d[:, 0].max()), (0, 255))
scaled_blue = np.interp(points_2d[:, 1], (points_2d[:, 1].min(), points_2d[:, 1].max()), (0, 255))

# Create a 2D array for color representation
colors = np.column_stack((image[:, :, 0].flatten(), scaled_green.reshape(image.shape[:2]).flatten(), scaled_blue.reshape(image.shape[:2]).flatten()))

# Display the image using the green and blue values
plt.figure(figsize=(8, 8))
plt.imshow(colors.reshape(image.shape) / 255.0, origin='upper')
plt.title('Mapped 2D Projection to Green and Blue')
plt.xlabel('Green')
plt.ylabel('Blue')
plt.show()
