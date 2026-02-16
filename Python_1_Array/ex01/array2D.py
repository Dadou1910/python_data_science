def slice_me(family: list, start: int, end: int) -> list:
    """
Slice a 2D list and display its shape.

Takes a list of lists and returns a sliced
version from index start to end.
Prints the original and new shapes.

Args:
    family (list): 2D list to slice.
    start (int): Starting index.
    end (int): Ending index.

Returns:
    list: The sliced 2D list.
    """
    if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("The arguments are bad")
    if not family:
        raise ValueError("family cannot be empty")
    len_list = len(family[0])
    for member in family:
        if not isinstance(member, list):
            raise TypeError("list argument should contain list of strings")
        if len(member) != len_list:
            raise ValueError("All lists must have the same size")

    new_family = family[start:end]
    if new_family:
        print(f"My shape is: ({len(family)}, {len(family[0])})")
        print(f"My new shape is: ({len(new_family)}, {len(new_family[0])})")
    else:
        print("My new shape is: (0, 0)")
    return new_family
