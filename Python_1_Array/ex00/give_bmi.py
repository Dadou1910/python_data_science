def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
Compute BMI values from height and weight lists.

Each BMI is calculated as weight / height^2.

Args:
    height (list[int | float]): Heights in meters.
    weight (list[int | float]): Weights in kilograms.

Returns:
    list[float]: List of BMI values.

Raises:
    TypeError: If arguments are not lists of numbers or lengths differ.
    ValueError: If a height value is zero.
    """
    if not isinstance(height, list) or not isinstance(weight, list)\
       or len(height) != len(weight):
        raise TypeError("Argumetns are bad")
    for value in height + weight:
        if not isinstance(value, (int, float)):
            raise TypeError("List elements should be int or float")
    bmi = []   
    for h, w in zip(height, weight):
        if h == 0:
            raise ValueError("You cannot divide by 0 ;)")
        n = w / h**2
        bmi.append(n)
    
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Compare BMI values against a limit.

Args:
    bmi (list[int | float]): List of BMI values.
    limit (int): Threshold to compare against.

Returns:
    list[bool]: True if BMI >= limit, else False.

Raises:
    TypeError: If bmi is not a list of numbers or limit is not an int.
    """
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise TypeError("Argumetns should be a list and an int")
    for value in bmi:
        if not isinstance(value, (int, float)):
            raise TypeError("List elements should be int or float")
    
    lim = [value >= limit for value in bmi]
    
    return lim