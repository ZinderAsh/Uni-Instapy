import numpy as np

def grayscale_filter(image):
    """
    Applies a grayscale filter to an image using numpy
    Args:
        image (int[:,:,3]): The image (3d numpy array) to apply filter to
    Returns:
        int[:,:,3]: The new image in a 3d numpy array
    """
    weights = [0.07, 0.72, 0.21]
    grayscale = image[...,:] @ weights
    return grayscale.astype(np.uint8)