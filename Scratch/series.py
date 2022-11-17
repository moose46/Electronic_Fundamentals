__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# series.py was created on October 28 2022 @ 10:37 AM
# Project: RealPythonTutorials
#
from fractions import Fraction
from functools import singledispatchmethod


class Series:
    @singledispatchmethod
    def __init__(self, value):
        raise ValueError(f'unsupported values: {value}')

    @__init__.register(float)
    @__init__.register(int)
    def _from_value(self, value):
        self._total = value

    @__init__.register(list)
    def _from_list(self, value):
        self._total = 0
        for v in value:
            self._total += v

    @property
    def value(self):
        return self._total


def continued_fraction(number):
    while True:
        yield (whole_part := int(number))
        fractional_part = number - whole_part
        try:
            number = 1 / fractional_part
        except ZeroDivisionError:
            break


print(list(continued_fraction(42)))

print(list(continued_fraction(Fraction(3,4))))

