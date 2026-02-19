from typing import Any
import math


def _to_sorted_floats(args: tuple[Any, ...]) -> list[float]:
    """Convertit les arguments numériques en floats triés."""
    nums: list[float] = []
    for x in args:
        if not isinstance(x, (int, float)):
            raise TypeError
        nums.append(float(x))
    nums.sort()
    return nums


def _mean(nums: list[float]) -> float:
    """Calcule la moyenne."""
    return sum(nums) / len(nums)


def _median(nums: list[float]) -> float:
    """Calcule la médiane d'une liste triée."""
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    return (nums[mid - 1] + nums[mid]) / 2.0


def _quantile(nums: list[float], p: float) -> float:
    """Calcule un quantile inclusif avec interpolation linéaire."""
    n = len(nums)
    if n == 1:
        return nums[0]

    h = (n - 1) * p + 1.0
    hf = math.floor(h)
    hc = math.ceil(h)

    x_low = nums[hf - 1]
    x_high = nums[hc - 1]

    if hf == hc:
        return x_low
    return x_low + (h - hf) * (x_high - x_low)


def _pop_variance(nums: list[float]) -> float:
    """Calcule la variance de population."""
    n = len(nums)
    m = _mean(nums)
    return sum((x - m) ** 2 for x in nums) / n


def _pop_stdev(nums: list[float]) -> float:
    """Calcule l'écart-type de population."""
    return math.sqrt(_pop_variance(nums))


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Affiche les statistiques demandées."""
    ops = list(kwargs.values())

    def _print_errors() -> None:
        """Affiche 'ERROR' pour chaque mauvais arg."""
        for op in ops:
            print("ERROR")

    if len(args) == 0:
        _print_errors()
        return

    try:
        nums = _to_sorted_floats(args)
    except TypeError:
        _print_errors()
        return

    for op in ops:
        if op == "mean":
            print(f"mean : {_mean(nums)}")
        elif op == "median":
            print(f"median : {_median(nums)}")
        elif op == "quartile":
            q1 = _quantile(nums, 0.25)
            q3 = _quantile(nums, 0.75)
            print(f"quartile : [{q1}, {q3}]")
        elif op == "std":
            print(f"std : {_pop_stdev(nums)}")
        elif op == "var":
            print(f"var : {_pop_variance(nums)}")
