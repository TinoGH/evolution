
from Classes.Dna.Dna import Dna


class Animal:
    """

    """

    def __init__(self):
        """

        """
        self._dna = Dna()
        self._main_traits = self._dna.define_main_traits()
        self._has_eaten = False

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

    def eat(self):
        """

        """
        self._has_eaten = True

    def survive(self):
        """

        :return:
        """
        if self._has_eaten:
            self._has_eaten = False
            return True
        else:
            return False

    def can_be_eaten_by(self, animal: 'Animal'):
        """

        :type animal: 'Animal'
        :param animal:
        :return:
        """
        assert ('CARNIVORE' in animal._main_traits.keys())
        if animal._main_traits['SIZE'] > self._main_traits['SIZE']:
            return True
        else:
            return False

    def meat(self):
        """

        :return:
        """
        return self._main_traits['POPULATION'] * self._main_traits['SIZE']

    def is_herbivore(self):
        """

        :return:
        """
        return 'HERBIVORE' in self._main_traits.keys()

    def is_carnivore(self):
        """

        :return:
        """
        return 'CARNIVORE' in self._main_traits.keys()

    def get_main_traits(self):
        """

        :return:
        """
        return self._main_traits
