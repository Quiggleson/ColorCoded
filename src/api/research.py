import matplotlib.pyplot as plt
import numpy as np

def codistance(M, f):
    ans = []
    for r1 in M:
        for c1 in r1:
            ans_row = []
            for r2 in M:
                for c2 in r2:
                    ans_row.append(f(c1,c2))
            ans.append(ans_row)
    return ans

def f(c1, c2):
    return c1 - c2

def hex_to_rgb(hex_val):
    red = (hex_val >> 16) & 0xFF
    green = (hex_val >> 8) & 0xFF
    blue = hex_val & 0xFF
    return red, green, blue

M = [
    [0x819a35, 0xedfa91, 0x11af00],
    [0xb611d0, 0xfade00, 0xffaf00],
    [0x222244, 0xbfffb1, 0xaaaf00]
    ]

# gM = [[format(x & 0x00FFFF, "#06x") for x in y] for y in M]
gM = [[x & 0x00FFFF for x in row] for row in M]
# print(gM)

codm = codistance(M, f)
codgm = codistance(gM, f)

M_rgb_values = [[hex_to_rgb(value) for value in row] for row in codm]
gm_rgb_values = [[hex_to_rgb(value) for value in row] for row in codgm]

# Create a NumPy array from the RGB tuples
M_rgb_array = np.array(M_rgb_values, dtype=np.uint8)
gm_rgb_array = np.array(gm_rgb_values, dtype=np.uint8)

plt.figure()
plt.imshow(codm,cmap="seismic",interpolation="nearest")
plt.title("Heatmap with M")
color_bar = plt.colorbar()


plt.figure()
plt.imshow(codgm,cmap="seismic",interpolation="nearest")
plt.title("Heatmap with gM")
color_bar = plt.colorbar()

plt.figure()
plt.imshow(M)
plt.title("M")
for i in range(len(M)):
    for j in range(len(M[0])):
        plt.text(j, i, f'{M[i][j]:X}', ha='center', va='center', color='w')


plt.figure()
plt.imshow(gM)
plt.title("gM")
for i in range(len(gM)):
    for j in range(len(gM[0])):
        plt.text(j, i, f'{gM[i][j]:06X}', ha='center', va='center', color='w')



plt.show()