class calculator:
    """Does calculations with a scalar"""
    def __init__(self):
        """Initializes a calculator instance"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Adds the numbers from two lists"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("Arg should be a scalar")
        if len(V1) != len(V2):
            raise TypeError("Lists should be the same size")
        res = [a * b for a, b in zip(V1, V2)]
        print(f"Dot product is: {sum(res)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Multiplies the numbers from two lists"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("Arg should be a scalar")
        if len(V1) != len(V2):
            raise TypeError("Lists should be the same size")
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is :{res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Multiplies the numbers from two lists"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("Arg should be a scalar")
        if len(V1) != len(V2):
            raise TypeError("Lists should be the same size")
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is:{res}")
