from load_image import ft_load, ft_transpose, slicing

def main():
    path = 'animal.jpeg'
    try:
        img = ft_load(path)
        arr = slicing(img, path)
        print()
        print(ft_transpose(arr))
    except (ValueError, TypeError) as error:
        print(type(error), __name__, error)

if __name__ == '__main__':
    main()