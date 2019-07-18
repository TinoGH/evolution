from typing import Dict, Any

from Classes.Dna.Gene import Gene
from Classes.Dna.traits import TRAITS


class Dna:
    """

    """
    _number_main_traits = 4
    _mutation_probability_coefficient = 0.1

    def __init__(self):
        """

        """
        self._genes = dict()
        for trait in TRAITS:
            self._genes[trait] = Gene()

    def __copy__(self):
        """

        :return:
        """
        dna = type(self)()
        for trait in TRAITS:
            dna._genes[trait] = self._genes[trait].__copy__()
        return dna

    def __str__(self):
        """

        :return:
        """
        return "\n".join([(trait + " : " + str(self._genes[trait].get_strength())) for trait in self._genes.keys()])

    def define_main_traits(self):
        """

        :return:
        """
        main_traits: Dict[str, int] = dict()
        genes = self._genes.copy()
        main_traits['POPULATION'] = genes.pop('POPULATION').get_strength()
        main_traits['SIZE'] = genes.pop('SIZE').get_strength()
        strengths = [genes[trait].get_strength() for trait in genes.keys()]
        traits = [trait for trait in genes.keys()]
        for i in range(Dna._number_main_traits):
            index = strengths.index(max(strengths))
            main_traits[traits.pop(index)] = strengths.pop(index)
        return main_traits

    def mutate(self):
        """

        """
        probability: float = Dna._mutation_probability_coefficient * self._genes['POPULATION'].get_strength()
        for trait in self._genes.keys():
            self._genes[trait].mutate(probability)
