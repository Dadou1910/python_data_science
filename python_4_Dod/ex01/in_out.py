def square(x: int | float) -> int | float:
    """Returns the squared of x."""
    if not isinstance(x, (int, float)):
        raise TypeError("Args should be int or float")
    return x**2


def pow(x: int | float) -> int | float:
    """Returns the exponent of x by x."""
    if not isinstance(x, (int, float)):
        raise TypeError("Args should be int or float")
    return x**x


def outer(x: int | float, function) -> object:
    """Appel une fonction en se rappelant du résulatat
    de l'appel précedent."""
    def inner() -> float:
        """Garde en mémoire les résultats de l'appel précédent"""
        nonlocal x
        count = function(x)
        x = count
        return count
    return inner
