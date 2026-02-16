from PIL import Image
import matplotlib.pyplot as plt
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
    print(f"The shape of image is: {cropped_gray.shape} or {cropped.shape}")
    plt.imshow(cropped, cmap='gray')
    plt.savefig("cropped_img.jpeg")
    print(cropped_gray)
    return cropped

def ft_transpose(cropped):
    """
Manually transpose a (H, W, 1) image array

Args:
    cropped (np.ndarray): Cropped grayscale image

Returns:
    rotated (np.ndarray): the grayscale rotated image
    """
    if not isinstance(cropped, np.ndarray):
        raise TypeError("Arguments are bad")
    if cropped.size == 0:
        raise ValueError("Array param in ft_transpose cannot be empty")
    if cropped.ndim != 2:
        raise ValueError("Array must be (H, W)")
    
    h, w = cropped.shape
    rotated = np.zeros((w, h), dtype=cropped.dtype)
    for i in range(h):
        for j in range(w):
            rotated[w-1-j][i] = cropped[i][w-1-j]

    print(f"New shape after Transpose: {rotated.shape}")
    plt.imshow(rotated, cmap='grey')
    plt.savefig('rotated_img.jpeg')

    return rotated
    