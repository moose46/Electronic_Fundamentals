# pp.442 Electronic Fundamentals
import math
import traceback

DEGREE_SYMBOL = "\u00B0"
MU_SYMBOL = "\u03BC"
THETA_SYMBOL = "\u03B8"


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
            >>> x.volts = 10
            >>> x.farads = 2.2e-6
            >>> x.frequency = 2e-3
            >>> x.calculate_all()
            >>> x.xc
            36171577.97543076
    """
        self._resistor = resistor
        self._xc = xc
        self._frequency = 0
        self._current = 0.0
        self._volts = 0.0
        self._farads = 0.0
        self._function_name = ""
        (self._filename, self._line_number, self._function_name, text) = traceback.extract_stack()[-2]
        self._def_name = text[:text.find('=')].strip()
        self._z = 0.0

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value: [int | float]):
        self._frequency = value

    @property
    def phase_angle(self) -> float:
        return math.degrees(math.atan(self._xc / self._resistor))

    @property
    def z(self):
        self._z = math.sqrt(self._resistor ** 2 + self._xc ** 2)
        return self._z

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value

    @property
    def volts(self):
        return self._volts

    @volts.setter
    def volts(self, value: [int | float]) -> float:
        self._volts = value

    @property
    def farads(self):
        return self._farads

    @farads.setter
    def farads(self, value: [int | float]) -> float:
        self._farads = value

    @property
    def xc(self):
        """ return capacitive reactance"""
        return self._xc

    def calculate_xc(self, frequency: [int | float], farads: [int | float]):
        """ calculate self._xc to the capacitive reactance of frequency and farads """
        self._farads = farads
        self._frequency = frequency
        self._xc = 1 / (2 * math.pi * frequency * farads)
        return self._xc

    def calculate_volts(self, current: [int | float]):
        self._current = current
        self._volts = current * self.z
        return self._volts

    def calculate_all(self):
        if self._frequency != 0 and self._farads != 0:
            self._xc = self._xc = 1 / (2 * math.pi * self._frequency * self._farads)
        else:
            print(f"\t*** Frequency {self._frequency} or farads {self._farads} not set ***")
        if self._volts != 0 and self._xc != 0:
            self._current = self._volts / self.z
        else:
            print(f"\t*** Volts {self._volts:2.2e} or Z {self.z:2.2e} not set ***")

    def __repr__(self):
        return f'- {self._def_name:20}:' \
               f'\n\txc = {self._xc:8.2e} {MU_SYMBOL}F={self._farads:8.2e} f={self._frequency:,.2e}' \
               f'\n\tZ = {self.z:8.2e}' \
               f'\n\t{THETA_SYMBOL} = {self.phase_angle:2.2f}{DEGREE_SYMBOL}' \
               f'\n\tR = {self._resistor:8.2e}' \
               f'\n\tV = {self._volts:.2f}' \
               f'\n\tI = {self._current:4.2e}' \
               f'  '


example_10_1 = ImpedanceTriangle()
print(example_10_1)
related_problem_10_1 = ImpedanceTriangle(resistor=1e3, xc=2.2e3)
print(related_problem_10_1)
# Example 10-2
example_10_2 = ImpedanceTriangle(resistor=10e3)
# set xc
example_10_2.calculate_xc(frequency=1e3, farads=.01e-6)
# get xc
example_10_2.calculate_volts(current=.2e-3)
print(example_10_2)
example_10_3 = ImpedanceTriangle(resistor=2.2e3)
example_10_3.farads = .022e-6
example_10_3.frequency = 1.5e3
# example_10_3.volts = 10
example_10_3.calculate_all()
print(example_10_3)
