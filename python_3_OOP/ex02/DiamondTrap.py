from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Changes the physical characteristics of characters"""
    def __init__(self, first_name, is_alive=True):
        """Creates an instance of the King class"""
        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise TypeError("bad arguments")
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Sets a different eye colour."""
        self.eyes = color

    def set_hairs(self, color):
        """Sets a different hair colour."""
        self.hairs = color

    def get_eyes(self):
        """Returns the eye colour."""
        return self.eyes

    def get_hairs(self):
        """Returns the hair colour."""
        return self.hairs
