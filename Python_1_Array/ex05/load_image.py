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
    if not path.lower().endswith('.jpg'):
        raise TypeError("Wrong file format")

    try:
        img = Image.open(path).convert('RGB')
    except FileNotFoundError as error:
        print(type(error), __name__, error)
        return
    
    image = np.array(img)
    print(f"The shape of image is: {image.shape}")
    print(image)
    
    return image
