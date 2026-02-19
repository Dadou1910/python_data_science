from load_image import ft_load

try:
    print(ft_load("landscape.jpg"))
except (ValueError, TypeError) as error:
    print(type(error), __name__, error)