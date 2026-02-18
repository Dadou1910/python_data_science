from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """initializes a Lannister instance."""
        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise TypeError("bad arguments")
        super().__init__(first_name, is_alive)
        self.family_name = self.__class__.__name__
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Changes the status of a character to not alive"""
        super().die()

    def __str__(self):
        """Returns a string containing the class info"""
        r = f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return r

    def __repr__(self):
        """Returns a string containing the class info"""
        r = f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return r


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """initializes a Lannister instance."""
        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise TypeError("bad arguments")
        super().__init__(first_name, is_alive)
        self.family_name = self.__class__.__name__
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Changes the status of a character to not alive"""
        super().die()

    def __str__(self):
        """Returns a string containing the class info"""
        r = f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return r

    def __repr__(self):
        """Returns a string containing the class info"""
        r = f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return r

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """Creates a Lannister instance."""
        return Lannister(first_name, is_alive)
