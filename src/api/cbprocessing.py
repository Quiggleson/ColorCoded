import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

def nored(unchanged_colors, upload_path, image_name):
    # Define the color to remain unchanged
    unchanged_colors = [[255, 255, 255], [255,0,0]]  # White color in RGB format

    # Load an image file using OpenCV
    # image_path = './test/three.png'  # Replace with the path to your image file
    image = cv2.imread(f'{upload_path}/{image_name}')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV loads images in BGR format, convert to RGB

    # Reshape the image array to a 2D array of RGB values
    points_3d = image.reshape((-1, 3))

    print(f'points: {points_3d}')
    # Identify pixels that match the unchanged color
    mask_unchanged = [False for _ in range(len(points_3d))]
    for unchanged_color in unchanged_colors:
        temp = np.all(points_3d == unchanged_color, axis=1)
        mask_unchanged = np.array([temp[i] or mask_unchanged[i] for i in range(len(temp))])

    print(f'mask: {mask_unchanged}')
    # Apply PCA to pixels that don't match the unchanged color using SVD
    # points_to_transform = points_3d[~mask_unchanged][:, 1:]
    points_to_transform = points_3d[:, 1:]
    U, S, Vt = np.linalg.svd(points_to_transform, full_matrices=False)

    # Take the first two components
    transformed_points = U[:, :2] @ np.diag(S[:2]) @ Vt[:2, :]

    # Scale the transformed points to the range [0, 255]
    scaled_green = np.interp(transformed_points[:, 0], (transformed_points[:, 0].min(), transformed_points[:, 0].max()), (0, 255))
    scaled_blue = np.interp(transformed_points[:, 1], (transformed_points[:, 1].min(), transformed_points[:, 1].max()), (0, 255))

    # Create an empty array for the final image
    transformed_image = np.zeros_like(points_3d)

    # Fill the unchanged pixels with the original values
    transformed_image[mask_unchanged] = unchanged_color

    # Map the transformed pixels to the correct channels
    transformed_image[:,1] = scaled_green
    transformed_image[:,2] = scaled_blue

    # Reshape the transformed image back to its original shape
    transformed_image = transformed_image.reshape(image.shape)

    # Write it to uploads
    nored_image_name = f'nored_{image_name}'
    plt.axis('off')
    plt.imshow(transformed_image / 255.0, origin='upper')
    plt.savefig(f'{upload_path}/{nored_image_name}', bbox_inches='tight', pad_inches=0)

    # return file name
    return nored_image_name

    # Display the image
    # plt.figure(figsize=(8, 8))
    # plt.imshow(transformed_image / 255.0, origin='upper')
    # plt.title('Mapped 2D Projection with Unchanged Color')
    # plt.xlabel('Green')
    # plt.ylabel('Blue')
    # plt.show()

nored([[255,255,255]], './uploads','image.png')