# Instapy

A package and script to apply a grayscale or sepia filter to images, using either python, numpy or numba.
Written for a university assignment.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install instapy.
Type this into the command line while inside the directory containing setup.py.
```
pip install .
```

## Dependencies

These packages are required for this package:
- numpy (v1.19.1)
- numba (v0.52.2)
- opencv-python (v4.4.0.44)

Install these using [pip](https://pip.pypa.io/en/stable/).
```
pip install numpy
pip install numba
pip install opencv-python
```

## Usage

Running scripts from the command line.

```bash
# Display all arguments available for the script
instapy -h

## Examples

# Perform grayscale filter on input and save file to output
instapy -g -f input -o output

# Perform sepia filter on input and scale the image to 0.5x size
instapy -se -sc 0.5 -f input -o output

# Perform grayscale filter using the python implementation (numpy is used by default)
instapy -g -i python -f input -o output
```


Using the package in python scripts.

```python
import instapy

# Common functions that always use the numpy implementation
image = instapy.grayscale_image("filename.jpg")

image = instapy.sepia_image("filename.png")

# Add another filename to save the file as well
instapy.sepia_image("input.png", "output.png")


# Using specific implementations is done as such
from instapy.python_color2gray import grayscale_filter
from instapy.numba_color2gray import sepia_filter

image = cv2.imread("filename.jpg")

grayscale = grayscale_filter(image)

sepia = sepia_filter(image)

```

### Tests

```bash
# To run the tests, simply type the following in a command line in the package directory after installing the package
pytest

# If pytest is not installed, install it with pip.
pip install pytest
```
