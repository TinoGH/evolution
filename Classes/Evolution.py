from typing import List

from Classes.Animal import Animal
from random import shuffle


class Evolution:
    """

    """
    _plants_number_of_new_ones = 100
    _plants_growth_rate = 2

    def __init__(self, number_starting_animals: int):
        """
        :type number_starting_animals: int

        """
        assert number_starting_animals > 0
        self._plants = 1000
        self._animals: List['Animal'] = [Animal() for i in range(number_starting_animals)]

    def __str__(self):
        """

        :return:
        """
        return '\n'.join([str(animal.get_main_traits()) for animal in self._animals])

    def pop_new_animal(self):
        """

        """
        self._animals.append(Animal())

    def step_reproduce(self):
        """

        """
        self._plants *= Evolution._plants_growth_rate
        self._plants += Evolution._plants_number_of_new_ones
        new_animals: List['Animal'] = [animal.give_birth() for animal in self._animals]
        self._animals += new_animals

    def step_feed(self):
        """

        """
        shuffle(self._animals)
        for animal in self._animals:
            traits = animal.get_main_traits()
            food_needed = traits['POPULATION'] * traits['SIZE']
            if 'HERBIVORE' in traits:
                if self._plants >= food_needed:
                    self._plants -= food_needed
                    animal.eat()
                else:
                    self._plants = 0
            elif 'CARNIVORE' in traits:
                i = 0
                while i < len(self._animals):
                    prey = self._animals[i]
                    if (prey is not animal) and (prey.can_be_eaten_by(animal)):
                        food_needed -= prey.meat()
                        self._animals.pop(i)
                    else:
                        i += 1
                    if food_needed <= 0:
                        animal.eat()
                        break

    def step_survive(self):
        """

        return:
        """
        self._animals = [animal for animal in self._animals if animal.survive()]
        return len(self._animals)

