from PIL import Image
import numpy as np

def save_img(array: np.ndarray, color: str) -> None:
    """Save array as {color}_img.jpg."""

    if not isinstance(array, np.ndarray):
        raise TypeError("Expected numpy array")

    img = Image.fromarray(array.astype(np.uint8))
    img.save(f"{color}_img.jpg")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""

    if not isinstance(array, np.ndarray):
        raise TypeError("Expected numpy array")

    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only red channel."""

    if not isinstance(array, np.ndarray):
        raise TypeError("Expected numpy array")

    red = array.copy()
    red[:,:,1] = 0
    red[:,:,2] = 0
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only green channel."""

    if not isinstance(array, np.ndarray):
        raise TypeError("Expected numpy array")

    green = array.copy()
    green[:,:,0] = 0
    green[:,:,2] = 0
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only blue channel."""

    if not isinstance(array, np.ndarray):
        raise TypeError("Expected numpy array")

    blue = array.copy()
    blue[:,:,0] = 0
    blue[:,:,1] = 0
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert image to grayscale."""

    if not isinstance(array, np.ndarray):
        raise TypeError("Expected numpy array")

    grey = array.copy()

    grey_val = (
        0.299 * array[:,:,0] +
        0.587 * array[:,:,1] +
        0.114 * array[:,:,2]
    )

    grey[:,:,0] = grey_val
    grey[:,:,1] = grey_val
    grey[:,:,2] = grey_val

    return grey.astype(np.uint8)
