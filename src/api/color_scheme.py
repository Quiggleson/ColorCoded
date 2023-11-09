from PIL import Image, ImageChops, ImageOps
import numpy as np
import os, imghdr, colorsys, cv2

# Pass in
#user_image = "OIP.png" Connect with photo image.
#output_path = "output_image.png" Connect with download area.

# Simulating tritanopia
def tritanopia(user_image, output_path):
        original_image = cv2.imread(user_image)
        blue = original_image[:, :, 0]
        green = original_image[:, :, 1]
        red = original_image[:, :, 2]

        black = np.zeros_like(blue)

        new_image = original_image.copy()
        new_image[..., 0] = original_image[..., 1] # set blue to green

        cv2.imwrite(output_path, new_image)
tritanopia(user_image, output_path) # Passes back the path to download area
                                    # and the altered image. 