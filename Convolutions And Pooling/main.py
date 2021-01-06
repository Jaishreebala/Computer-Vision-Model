import cv2
import numpy as np
from scipy import misc
i = misc.ascent()
import matplotlib.pyplot as plt

plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(i)
plt.show()

#Convolution

# Manipulate image:
i_transformed = np.copy(i)
size_x = i_transformed.shape[0] #Gets the x dimensions
size_y = i_transformed.shape[1] #Gets the y dimensions

# Create filters & weights - filter has to be 0 or 1 & if its not weight has to bring it down to 0 / 1
# filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]] # strong vertical lines
filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] # strong horizontal lines
weight = 1  # filters add up to 0 so weight is 1

# Create new image
for x in range(1, size_x-1):
    for y in range(1, size_y-1):
        output_pixel = 0.0
        output_pixel = output_pixel + (i[x - 1, y - 1] * filter[0][0])
        output_pixel = output_pixel + (i[x, y - 1] * filter[0][1])
        output_pixel = output_pixel + (i[x + 1, y - 1] * filter[0][2])
        output_pixel = output_pixel + (i[x - 1, y] * filter[1][0])
        output_pixel = output_pixel + (i[x, y] * filter[1][1])
        output_pixel = output_pixel + (i[x + 1, y] * filter[1][2])
        output_pixel = output_pixel + (i[x - 1, y + 1] * filter[2][0])
        output_pixel = output_pixel + (i[x, y + 1] * filter[2][1])
        output_pixel = output_pixel + (i[x + 1, y + 1] * filter[2][2])
        output_pixel = output_pixel * weight
        if(output_pixel<0):
            output_pixel = 0
        if(output_pixel>255):
            output_pixel = 255
        i_transformed[x, y]  = output_pixel
# plt.imshow(i_transformed)
# plt.show()


# Pooling - Maximum Pooling

new_x = int(size_x/2)
new_y = int(size_y/2)
newImage = np.zeros((new_y, new_y))

for x in range(0, size_x, 2):
    for y in range(0, size_y, 2):
        pixels = []
        pixels.append(i_transformed[x][y])
        pixels.append(i_transformed[x+1][y])
        pixels.append(i_transformed[x][y+1])
        pixels.append(i_transformed[x+1][y+1])
        pixels.sort(reverse=True)
        newImage[int(x/2)][int(y/2)] = pixels[0]

plt.imshow(newImage)
plt.show()