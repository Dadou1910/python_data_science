def ft_filter(func, values):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if func is None:
        values = [value for value in values if value]
    else:
        values = [value for value in values if func(value)]
    return (value for value in values)
