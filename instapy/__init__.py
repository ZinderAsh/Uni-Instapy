from instapy.numpy_color2gray import grayscale_filter as color2gray
from instapy.numpy_color2sepia import sepia_filter as color2sepia
import cv2

def grayscale_image(input_filename, output_filename=None):
    """
    Applies a grayscale filter to an image
    Args:
        input_filename (string): The filename of the image to apply filter to
        [output_filename]: The filename to save the new image to
    Returns:
        int[:,:]: The new image in a 2d numpy array
    """
    image = cv2.imread(input_filename)
    image = color2gray(image)
    if (output_filename):
        cv2.imwrite(output_filename, image)
    return image

def sepia_image(input_filename, output_filename=None):
    """
    Applies a sepia filter to an image
    Args:
        input_filename (string): The filename of the image to apply filter to
        [output_filename]: The filename to save the new image to
    Returns:
        int[:,:,3]: The new image in a 3d numpy array
    """
    image = cv2.imread(input_filename)
    image = color2sepia(image)
    if (output_filename):
        cv2.imwrite(output_filename, image)
    return image