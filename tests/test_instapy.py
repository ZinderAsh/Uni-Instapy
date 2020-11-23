import numpy as np
from instapy.python_color2gray import grayscale_filter as py_gray
from instapy.numpy_color2gray import grayscale_filter as numpy_gray
from instapy.numba_color2gray import grayscale_filter as numba_gray
from instapy.python_color2sepia import sepia_filter as py_sepia
from instapy.numpy_color2sepia import sepia_filter as numpy_sepia
from instapy.numba_color2sepia import sepia_filter as numba_sepia
import math
import pytest

@pytest.mark.parametrize("gray_filter", [py_gray, numpy_gray, numba_gray])
def test_grayscale(gray_filter):
    image = np.random.randint(0, 256, (600,400,3), dtype="uint8")
    grayscale = gray_filter(image)
    # Grayscale weights
    w = [0.07, 0.72, 0.21]
    # Test that the array is 2D not 3D, as each pixel only has one brightness value and not bgr
    assert grayscale.shape == (600,400)
    x = np.random.randint(0, 600)
    y = np.random.randint(0, 400)
    # Manually calculate gray value for randomly chosen pixel
    expected = math.floor(image[x,y,0] * w[0] + image[x,y,1] * w[1] + image[x,y,2] * w[2])
    assert grayscale[x,y] == expected

@pytest.mark.parametrize("sepia_filter", [py_sepia, numpy_sepia, numba_sepia])
def test_sepia(sepia_filter):
    image = np.random.randint(0, 256, (600,400,3), dtype="uint8")
    sepia = sepia_filter(image)
    # Sepia weights
    w = [[.131, .534, .272],
         [.168, .686, .349],
         [.189, .769, .393]]
    x = np.random.randint(0, 600)
    y = np.random.randint(0, 400)
    # Manually calculate BGR for randomly chosen pixel
    expected_b = math.floor(image[x,y,0] * w[0][0] + image[x,y,1] * w[0][1] + image[x,y,2] * w[0][2])
    expected_g = math.floor(image[x,y,0] * w[1][0] + image[x,y,1] * w[1][1] + image[x,y,2] * w[1][2])
    expected_r = math.floor(image[x,y,0] * w[2][0] + image[x,y,1] * w[2][1] + image[x,y,2] * w[2][2])
    # Confirm the values are correct
    assert sepia[x,y,0] == min([255,expected_b])
    assert sepia[x,y,1] == min([255,expected_g])
    assert sepia[x,y,2] == min([255,expected_r])