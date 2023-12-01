import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import cv2

# Generate random 3D points in the color space
# np.random.seed(42)
# points_3d = np.random.randint(0, 256, size=(100, 3))
image_path = './test/image.png'  # Replace with the path to your image file
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV loads images in BGR format, convert to RGB
points_3d = image.reshape((-1, 3))

# Apply PCA for dimensionality reduction
pca = PCA(n_components=2, iterated_power=400)
points_2d = pca.fit_transform(points_3d)

# Plot the 3D points and the 2D projection
fig = plt.figure(figsize=(12, 6))

# 3D scatter plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2], c=points_3d / 255.0, marker='o')
ax1.set_title('Original 3D Color Space')
ax1.set_xlabel('Red')
ax1.set_ylabel('Green')
ax1.set_zlabel('Blue')

# 2D scatter plot
ax2 = fig.add_subplot(122)
ax2.scatter(points_2d[:, 0], points_2d[:, 1], c=points_3d / 255.0, marker='o')
ax2.set_title('2D Projection using PCA')
ax2.set_xlabel('Principal Component 1')
ax2.set_ylabel('Principal Component 2')

plt.show()

