from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character"""
    def __init__(self, first_name, is_alive=True):
        """initializes a Character instance"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Changes the status of a character to not alive"""
        self.is_alive = False


class Stark(Character):
    """Class for a Stark character"""
    def __init__(self, first_name, is_alive=True):
        """initializes a Stark instance"""
        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise TypeError("bad arguments")
        super().__init__(first_name, is_alive)

    def die(self):
        """Changes the status of a character to not alive"""
        super().die()
