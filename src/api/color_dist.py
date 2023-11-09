from colormath.color_objects import LabColor, sRGBColor
from colormath.color_diff import delta_e_cie2000
from PIL import Image
import numpy as np
import math
# Load the image
#image = Image.open('OIP.png')  # Replace with the path to your image

# Example usage: calculate the CIEDE2000 color difference between two pixels in the image
# Replace (x1, y1) and (x2, y2) with the pixel coordinates you want to compare
x1, y1 = 100, 100
x2, y2 = 200, 200

pixel1 = image.getpixel((x1, y1))
pixel2 = image.getpixel((x2, y2))
# Convert RGB values to Lab color space

def rgb_to_lab(rgb):
    # Handle both grayscale and color images
    if isinstance(rgb, int):
        # Grayscale image, RGB value is an integer
        rgb = (rgb, rgb, rgb)
    #r, g, b = [x / 255.0 for x in rgb]
    # Normalize RGB values
    r, g, b = [x / 255.0 for x in rgb]

    # Define the D65 illuminant values
    Xn, Yn, Zn = 95.047, 100.000, 108.883

    # Convert to XYZ
    if r > 0.04045:
        r = math.pow((r + 0.055) / 1.055, 2.4)
    else:
        r = r / 12.92
    if g > 0.04045:
        g = math.pow((g + 0.055) / 1.055, 2.4)
    else:
        g = g / 12.92
    if b > 0.04045:
        b = math.pow((b + 0.055) / 1.055, 2.4)
    else:
        b = b / 12.92

    r *= 100.0
    g *= 100.0
    b *= 100.0

    X = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    Y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    Z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    # Convert to Lab
    X /= Xn
    Y /= Yn
    Z /= Zn

    if X > 0.008856:
        X = math.pow(X, 1.0/3.0)
    else:
        X = (903.3 * X + 16.0) / 116.0
    if Y > 0.008856:
        Y = math.pow(Y, 1.0/3.0)
    else:
        Y = (903.3 * Y + 16.0) / 116.0
    if Z > 0.008856:
        Z = math.pow(Z, 1.0/3.0)
    else:
        Z = (903.3 * Z + 16.0) / 116.0

    L = max(0.0, (116.0 * Y) - 16.0)
    a = (X - Y) * 500.0
    b = (Y - Z) * 200.0

    return L, a, b

lab_color1 = np.array(rgb_to_lab(pixel1), dtype=float)
lab_color2 = np.array(rgb_to_lab(pixel2), dtype=float)

# Calculate the CIEDE2000 color difference manually
def ciede2000(lab1, lab2):
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    C1 = math.sqrt(a1**2 + b1**2)
    C2 = math.sqrt(a2**2 + b2**2)
    C_bar = (C1 + C2) / 2

    G = 0.5 * (1 - math.sqrt(C_bar**7 / (C_bar**7 + 25**7)))

    a1_prime = (1 + G) * a1
    a2_prime = (1 + G) * a2

    C1_prime = math.sqrt(a1_prime**2 + b1**2)
    C2_prime = math.sqrt(a2_prime**2 + b2**2)
    C_bar_prime = (C1_prime + C2_prime) / 2

    h1_prime = math.degrees(math.atan2(b1, a1_prime))
    if h1_prime < 0:
        h1_prime += 360

    h2_prime = math.degrees(math.atan2(b2, a2_prime))
    if h2_prime < 0:
        h2_prime += 360

    H_bar_prime = (h1_prime + h2_prime) / 2

    T = 1 - 0.17 * math.cos(math.radians(H_bar_prime - 30)) + 0.24 * math.cos(math.radians(2 * H_bar_prime)) + 0.32 * math.cos(math.radians(3 * H_bar_prime + 6)) - 0.20 * math.cos(math.radians(4 * H_bar_prime - 63))

    Delta_L = L2 - L1
    Delta_C = C2_prime - C1_prime

    h_diff = h2_prime - h1_prime
    if abs(h_diff) <= 180:
        Delta_H = h2_prime - h1_prime
    elif h_diff > 180:
        Delta_H = h2_prime - h1_prime - 360
    else:
        Delta_H = h2_prime - h1_prime + 360

    Delta_H = 2 * math.sqrt(C1_prime * C2_prime) * math.sin(math.radians(Delta_H / 2))

    L_bar_prime = (L1 + L2) / 2
    C_bar_prime = (C1_prime + C2_prime) / 2

    h1_prime_degrees = math.degrees(math.atan2(b1, a1_prime))
    if h1_prime_degrees < 0:
        h1_prime_degrees += 360

    h2_prime_degrees = math.degrees(math.atan2(b2, a2_prime))
    if h2_prime_degrees < 0:
        h2_prime_degrees += 360

    H_bar_prime_degrees = (h1_prime_degrees + h2_prime_degrees) / 2

    L_bar_prime = (L1 + L2) / 2
    C_bar_prime = (C1_prime + C2_prime) / 2

    T = 1 - 0.17 * math.cos(math.radians(H_bar_prime_degrees - 30)) + 0.24 * math.cos(math.radians(2 * H_bar_prime_degrees)) + 0.32 * math.cos(math.radians(3 * H_bar_prime_degrees + 6)) - 0.20 * math.cos(math.radians(4 * H_bar_prime_degrees - 63))

    S_L = 1 + (0.015 * (L_bar_prime - 50)**2) / math.sqrt(20 + (L_bar_prime - 50)**2)
    S_C = 1 + 0.045 * C_bar_prime
    S_H = 1 + 0.015 * C_bar_prime * T

    R_T = -2 * math.sqrt(C_bar_prime**7 / (C_bar_prime**7 + 25**7)) * math.sin(math.radians(60 * math.exp(-((H_bar_prime_degrees - 275) / 25)**2)))

    Delta_E = math.sqrt((Delta_L / (S_L))**2 + (Delta_C / (S_C))**2 + (Delta_H / (S_H))**2 + R_T * (Delta_C / (S_C)) * (Delta_H / (S_H)))

    return Delta_E

# Calculate the CIEDE2000 color difference manually
delta_e = ciede2000(lab_color1, lab_color2)

#Print results of delta_e variable