import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def ft_load(path: str):
    """
Load an image from a file path.

Args:
    path (str): Path to the image file.

Returns:
    img (Image): Loaded image."""
    if not path:
        raise ValueError("Argument cannot be empty")
    if not isinstance(path, str) or len(path) < 6:
        raise TypeError("Arguments are bad")

    try:
        img = Image.open(path)
    except FileNotFoundError as error:
        print(type(error), __name__, error)
        return
    
    return img

def rgb(img: Image, path:str):
    """
Convert an image to RGB and print its shape.

Args:
    img (Image): Image to convert.
    path (str): Image file path.

Returns:
    np.ndarray: RGB image array.
    """
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise TypeError("Wrong file format")
    rgb_image = img.convert('RGB')
    arr = np.array(rgb_image)
    print(f"The shape of image is: {arr.shape}")

    return arr

def slicing(img:Image, path: str):
    """
Convert an image to grayscale, crop it,
display and save the result.

Args:
    img (Image): Image to process.
    path (str): Image file path.

Returns:
    np.ndarray: Cropped grayscale image.
    """
    if not path.lower().endswith('.jpeg'):
        raise TypeError("Wrong file format")
    gray_image = np.array(img.convert('L'))
    cropped = gray_image[:400, :400]
    cropped_gray = cropped[:, :, np.newaxis]
    print(f"New shape after slicing: {cropped_gray.shape} or {cropped.shape}")
    plt.imshow(cropped, cmap='gray')
    plt.savefig("cropped_img.jpeg")

    return cropped_gray