import numpy as np
from numba import jit

@jit
def sepia_filter(image):
    """
    Applies a sepia filter to an image using numba
    Args:
        image (int[:,:,3]): The image (3d numpy array) to apply filter to
    Returns:
        int[:,:,3]: The new image in a 3d numpy array
    """
    sepia = np.empty(image.shape, dtype=np.uint8)
    weights = [[.131, .534, .272],
               [.168, .686, .349],
               [.189, .769, .393]]
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            bgr = [0.0, 0.0, 0.0]
            for c1 in range(3):
                for c2 in range(3):
                    bgr[c1] += image[x,y,c2] * weights[c1][c2]
            for c in range(3):
                sepia[x,y,c] = min([bgr[c], 255])
    return sepia