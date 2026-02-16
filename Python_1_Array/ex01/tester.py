from array2D import slice_me

try:
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print()
    print(slice_me(family, 1, -2))
    print()
    print(slice_me([], 1, -2))
    print()
    print(slice_me(family, 23423, 234232))
    print()
except (TypeError, ValueError) as error:
    print(type(error), __name__, error)