
from Classes.Dna.Nucleotide import Nucleotide


class Gene:
    """

    """
    _number_nucleotides = 4

    def __init__(self):
        """

        """
        self._nucleotides = [Nucleotide() for i in range(Gene._number_nucleotides)]

    def __str__(self):
        """

        :return:
        """
        return "".join([str(nucleotide) for nucleotide in self._nucleotides])

    def __copy__(self):
        """

        :return:
        """
        gene = type(self)()
        for i in range(Gene._number_nucleotides):
            gene._nucleotides[i] = self._nucleotides[i].__copy__()
        return gene

    def get_strength(self):
        """

        :return:
        """
        result: int = 1
        for value in [nucleotide.get_value() for nucleotide in self._nucleotides]:
            result += value
        return result

    def mutate(self, probability: float):
        """
        :type probability: float
        :param probability:
        """
        probability /= Gene._number_nucleotides
        for nucleotide in self._nucleotides:
            nucleotide.mutate(probability)
