import numpy as np
from numba import jit

@jit
def grayscale_filter(image):
    """
    Applies a grayscale filter to an image using numba
    Args:
        image (int[:,:,3]): The image (3d numpy array) to apply filter to
    Returns:
        int[:,:,3]: The new image in a 3d numpy array
    """
    grayscale = np.empty(image.shape[:2], dtype=np.uint8)
    weights = [0.07, 0.72, 0.21]
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            total = 0
            for c in range(3):
                total += image[x,y,c] * weights[c]
            grayscale[x,y] = total
    return grayscale