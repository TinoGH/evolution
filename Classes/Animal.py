
from Classes.Dna.Dna import Dna


class Animal:
    """

    """

    def __init__(self):
        """

        """
        self._dna = Dna()
        self._main_traits = self._dna.define_main_traits()

    def __str__(self):
        """

        :return:
        """
        return str(self._main_traits)

    def __copy__(self):
        """

        :return:
        """
        animal = type(self)()
        animal._dna = self._dna.__copy__()
        return animal

    def give_birth(self):
        """

        :return:
        """
        animal = self.__copy__()
        animal._dna.mutate()
        animal._main_traits = animal._dna.define_main_traits()
        return animal
