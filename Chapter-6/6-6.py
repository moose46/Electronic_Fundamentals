# Chapter-6/6-6.py
""" Sum of two resistors in series and parallel
    This module contains the following functions:
    - 'Resistor.series' - Returns the sum of two resistors in series
    - 'Resistor.parallel - Returns the sum of two rsistors in parallel

    Examples:
    >>> Resistor.parallel(200,200)
    100.0
    >>> Resistor.series([200,200,50])
    450.0
    >>> x = Resistor


"""
from typing import Union


class Resistor:
    @staticmethod
    def series(resistors: list[float | int]) -> float:
        """ Rt = resistor1 + resistor2 + resistorN
        Examples:
        >>> Resistor.series([200,200])
        400.0

        resistor1: A number in ohms representing the first resistor
        resistor2 A number in ohms representing the second resisitor
        Returns:
             Rt:float with the sum (Rt) of resitor1 and resistor2 in ohms
        """
        total = 0
        [total := total + r for r in resistors]
        return round(float(total), 2)

    @staticmethod
    def parallel(r1: Union[float, int], r2: Union[float, int]) -> float:
        """Compute the sum of two parallel resistors
        Examples:
        >>> Resistor.parallel(100,100)
        50.0
        >>> Resistor.parallel(200,100)
        66.67

        resistor1: first resistor's value in ohms
        resistor2: second resistor's value in ohms
        Returns:
            The computed sum of two resistors in parallel
        """
        return round(float(((r1 ** -1) + (r2 ** -1)) ** -1), 2)

# print(Resistor.parallel(100, 100), chr(937))
# print(Resistor.parallel(200, 100), chr(937))
# print(Resistor.series(200, 100), chr(937))
# # Vth = (100 / (100 + 2500)) * 10Volts = .38V
# Vth = (100 / Resistor.series(100, 2500)) * 10
# print(f'{Vth:2.2f}V')
# Vth = 69 / 169 * 10
# print(f'Fig 6-44 Vth={Vth:2.2f}V')
#
# print(f'Fig 6-45 Rth={(((47 + 22) ** -1) + (100 ** -1)) ** -1 + 100:2.2f}{chr(937)}')
# print('mu=\u03BC  theta=\u03B8   beta=\u03B2  theta=\u0398  Degree=\u00B0')
