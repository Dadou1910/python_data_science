from PIL import Image
import numpy as np

def ft_load(path: str):
    """
Load an image from a file path.

Prints the shape of the image and returns
its RGB pixel values as a NumPy array.

Args:
    path (str): Path to the image file.

Returns:
    np.ndarray: RGB pixel array of the image."""
    if not path:
        raise ValueError("Argument cannot be empty")
    if not isinstance(path, str) or len(path) < 6:
        raise TypeError("Arguments are bad")
    if path[-5:].lower() != '.jpeg' and path[-4:] != '.jpg':
        raise TypeError("Wrong file format")
    
    try:
        img = Image.open(path).convert('RGB')
    except FileNotFoundError as error:
        print(type(error), __name__, error)
        return
    
    arr = np.array(img)
    print(f"The shape of image is: {arr.shape}")
    return arr
    