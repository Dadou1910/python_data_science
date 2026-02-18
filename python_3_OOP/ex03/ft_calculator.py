class calculator:
    """Does calculations with a scalar"""
    def __init__(self, object):
        """Initializes a calculator instance"""
        if not isinstance(object, list):
            raise TypeError("Arg should be a list")
        self.object = object

    def __add__(self, object) -> None:
        """Adds the numbers in the list"""
        if not isinstance(object, (int, float)):
            raise TypeError("Arg should be a scalar")
        for i in range(len(self.object)):
            self.object[i] += object
        print(self.object)

    def __mul__(self, object) -> None:
        """Multiplies the numbers in the list"""
        if not isinstance(object, (int, float)):
            raise TypeError("Arg should be a scalar")
        for i in range(len(self.object)):
            self.object[i] *= object
        print(self.object)

    def __sub__(self, object) -> None:
        """Substracts the numbers in the list"""
        if not isinstance(object, (int, float)):
            raise TypeError("Arg should be a scalar")
        for i in range(len(self.object)):
            self.object[i] -= object
        print(self.object)

    def __truediv__(self, object) -> None:
        """Divides the numbers in the list"""
        if not isinstance(object, (int, float)):
            raise TypeError("Arg should be a scalar")
        if object == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        for i in range(len(self.object)):
            self.object[i] /= object
        print(self.object)
