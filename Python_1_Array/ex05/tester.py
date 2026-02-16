from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red, save_img

try:
    array = ft_load("landscape.jpg")
    save_img(ft_invert(array), 'invert')
    save_img(ft_red(array), 'red')
    save_img(ft_green(array), 'green')
    save_img(ft_blue(array), 'blue')
    save_img(ft_grey(array), 'gray')
    print(ft_invert.__doc__)
except Exception as error:
    print(type(error), __name__, error)