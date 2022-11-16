# pp.442 Electronic Fundamentals
import math

DEGREE_SYMBOL = "\u00B0"


class ImpedanceTriangle:

    def __init__(self, resistor: [int | float] = 47.0, xc: [int | float] = 100.0):
        """
        Calculates the phase angle, and impedance of a simple rc circuit

        :resistor: in ohms
        :xc: result of 1/(2pi*f*c) in ohms
        Examples:
            >>> x = ImpedanceTriangle()
            >>> x.phase_angle
            64.82647547546983
            >>> x.z
            110.4943437466371
        """
        self.resistor = resistor
        self.xc = xc

    @property
    def phase_angle(self):
        return math.degrees(math.atan(self.xc / self.resistor))

    @property
    def z(self):
        return math.sqrt(self.resistor ** 2 + self.xc ** 2)

    def __repr__(self):
        return f'xc={self.xc:,.2f}, resistance={self.resistor:,.2f}, z={self.z:,.2f},' \
               f' phase angle={self.phase_angle:.2f}{DEGREE_SYMBOL}'


example_10_1 = ImpedanceTriangle()
print(example_10_1)
related_problem_10_1 = ImpedanceTriangle(resistor=1e3, xc=2.2e3)
print(related_problem_10_1)
