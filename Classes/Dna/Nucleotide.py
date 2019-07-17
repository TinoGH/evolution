
from random import choice, random


class Nucleotide:
    """

    """
    _number_nucleotide_types = 4

    def __init__(self):
        """

        """
        self._name = choice(range(Nucleotide._number_nucleotide_types))

    def __str__(self):
        """

        :return:
        """
        return str(self._name)

    def __copy__(self):
        """

        :return:
        """
        nucleotide = type(self)()
        nucleotide._name = self._name
        return nucleotide

    def get_value(self):
        """

        :return:
        """
        return self._name

    def mutate(self, probability: float):
        """
        :type probability: float
        :param probability:
        """
        probability /= Nucleotide._number_nucleotide_types
        if random() < probability:
            possible_names = [i for i in range(Nucleotide._number_nucleotide_types)]
            possible_names.pop(self._name)
            self._name = choice(possible_names)
