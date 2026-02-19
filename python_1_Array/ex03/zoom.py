from load_image import ft_load, rgb, slicing

def main():
    path = 'animal.jpeg'
    try:
        img = ft_load(path)
        print(rgb(img, path))
        print(slicing(img, path))
    except (ValueError, TypeError) as error:
        print(type(error), __name__, error)

if __name__ == '__main__':
    main()