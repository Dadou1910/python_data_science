from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """Retourne un décorateur limitant le nombre d'appels d'une fonction."""
    if not isinstance(limit, int) or limit < 0:
        raise TypeError("limit must be a non-negative int")

    def callLimiter(function: Callable) -> Callable:
        """Décorateur appliquant une limite d'appels à la fonction donnée."""
        count = 0

        def limit_function(*args: Any, **kwargs: Any):
            """Exécute la fonction tant que la limite n'est pas dépassée."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwargs)

        return limit_function

    return callLimiter
