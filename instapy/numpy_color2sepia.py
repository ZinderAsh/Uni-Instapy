import numpy as np

def sepia_filter(image):
    """
    Applies a sepia filter to an image using numpy
    Args:
        image (int[:,:,3]): The image (3d numpy array) to apply filter to
    Returns:
        int[:,:,3]: The new image in a 3d numpy array
    """
    weights = np.array([[.131, .534, .272],
                        [.168, .686, .349],
                        [.189, .769, .393]])
    sepia = (image @ weights.T).clip(0, 255)
    return sepia.astype(np.uint8)