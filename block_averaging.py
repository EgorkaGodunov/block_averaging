import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def block_averaging(image, yb, xb):
    new_image = np.zeros((yb, xb))
    fsy = image.shape[0] // yb
    fsx = image.shape[1] // xb
    for y in range(yb):
        ssy = fsy * (y + 1)
        for x in range(xb):
            ssx = fsx * (x + 1)
            new_image[y, x] = np.mean(image[y * fsy:ssy, x * fsx:ssx])
    return new_image



image = mpimg.imread('LenaImage.png')
plt.imshow(block_averaging(image, 50, 50))
plt.show()
